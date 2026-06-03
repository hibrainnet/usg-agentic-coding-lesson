# 실습 1: 나만의 슬래시 커맨드 만들기 (15분)

## 준비

이번 실습에서는 자주 쓰는 작업 2가지를 커스텀 커맨드로 만들어봅니다.
- `/review` — 코드 리뷰 요청
- `/commit` — 커밋 메시지 생성

---

## Step 1: 커맨드 디렉토리 만들기

프로젝트 루트에서 커맨드 디렉토리를 만듭니다.

```bash
mkdir -p .claude/commands
```

또는 에이전트에게 요청합니다.

```
"프로젝트에 커스텀 Claude Code 슬래시 커맨드를 저장할 디렉토리를 만들어줘.
경로는 .claude/commands/ 이야."
```

---

## Step 2: 코드 리뷰 커맨드 만들기

`.claude/commands/review.md` 파일을 만듭니다.

```
"`.claude/commands/review.md` 파일을 만들어줘.
이 커맨드는 git diff를 분석해서 코드 리뷰를 요청하는 용도야.
다음 내용을 포함해줘:
1. 버그나 논리 오류 확인
2. 엣지 케이스 누락 확인  
3. 코드 가독성 확인
각 항목은 파일명과 줄 번호를 포함해달라고 지시해줘."
```

파일이 만들어졌으면 Claude Code에서 `/review`를 입력해서 동작하는지 확인합니다.

---

## Step 3: 커밋 메시지 생성 커맨드 만들기

`.claude/commands/commit.md` 파일을 만듭니다.

```
"`.claude/commands/commit.md` 파일을 만들어줘.
staged된 변경 사항을 분석해서 커밋 메시지를 제안하는 커맨드야.
형식: 타입(feat/fix/refactor/test/docs): 설명 (50자 이내)
그 아래 상세 설명도 포함하도록 지시해줘."
```

이전 실습에서 수정한 task-manager 파일이 있다면 스테이징하고 `/commit`을 실행해봅니다.

```bash
git add lessons/04-real-development/examples/task-manager/
```

그다음 Claude Code에서:
```
/commit
```

---

## Step 4: 인자를 받는 커맨드 만들기

`$ARGUMENTS`를 활용해서 함수 설명 커맨드를 만들어봅니다.

`.claude/commands/explain.md`:

```
"`.claude/commands/explain.md` 파일을 만들어줘.
$ARGUMENTS로 함수 이름이나 파일 경로를 받아서
초보자도 이해할 수 있게 설명해주는 커맨드야.
함수 역할, 파라미터, 반환값, 사용 예시를 포함하도록 지시해줘."
```

사용해보기:
```
/explain task_manager.py의 add_task 함수
```

---

## Step 5: examples 폴더의 완성된 예시와 비교

`examples/custom-commands/` 폴더에 미리 작성된 예시가 있습니다.  
자신이 만든 커맨드와 비교해서 개선할 점이 있으면 수정해봅니다.

---

## 체크리스트

- [ ] `.claude/commands/` 디렉토리를 만들었다
- [ ] `/review` 커맨드를 만들고 실행했다
- [ ] `/commit` 커맨드를 만들고 실행했다
- [ ] `$ARGUMENTS`를 활용한 커맨드를 1개 이상 만들었다
- [ ] 커맨드 파일을 수정해서 원하는 형태로 다듬었다
