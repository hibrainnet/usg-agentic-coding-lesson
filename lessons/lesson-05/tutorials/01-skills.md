# 실습 1: 스킬(Skill) 만들기

## 이번 실습 목표

Claude Code에서 **스킬(Skill)**은 반복 작업을 `/스킬이름`으로 저장해두는 기능입니다.  
4교시에서 완성한 task-manager 프로젝트를 기반으로, 스킬 3개를 만들어봅니다.

> **알아두기**: 이전에 "커스텀 커맨드(Custom Commands)"라고 불리던 기능이 스킬로 통합됐습니다.  
> `.claude/commands/*.md` (레거시) 방식도 계속 동작하지만, 이번 실습에서는 새 방식인 `.claude/skills/` 구조를 사용합니다.

---

## Step 0: 번들 스킬 먼저 체험 (2분)

스킬을 직접 만들기 전에, Claude Code에 내장된 번들 스킬을 먼저 사용해봅니다.

```
/code-review
```

task-manager 파일에 작은 변경이 있다면 자동으로 리뷰가 시작됩니다.  
이처럼 `/스킬이름`으로 고정된 워크플로우를 호출하는 것이 스킬의 핵심입니다.

다른 번들 스킬도 확인해봅니다.

```
/debug
```

---

## Step 1: 스킬 디렉토리 만들기

프로젝트 루트에서 스킬 디렉토리를 만듭니다.

```bash
mkdir -p .claude/skills/task-review
mkdir -p .claude/skills/task-test
mkdir -p .claude/skills/task-commit
```

또는 에이전트에게 요청합니다.

```
"이 프로젝트에 Claude Code 스킬을 저장할 디렉토리 3개를 만들어줘.
경로: .claude/skills/task-review/, .claude/skills/task-test/, .claude/skills/task-commit/"
```

---

## Step 2: task-review 스킬 만들기

`.claude/skills/task-review/SKILL.md` 파일을 만듭니다.

```
"`.claude/skills/task-review/SKILL.md` 파일을 만들어줘.
이 스킬은 task-manager 프로젝트의 코드 변경 사항을 리뷰하는 용도야.

frontmatter 포함:
- description: task-manager 변경 사항에서 버그·엣지 케이스·테스트 누락을 찾는다
- disable-model-invocation: true (사람이 직접 호출하는 용도)

본문에는:
- !`git diff HEAD` 로 현재 diff를 동적 주입
- 리뷰 항목: 버그/논리 오류, 엣지 케이스, 테스트 커버리지, 가독성
- 파일명:줄번호 포함 요청
- 문제 없으면 '리뷰 결과: 문제 없음' 출력"
```

파일이 만들어졌으면 task_manager.py를 수정한 뒤 실행해봅니다.

```
/task-review
```

`!`git diff HEAD`` 부분이 실제 diff로 자동 대체된 것을 확인합니다.

---

## Step 3: task-test 스킬 만들기

pytest를 실행하고 결과를 요약해주는 스킬입니다.

```
"`.claude/skills/task-test/SKILL.md` 파일을 만들어줘.
task-manager의 pytest 테스트를 실행하고 결과를 요약하는 스킬이야.

frontmatter:
- description: task-manager pytest 테스트를 실행하고 결과를 요약한다
- disable-model-invocation: true
- allowed-tools: Bash(python -m pytest *)

본문에는:
- !`cd lessons/lesson-05/examples/task-manager && python -m pytest -v 2>&1` 로 테스트 결과 주입
- 전체/통과/실패 수 요약
- 실패 시 원인과 수정 방법 제안
- 모두 통과 시 '✅ 모든 테스트 통과' 출력"
```

실행해보기:

```
/task-test
```

---

## Step 4: task-commit 스킬 만들기

`disable-model-invocation: true`를 써서 사람만 호출할 수 있는 스킬을 만듭니다.  
커밋처럼 부작용이 있는 작업은 Claude가 자동 실행하면 안 됩니다.

```
"`.claude/skills/task-commit/SKILL.md` 파일을 만들어줘.
staged 변경 사항을 분석해서 커밋 메시지를 제안하는 스킬이야.

frontmatter:
- description: staged 변경 사항을 분석해서 커밋 메시지를 제안한다
- disable-model-invocation: true

본문에는:
- !`git diff --staged` 로 staged diff 주입
- 형식: 타입(feat/fix/refactor/test/docs): 설명 (50자 이내) + 상세 설명
- staged 변경 없으면 'git add 먼저 해주세요.' 안내"
```

task-manager 변경 사항을 스테이징하고 실행해봅니다.

```bash
git add lessons/lesson-05/examples/task-manager/
```

```
/task-commit
```

---

## Step 5: $ARGUMENTS를 활용한 스킬 만들기

인자를 받아서 동작하는 스킬을 만들어봅니다.

```
"`.claude/skills/explain/SKILL.md` 파일을 만들어줘.
$ARGUMENTS로 함수 이름이나 파일 경로를 받아서
초보자도 이해할 수 있게 설명해주는 스킬이야.
함수 역할, 파라미터, 반환값, 사용 예시를 포함하도록 지시해줘."
```

사용해보기:

```
/explain task_manager.py의 complete_task 함수
```

```
/explain task_manager.py의 get_pending_tasks 함수
```

---

## Step 6: examples 폴더의 완성된 예시와 비교

`examples/skills/` 폴더에 미리 작성된 SKILL.md 예시가 있습니다.  
자신이 만든 스킬과 비교해서 개선할 점이 있으면 수정해봅니다.

레거시 방식 예시는 `examples/custom-commands/`에서 확인할 수 있습니다.

---

## 스킬 vs 레거시 커맨드 비교

| | 스킬 (권장) | 레거시 커맨드 |
|--|--|--|
| **경로** | `.claude/skills/<이름>/SKILL.md` | `.claude/commands/<이름>.md` |
| **Frontmatter** | 지원 (제어 옵션 다양) | 부분 지원 |
| **동적 컨텍스트** | `` !`command` `` 지원 | 지원 |
| **지원 파일** | 디렉토리 안에 추가 가능 | 단일 파일만 |
| **자동 로드** | 설명 기반으로 자동 가능 | 직접 호출만 |

---

## 체크리스트

- [ ] `.claude/skills/` 디렉토리를 만들었다
- [ ] `/task-review` 스킬을 만들고 실행했다 (동적 diff 주입 확인)
- [ ] `/task-test` 스킬을 만들고 실행했다
- [ ] `/task-commit` 스킬에 `disable-model-invocation: true`를 적용했다
- [ ] `$ARGUMENTS`를 활용한 스킬을 1개 이상 만들었다
