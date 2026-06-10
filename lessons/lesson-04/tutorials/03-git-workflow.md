# 실습 3: Git 커밋과 PR

## 준비

1, 2번 실습에서 버그를 수정하고 새 기능을 추가했습니다.  
이제 변경 사항을 Git으로 기록합니다.

> 이 실습은 프로젝트 루트 디렉토리에서 진행합니다.

---

## Step 1: 변경 사항 확인하기

어떤 파일이 변경됐는지 확인합니다.

```bash
git status
```

변경된 파일이 보이면, 구체적인 변경 내용을 확인합니다.

```bash
git diff
```

출력이 길면 에이전트에게 요약을 요청합니다.

```
git diff 결과:
[git diff 출력 붙여넣기]

이 변경 사항을 간략하게 요약해줘.
어떤 버그를 수정했고 어떤 기능이 추가됐는지 알려줘.
```

---

## Step 2: 변경 사항 스테이징

커밋할 파일을 스테이징합니다.

```bash
git add lessons/lesson-04/examples/task-manager/task_manager.py
git add lessons/lesson-04/examples/task-manager/test_task_manager.py
```

---

## Step 3: 커밋 메시지 작성하기

좋은 커밋 메시지는 **왜** 변경했는지를 설명합니다.  
에이전트에게 커밋 메시지 작성을 도와달라고 요청합니다.

```
방금 한 변경 사항을 바탕으로 Git 커밋 메시지를 작성해줘.

변경 내용:
1. 빈 제목 태스크 추가 방지 검증 추가 (ValueError 발생)
2. 존재하지 않는 ID 삭제 시 False 반환
3. complete_task 기능 추가 (테스트 포함)

커밋 메시지 형식: 제목(50자 이내) + 빈 줄 + 상세 설명
```

에이전트가 제안한 메시지를 검토하고 필요하면 수정합니다.

### 좋은 커밋 메시지 예시

```
fix: task-manager 버그 수정 및 complete_task 기능 추가

- 빈 제목 태스크 추가 방지를 위한 ValueError 검증 추가 (#1)
- 존재하지 않는 ID 삭제 시 False 반환 (#2)
- complete_task(task_id) 함수 구현 및 테스트 추가
```

---

## Step 4: 커밋하기

```bash
git commit -m "fix: task-manager 버그 수정 및 complete_task 기능 추가"
```

또는 에이전트에게 커밋 자체를 요청합니다.

```
"스테이징된 파일을 커밋해줘. 커밋 메시지는 방금 작성한 것을 사용해줘."
```

---

## Step 5: (선택) PR 생성하기

GitHub에 push하고 PR을 생성합니다.

```
"현재 브랜치를 origin에 push하고
GitHub PR을 생성해줘.

PR 제목: fix: task-manager 버그 수정 및 complete_task 기능 추가
PR 설명에는 수정된 버그 3개와 추가된 기능을 포함해줘."
```

---

## 커밋 메시지 작성 팁

| 타입 | 의미 | 예시 |
|------|------|------|
| `feat` | 새 기능 추가 | `feat: 태스크 검색 기능 추가` |
| `fix` | 버그 수정 | `fix: 빈 목록 IndexError 수정` |
| `test` | 테스트 추가/수정 | `test: complete_task 테스트 추가` |
| `refactor` | 기능 변경 없는 코드 개선 | `refactor: add_task 함수 정리` |
| `docs` | 문서 수정 | `docs: README 업데이트` |

---

## 체크리스트

- [ ] `git diff`로 변경 내용을 확인하고 에이전트에게 요약받았다
- [ ] 관련 파일을 스테이징했다
- [ ] 의미 있는 커밋 메시지를 작성해서 커밋했다
- [ ] `git log`로 커밋이 기록된 것을 확인했다
- [ ] (선택) GitHub에 push하고 PR을 생성했다
