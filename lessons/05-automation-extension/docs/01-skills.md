# 스킬(Skill): 나만의 명령어 만들기

## 스킬이란?

Claude Code에서 **스킬(Skill)**은 반복적으로 사용하는 지시나 절차를 `SKILL.md` 파일로 저장해두고, `/스킬이름`으로 언제든 호출하는 기능입니다.

> **커스텀 커맨드(Custom Commands)는 스킬로 통합됐습니다.**  
> `.claude/commands/deploy.md`와 `.claude/skills/deploy/SKILL.md`는 동일하게 `/deploy`를 만들고 같은 방식으로 동작합니다.  
> 기존 `.claude/commands/` 파일은 계속 동작하지만, 스킬 방식을 권장합니다.  
> 스킬은 지원 파일 디렉토리, frontmatter 제어, 자동 로드 등 추가 기능을 제공합니다.

---

## 스킬의 세 가지 종류

| 종류 | 설명 | 예시 |
|------|------|------|
| **번들 스킬** | Claude Code가 기본 제공하는 고급 워크플로우 | `/code-review`, `/debug`, `/run` |
| **나만의 스킬** | 직접 만드는 프로젝트/개인 스킬 | `/task-review`, `/task-test` |
| **레거시 커맨드** | 통합 이전 방식, 계속 동작 | `.claude/commands/*.md` |

### 번들 스킬 목록

| 스킬 | 용도 |
|------|------|
| `/code-review` | 변경 사항 코드 리뷰 |
| `/debug` | 버그 진단 및 수정 |
| `/run` | 앱 실행 및 동작 확인 |
| `/verify` | 코드 변경이 실제로 동작하는지 확인 |
| `/loop` | 반복 작업 자동화 |
| `/security-review` | 보안 취약점 검토 |

---

## 파일 위치와 구조

### 저장 위치

| 위치 | 경로 | 적용 범위 |
|------|------|-----------|
| 개인 스킬 | `~/.claude/skills/<스킬이름>/SKILL.md` | 모든 프로젝트 |
| 프로젝트 스킬 | `.claude/skills/<스킬이름>/SKILL.md` | 이 프로젝트만 |
| 레거시 커맨드 | `.claude/commands/<이름>.md` | 이 프로젝트만 (계속 동작) |

디렉토리 이름이 커맨드 이름이 됩니다.  
`.claude/skills/task-review/SKILL.md` → `/task-review`

### SKILL.md 기본 구조

```markdown
---
description: 이 스킬이 무엇을 하는지 설명 (Claude가 자동 로드 여부 판단에 사용)
disable-model-invocation: false  # true면 사람만 직접 호출 가능
---

스킬 실행 시 Claude에게 전달되는 지시 내용
```

### 스킬 디렉토리 구조 (지원 파일 포함)

```
.claude/skills/task-review/
├── SKILL.md          # 핵심 지시 (필수)
├── checklist.md      # 리뷰 체크리스트 (선택)
└── examples/
    └── good-code.md  # 참고 예시 (선택)
```

---

## Frontmatter 주요 옵션

```yaml
---
description: 이 스킬의 역할과 사용 시점
disable-model-invocation: true   # true = 사람만 호출, Claude 자동 로드 방지
user-invocable: false            # false = Claude만 자동 로드, 메뉴에서 숨김
allowed-tools: Bash(pytest *)    # 이 스킬 실행 중 승인 없이 허용할 도구
context: fork                    # fork = 서브에이전트에서 독립 실행
argument-hint: "[task-id]"       # 자동완성 힌트
---
```

| 옵션 | 사용 상황 |
|------|-----------|
| `disable-model-invocation: true` | `/commit`, `/deploy` 처럼 Claude가 자동으로 실행하면 안 되는 작업 |
| `user-invocable: false` | 배경 지식을 주입하는 스킬, 메뉴에서 보이지 않아도 됨 |
| `allowed-tools` | 스킬 실행 중 특정 도구를 매번 승인 없이 허용 |
| `context: fork` | 긴 탐색/분석을 서브에이전트에서 독립 실행 |

---

