# [심화 실습] 프롬프트 차이가 만드는 결과 비교

> 🎯 목표: 나쁜 프롬프트의 실패 유형 3가지를 **실제로 재현**하고, 좋은 프롬프트로 교체했을 때 무엇이 달라지는지 측정한다.
> ⏱️ 예상 시간: 25~30분
> 💡 `examples/todo-api/` — Flask REST API 예제를 사용합니다.

---

## 왜 REST API인가

contact-book은 단일 파일이라 모호한 프롬프트를 줘도 Claude가 선택할 수 있는 범위가 좁습니다.
todo-api는 **`app.py`, `models.py`, `test_app.py`** 3개 파일과 **5개 엔드포인트**가 있어서,
모호한 요청을 주면 에이전트가 어디서든 어떤 방식으로든 구현할 수 있습니다.
그 선택의 폭이 바로 프롬프트 품질 차이가 드러나는 지점입니다.

**실패 유형 3가지:**

| 유형 | 나쁜 프롬프트의 증상 | 핵심 원인 |
|------|---------------------|-----------|
| **① 대상 불명** | 엉뚱한 엔드포인트·파일을 수정 | 어디를 바꿔야 하는지 명시 안 함 |
| **② 범위 폭발** | 건드리지 않아도 될 파일까지 전부 수정 | 어디까지만 바꿔야 하는지 명시 안 함 |
| **③ 형식 불명** | 로직은 맞는데 응답 구조가 전혀 다름 | 어떤 JSON 형식으로 응답해야 하는지 명시 안 함 |

---

## 사전 준비

### 가상환경 설정 및 의존성 설치

```bash
cd 경로/lessons/03-prompting-context/examples/todo-api

# 가상환경 생성
python3 -m venv .venv

# 활성화 (macOS / Linux)
source .venv/bin/activate
# 활성화 (Windows Git Bash)
# source .venv/Scripts/activate

# 의존성 설치
pip install -r requirements.txt
```

> 이후 모든 명령은 `(.venv)` 프롬프트가 표시된 상태에서 실행합니다.

### 동작 확인

```bash
pytest test_app.py -v
```
→ 8개 테스트 전부 통과해야 합니다.

### Git 초기화 (라운드 간 코드 복원용)

```bash
git init
git add app.py models.py test_app.py requirements.txt
git commit -m "initial: todo-api 실습 시작"
```

> 각 라운드에서 나쁜 프롬프트 실행 후 `git checkout -- app.py models.py test_app.py` 로 원래 코드로 되돌립니다.

### Claude Code 실행

```bash
claude
```

---

## 라운드 1: 대상 불명 — 에이전트가 어디를 수정할지 모를 때

### 배경

현재 `GET /todos`는 모든 항목을 그냥 다 반환합니다. 제목(title)으로 검색하는 기능을 추가하려 합니다.

```bash
# 지금은 검색이 안 됨 — 전체만 반환
curl http://localhost:4000/todos
```

검색 기능은 여러 방식으로 구현할 수 있습니다:
- `GET /todos?q=우유` 처럼 기존 엔드포인트에 쿼리 파라미터 추가
- `GET /search?q=우유` 처럼 별도 엔드포인트 신설
- `GET /todos/search/우유` 처럼 URL 경로 방식
- `models.py`에 검색 메서드 추가 후 라우터에서 호출
- ... 등

이 중 어떤 방식이 "맞는 것"인지 에이전트는 알 수 없습니다. 여러분이 알려주지 않으면.

---

### STEP 1-A: 나쁜 프롬프트

```
> 검색 기능 추가해줘
```

**응답을 보면서 기록하세요:**

| 관찰 항목 | 내 관찰 결과 |
|-----------|-------------|
| 어느 파일을 수정했나? | |
| 검색 엔드포인트 URL은? (`/todos?q=`, `/search?q=`, 다른 것?) | |
| `models.py`도 건드렸나? | |
| 테스트를 추가했나? | |
| 예상과 다른 점은? | |

```
> /clear
```

```bash
git checkout -- app.py models.py test_app.py
```

---

### STEP 1-B: 좋은 프롬프트

```
> app.py의 GET /todos 핸들러에 검색 기능을 추가해줘.
>
> 동작:
>   - URL 쿼리 파라미터 q를 받는다 (예: GET /todos?q=우유)
>   - q가 있으면 title에 q가 포함된 항목만 반환 (대소문자 구분 없음)
>   - q가 없으면 기존처럼 전체 반환
>
> 범위:
>   - app.py의 get_todos() 함수만 수정
>   - models.py는 건드리지 말 것
>
> 검증:
>   - test_app.py에 아래 케이스 2건 추가 후 pytest 실행
>     * q="우유" → 제목에 "우유" 포함 항목만 반환
>     * q="없는검색어" → 빈 배열 반환
```

**결과 확인:**

```bash
pytest test_app.py -v
```

실제 서버로도 확인하고 싶다면 **터미널 탭을 하나 더 열어서** 서버를 실행합니다.

```bash
# [새 터미널 탭] — 서버 실행
source .venv/bin/activate
python3 app.py
# 확인 후 Ctrl+C 로 종료
```

