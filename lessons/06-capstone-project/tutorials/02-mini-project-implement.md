# 실습 2: 구현·테스트·문서화 (35분)

## 파트 A: 기능 구현 (20분)

### Step 1: 첫 기능 — add_note (TDD)

테스트 먼저 확인하고 구현합니다.

```
"test_note_app.py에서 add_note 관련 테스트를 보여줘.
그 테스트들을 통과하는 add_note 함수를 구현해줘.
구현 후 pytest를 실행해서 확인해줘."
```

테스트가 통과하면 다음 기능으로 넘어갑니다.

---

### Step 2: get_notes, get_note 구현

```
"get_notes와 get_note 함수를 구현해줘.
get_note는 없는 id를 받으면 None을 반환해야 해.
구현 후 관련 테스트가 통과하는지 확인해줘."
```

---

### Step 3: delete_note 구현

```
"delete_note 함수를 구현해줘.
없는 id를 삭제 시도하면 False를 반환해야 해.
성공하면 True를 반환해줘.
구현 후 pytest로 확인해줘."
```

---

### Step 4: search_notes 구현 (심화)

```
"search_notes(keyword) 함수를 구현해줘.
title과 content 모두에서 검색해야 해.
대소문자를 구분하지 않아야 해.
TDD 방식으로 테스트 먼저 작성하고 구현해줘."
```

---

### Step 5: 전체 테스트 통과 확인

```bash
pytest test_note_app.py -v
```

모든 테스트가 통과하면 파트 A 완료입니다.

---

## 파트 B: 직접 실행해서 검증 (5분)

테스트가 통과해도 실제 실행을 확인합니다.

```bash
python note_app.py
```

다음 시나리오를 직접 테스트합니다.

```
1. 메모 추가 → "오늘 배운 것: TDD" 입력
2. 전체 목록 확인
3. 키워드 "TDD"로 검색
4. 메모 삭제
5. 존재하지 않는 ID로 삭제 시도
```

문제가 있으면 에이전트에게 에러 메시지를 전달해서 수정합니다.

---

## 파트 C: README 작성 (5분)

```
"note-cli 프로젝트의 README.md를 작성해줘.
다음 내용을 포함해줘:
- 프로젝트 소개 (1~2줄)
- 설치 방법 (pip install -r requirements.txt)
- 실행 방법 (python note_app.py)
- 주요 기능 목록
- 테스트 실행 방법"
```

---

## 파트 D: 커밋 (5분)

변경 사항을 Git으로 저장합니다.

```bash
git add lessons/06-capstone-project/examples/note-cli/
```

```
"/commit 커맨드로 커밋 메시지를 작성해줘."
```

커밋 메시지를 확인하고 커밋합니다.

```bash
git commit -m "커밋 메시지"
```

---

## (선택) 추가 기능

시간이 남으면 아래 기능 중 하나를 추가해봅니다.

**태그 기능**
```
"메모에 태그를 추가하는 기능을 구현해줘.
add_note(title, content, tags=[]) 형식으로 변경하고
태그로 검색하는 filter_by_tag(tag) 함수도 추가해줘.
TDD 방식으로 진행해줘."
```

**메모 수정 기능**
```
"기존 메모의 내용을 수정하는 update_note(note_id, title=None, content=None) 함수를 추가해줘.
제공된 파라미터만 업데이트해야 해.
테스트도 함께 작성해줘."
```

---

## 체크리스트

- [ ] 모든 핵심 함수(add, get, delete, search)를 구현했다
- [ ] pytest 전체 테스트가 통과한다
- [ ] 직접 실행해서 주요 기능을 확인했다
- [ ] README.md를 작성했다
- [ ] Git으로 커밋했다
