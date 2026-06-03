# 커스텀 슬래시 커맨드

## 커스텀 커맨드란?

Claude Code에 기본 내장된 `/help`, `/clear` 같은 슬래시 커맨드처럼,
**자주 반복하는 작업을 나만의 커맨드로 저장**해두는 기능입니다.

한 번 만들어두면 언제든 `/review`, `/commit` 처럼 짧게 호출할 수 있습니다.

---

## 파일 위치와 구조

커스텀 커맨드는 마크다운(`.md`) 파일로 작성합니다.

### 저장 위치

| 위치 | 적용 범위 |
|------|-----------|
| `~/.claude/commands/커맨드이름.md` | 모든 프로젝트에서 사용 가능 (글로벌) |
| `{프로젝트}/.claude/commands/커맨드이름.md` | 해당 프로젝트에서만 사용 가능 (로컬) |

파일명이 커맨드 이름이 됩니다.  
`review.md` → `/review`, `commit-msg.md` → `/commit-msg`

### 파일 구조

```markdown
---
description: 이 커맨드가 무슨 일을 하는지 한 줄 설명 (선택)
---

커맨드 실행 시 에이전트에게 전달할 지시 내용
```

---

## 기본 예시: 코드 리뷰 커맨드

`.claude/commands/review.md`:

```markdown
---
description: 현재 변경 사항에서 버그와 개선점을 찾아 보고한다
---

git diff를 분석해서 코드 리뷰를 해줘.

다음 항목을 확인해줘:
1. 버그나 논리 오류
2. 엣지 케이스 누락
3. 코드 가독성

각 항목은 파일명과 줄 번호를 포함해서 알려줘.
```

이 파일을 만들면 `/review`를 입력할 때마다 위 지시가 에이전트에게 전달됩니다.

---

## 인자(Arguments) 활용

`$ARGUMENTS` 변수를 쓰면 커맨드 호출 시 추가 입력을 받을 수 있습니다.

`.claude/commands/explain.md`:

```markdown
$ARGUMENTS 코드를 초보자도 이해할 수 있게 설명해줘.
함수의 역할, 파라미터, 반환값을 포함해서 설명해줘.
```

사용법:
```
/explain task_manager.py의 add_task 함수
```

`$ARGUMENTS`에는 `task_manager.py의 add_task 함수`가 들어갑니다.

---

## 실용적인 커맨드 예시

### 커밋 메시지 생성

`.claude/commands/commit.md`:

```markdown
현재 staged된 변경 사항을 분석해서 Git 커밋 메시지를 작성해줘.

형식:
- 첫 줄: `타입: 짧은 설명` (50자 이내)
- 빈 줄
- 상세 설명 (변경 이유 중심)

타입: feat(새 기능), fix(버그), refactor(리팩토링), test(테스트), docs(문서)
```

### 테스트 작성 요청

`.claude/commands/write-tests.md`:

```markdown
$ARGUMENTS 함수에 대한 pytest 테스트를 작성해줘.

포함할 케이스:
- 정상 동작 (happy path)
- 엣지 케이스 (빈 입력, 경계값)
- 에러 케이스 (잘못된 입력)

테스트 함수명은 `test_함수명_상황` 형식으로 작성해줘.
```

---

## 커맨드 관리 팁

- 커맨드 파일을 수정하면 바로 반영됩니다 (Claude Code 재시작 불필요)
- 프로젝트마다 다른 규칙이 필요하면 로컬(`.claude/commands/`) 커맨드를 사용
- 팀 전체에서 쓸 커맨드는 프로젝트 루트 `.claude/commands/`에 두고 Git에 커밋

---

## 핵심 정리

```
✅ 파일명 = 커맨드 이름 (확장자 제외)
✅ 마크다운 파일 안이 에이전트에게 전달되는 지시
✅ $ARGUMENTS로 동적 입력 처리
✅ 글로벌(~/.claude) vs 로컬(.claude) 위치 선택
```