```bash
# [기존 터미널 탭] — 동작 확인
curl -X POST http://localhost:4000/todos -H "Content-Type: application/json" -d '{"title":"우유 사기"}'
curl -X POST http://localhost:4000/todos -H "Content-Type: application/json" -d '{"title":"빵 사기"}'
curl "http://localhost:4000/todos?q=우유" -s | python3 -m json.tool
```

**두 프롬프트의 차이:**

| 항목 | 나쁜 프롬프트 | 좋은 프롬프트 |
|------|-------------|-------------|
| 엔드포인트 방식 | (직접 기록) | GET /todos?q= |
| 수정된 파일 | (직접 기록) | app.py만 |
| 테스트 추가 | (직접 기록) | 2건 추가 후 통과 |

```
> /clear
```
```bash
git checkout -- app.py models.py test_app.py
```

---

## 라운드 2: 범위 폭발 — 에이전트가 너무 많이 바꿀 때

### 배경

현재 `POST /todos`는 `title`이 빈 문자열이어도 그냥 저장합니다.

```bash
# 아무 title 없이 생성 가능 — 이건 막아야 함
curl -X POST http://localhost:4000/todos \
     -H "Content-Type: application/json" \
     -d '{"title": ""}'
```

이걸 막으려면 `POST /todos` 핸들러에만 검증을 추가하면 됩니다.

---

### STEP 2-A: 나쁜 프롬프트

```
> 입력값 검증 추가해줘
```

**응답을 보면서 기록하세요:**

| 관찰 항목 | 내 관찰 결과 |
|-----------|-------------|
| 수정된 파일 전체 목록 | |
| `models.py`도 건드렸나? | |
| GET / PUT / DELETE에도 검증이 생겼나? | |
| 에러 메시지 형식이 일관적인가, 제각각인가? | |
| 원래 목적(POST /todos의 title 검증)만 됐나? | |

```
> /clear
```
```bash
git checkout -- app.py models.py test_app.py
```

---

### STEP 2-B: 좋은 프롬프트

```
> app.py의 POST /todos 핸들러에만 입력값 검증을 추가해줘.
>
> 검증 조건:
>   - 요청 body에 title 키가 없거나 빈 문자열("")이면
>     → 상태코드 400, 응답 본문 {"error": "title은 필수입니다."} 반환
>   - 위 조건이 아니면 기존 로직 그대로 실행
>
> 범위:
>   - app.py의 create_todo() 함수만 수정
>   - models.py, 다른 핸들러 함수는 건드리지 말 것
>
> 검증:
>   - test_app.py에 아래 케이스 2건 추가 후 pytest 실행
>     * title 없이 POST → 400 응답, {"error": "title은 필수입니다."} 확인
>     * title="" 으로 POST → 400 응답 확인
```

**결과 확인:**

```bash
pytest test_app.py -v
```

실제 동작을 확인하려면 **터미널 탭을 하나 더 열어서** 서버를 실행합니다.

```bash
# [새 터미널 탭] — 서버 실행
source .venv/bin/activate
python3 app.py
# 확인 후 Ctrl+C 로 종료
```

```bash
# [기존 터미널 탭] — 동작 확인
curl -X POST http://localhost:4000/todos \
     -H "Content-Type: application/json" \
     -d '{"title": ""}' -s | python3 -m json.tool
# {"error": "title은 필수입니다."} 가 나와야 함
```

**두 프롬프트의 차이:**

| 항목 | 나쁜 프롬프트 | 좋은 프롬프트 |
|------|-------------|-------------|
| 수정된 파일 수 | (직접 기록) | 1개 (app.py) |
| 수정된 함수 수 | (직접 기록) | 1개 (create_todo) |
| 에러 메시지 형식 | (직접 기록) | `{"error": "title은 필수입니다."}` |
| 기존 테스트 통과 | (직접 기록) | 전체 통과 |

```
> /clear
```
```bash
git checkout -- app.py models.py test_app.py
```

---

## 라운드 3: 형식 불명 — 에이전트가 응답 구조를 임의로 정할 때

### 배경

현재 API 응답 형식이 일관성이 없습니다:
- 성공: 그냥 데이터 반환 (예: `{"id": 1, "title": "우유 사기", "done": false}`)
- 실패: `{"error": "항목을 찾을 수 없습니다."}`

실제 프로덕션 API는 성공·실패 모두 표준 구조를 씁니다. 아래처럼 통일하고 싶습니다:

```json
// 성공 시
{"success": true, "data": {"id": 1, "title": "우유 사기", "done": false}}

// 실패 시
{"success": false, "error": "항목을 찾을 수 없습니다."}
```

---

### STEP 3-A: 나쁜 프롬프트

```
> API 응답 형식을 통일해줘
```

**응답을 보면서 기록하세요:**

| 관찰 항목 | 내 관찰 결과 |
|-----------|-------------|
| 성공 응답 구조는? | |
| 실패 응답 구조는? | |
| `success` 키를 사용하는가? | |
| `data` 키로 기존 응답을 감쌌는가? | |
| 어느 파일을 수정했나? | |
| 기존 테스트가 통과하는가? | |