## 동적 컨텍스트 주입

`` !`command` `` 문법을 사용하면 Claude가 스킬을 읽기 전에 쉘 명령어를 실행하고 결과를 주입합니다.

```markdown
---
description: task-manager 변경 사항을 요약하고 위험 요소를 찾는다
---

## 현재 변경 사항

!`git diff HEAD`

## 지시

위 변경 사항을 2~3 bullet로 요약하고, 누락된 에러 처리, 하드코딩된 값, 업데이트가 필요한 테스트가 있으면 위험 요소로 표시해줘.
```

스킬 실행 시 `git diff HEAD` 결과가 즉시 삽입되어 Claude는 실제 diff를 보게 됩니다.

---

## 인자(Arguments) 활용

```markdown
$ARGUMENTS 함수를 초보자도 이해할 수 있게 설명해줘.
```

```
/explain task_manager.py의 complete_task 함수
```

`$ARGUMENTS`에 `task_manager.py의 complete_task 함수`가 들어갑니다.

위치 기반 인자도 지원합니다.

```markdown
$0 컴포넌트를 $1에서 $2로 마이그레이션해줘.
```

```
/migrate SearchBar React Vue
```

---

## task-manager 스킬 예시

### task-review — 코드 리뷰

`.claude/skills/task-review/SKILL.md`:

```markdown
---
description: task-manager 변경 사항에서 버그·엣지 케이스·테스트 누락을 찾는다. 코드 변경 후 리뷰가 필요할 때 사용.
disable-model-invocation: true
---

## 변경 사항

!`git diff HEAD`

## 리뷰 항목

1. **버그 & 논리 오류** — task id 할당, 상태 전환 로직
2. **엣지 케이스 누락** — 빈 제목, 존재하지 않는 ID
3. **테스트 커버리지** — 새 로직에 테스트가 있는지
4. **코드 가독성**

파일명:줄번호와 함께 알려줘. 문제가 없으면 "리뷰 결과: 문제 없음"이라고 알려줘.
```

### task-test — 테스트 실행

`.claude/skills/task-test/SKILL.md`:

```markdown
---
description: task-manager pytest 테스트를 실행하고 결과를 요약한다
disable-model-invocation: true
allowed-tools: Bash(python -m pytest *)
---

다음 명령어를 실행하고 결과를 요약해줘:

!`cd lessons/05-automation-extension/examples/task-manager && python -m pytest -v 2>&1`

- 전체 / 통과 / 실패 수
- 실패 테스트가 있으면 원인과 수정 방법 제안
- 모두 통과하면 "✅ 모든 테스트 통과"
```

### task-commit — 커밋 메시지 생성

`.claude/skills/task-commit/SKILL.md`:

```markdown
---
description: staged 변경 사항을 분석해서 커밋 메시지를 제안한다
disable-model-invocation: true
---

## Staged 변경 사항

!`git diff --staged`

위 변경 사항에 맞는 Git 커밋 메시지를 작성해줘.

형식: `타입: 설명 (50자 이내)`
타입: feat / fix / refactor / test / docs

staged 변경이 없으면 "`git add` 먼저 해주세요."라고 안내해줘.
```

---

## 레거시 방식 (`.claude/commands/`)

기존 `.claude/commands/deploy.md` 형식도 계속 동작합니다.  
단, skills가 같은 이름의 command보다 우선합니다.  
새 기능(지원 파일, frontmatter 제어)이 필요 없다면 기존 방식도 충분합니다.

```markdown
<!-- .claude/commands/task-review.md (레거시) -->
---
description: task-manager 코드 리뷰
---

git diff를 분석해서 코드 리뷰를 해줘.
```

---

## 핵심 정리

```
✅ 스킬 = SKILL.md 파일 하나 + 선택적 지원 파일
✅ 디렉토리 이름 = 커맨드 이름
✅ frontmatter로 자동 로드 / 수동 호출 여부 제어
✅ !`command`로 실행 시점에 동적 컨텍스트 주입
✅ $ARGUMENTS로 인자 처리
✅ .claude/commands/ 레거시도 계속 동작
```