```
> /clear
```
```bash
git checkout -- app.py models.py test_app.py
```

---

### STEP 3-B: 좋은 프롬프트

```
> app.py의 모든 응답을 아래 구조로 통일해줘.
>
> 성공 응답 형식:
>   {"success": true, "data": <기존 응답 데이터>}
>
> 실패 응답 형식:
>   {"success": false, "error": "<에러 메시지>"}
>
> 적용 범위:
>   - app.py의 모든 핸들러 함수 수정
>   - models.py는 건드리지 말 것
>   - 204 No Content(DELETE 성공)는 변경 없이 유지
>
> 검증:
>   - test_app.py의 기존 테스트를 새 응답 형식에 맞게 수정
>   - pytest 실행해서 전체 통과 확인
```

**결과 확인:**

```bash
pytest test_app.py -v
```

실제 응답 구조를 확인하려면 **터미널 탭을 하나 더 열어서** 서버를 실행합니다.

```bash
# [새 터미널 탭] — 서버 실행
source .venv/bin/activate
python3 app.py
# 확인 후 Ctrl+C 로 종료
```

```bash
# [기존 터미널 탭] — 응답 구조 확인
curl -X POST http://localhost:4000/todos \
     -H "Content-Type: application/json" \
     -d '{"title": "우유 사기"}' -s | python3 -m json.tool
# {"success": true, "data": {"id": 1, "title": "우유 사기", "done": false}}

curl http://localhost:4000/todos/999 -s | python3 -m json.tool
# {"success": false, "error": "항목을 찾을 수 없습니다."}
```

**두 프롬프트의 차이:**

| 항목 | 나쁜 프롬프트 | 좋은 프롬프트 |
|------|-------------|-------------|
| 성공 응답 최상위 키 | (직접 기록) | `success`, `data` |
| 실패 응답 최상위 키 | (직접 기록) | `success`, `error` |
| 명세와 일치 여부 | (직접 기록) | 일치 |
| 기존 테스트 통과 | (직접 기록) | 전체 통과 |

---

## 전체 관찰 정리

세 라운드를 마치면 아래 표를 완성하세요.

| 라운드 | 나쁜 프롬프트로 에이전트가 임의로 결정한 것 | 좋은 프롬프트가 명시한 것 |
|--------|--------------------------------------|------------------------|
| 1. 대상 불명 | | 파일명 + 함수명 + URL 방식 |
| 2. 범위 폭발 | | "~만 수정, ~는 건드리지 말 것" |
| 3. 형식 불명 | | JSON 구조를 예시로 직접 제시 |

---

## 심화: 나쁜 프롬프트의 연쇄 효과

라운드 1에서 나쁜 프롬프트 결과가 예상과 달랐다면 어떻게 됐을까요?

```
> 검색 기능 추가해줘
Claude: GET /search?q= 엔드포인트를 새로 만듦 (원하지 않았던 방식)

> 아니, 기존 /todos 에 쿼리 파라미터로 해줘
Claude: /todos?q= 방식으로 변경했지만 이전에 만든 /search도 남아 있음

> /search 엔드포인트 지워줘
Claude: 지웠지만 테스트 파일에 /search 테스트가 남아서 실패

> 테스트도 정리해줘
Claude: 테스트를 일부만 정리, 다른 테스트가 깨짐
```

이 4번의 왕복이 좋은 프롬프트 하나로 없어집니다.

> **패턴**: 나쁜 프롬프트 → 예상과 다른 결과 → 수정 요청 → 코드가 점점 복잡해짐 → 더 많은 수정 요청
> **결론**: 처음부터 정확한 프롬프트가 결과적으로 더 빠릅니다.

---

## 스스로 작성해보기 (5분)

아래 요청을 좋은 프롬프트로 바꿔 써보세요.

**나쁜 프롬프트:**
```
> 완료된 항목 필터링 기능 추가해줘
```

**힌트 — 작성 전 결정해야 할 것들:**
- 어느 파일의 어느 함수를 수정하는가?
- URL 파라미터 이름은? (`done`? `completed`? `filter`?)
- 파라미터가 없을 때는 어떻게 동작하는가?
- 파라미터 값은 어떻게 전달하는가? (`?done=true`? `?done=1`?)
- 건드리지 않을 파일은?
- 테스트를 몇 건 추가하는가?

직접 작성한 프롬프트로 Claude에게 요청하고 결과를 확인해보세요.

---

## 🤔 생각해보기

**Q. 라운드 2에서 "오류 처리 추가해줘"로 얻은 결과가 어떤 면에서는 더 나을 수도 있을까? 나쁜 프롬프트의 결과가 항상 나쁜 것은 아닌 이유는?**

**Q. 라운드 3의 좋은 프롬프트처럼 응답 형식을 JSON으로 정확히 명시하는 것이 불편하다고 느껴진다면, 어떤 대안이 있을까? (힌트: CLAUDE.md)**

**Q. 실제 팀 프로젝트에서 API 응답 형식을 에이전트에게 매번 설명하지 않으려면 어떻게 하면 좋을까?**
