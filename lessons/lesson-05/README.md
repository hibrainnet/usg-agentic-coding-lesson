# 5교시. 자동화와 확장: 스킬·훅·MCP·서브에이전트

> 4교시에서 task-manager를 기능 구현부터 테스트까지 완성했습니다.  
> 이번 시간에는 **반복 작업을 자동화**하고, 에이전트의 능력을 **외부 도구까지 확장**합니다.  
> 4교시에서 만든 task-manager를 그대로 이어받아, 나만의 워크플로우를 완성합니다.

## ⏱️ 이번 시간(60분) 구성

| 시간 | 내용 | 형태 | 자료 |
|------|------|------|------|
| 0~5분 | 오리엔테이션 + 4교시 복습 | 강의 | — |
| 5~20분 | **스킬(Skill)** — 반복 작업을 나만의 명령어로 (커스텀 커맨드 통합) | 강의 + 따라하기 | [docs/01-skills.md](docs/01-skills.md) · [tutorials/01-skills.md](tutorials/01-skills.md) |
| 20~35분 | **훅(Hooks)** — 특정 이벤트에 자동 실행 | 강의 + 따라하기 | [docs/02-hooks.md](docs/02-hooks.md) · [tutorials/02-hooks.md](tutorials/02-hooks.md) |
| 35~47분 | **MCP 서버** — 외부 도구 연결 | 강의 + 따라하기 | [docs/03-mcp.md](docs/03-mcp.md) · [tutorials/03-mcp.md](tutorials/03-mcp.md) |
| 47~57분 | **서브에이전트** — 작업 위임 패턴 | 강의 + 따라하기 | [docs/04-subagents.md](docs/04-subagents.md) · [tutorials/04-subagents.md](tutorials/04-subagents.md) |
| 57~60분 | Q&A + 다음 시간 예고 | — | — |

## 🎯 학습 목표

- 커스텀 커맨드가 스킬로 통합된 배경과 차이를 설명할 수 있다.
- task-manager 프로젝트에 필요한 스킬을 SKILL.md로 만들고 재사용할 수 있다.
- 훅을 설정해서 파일 저장 직후 테스트가 자동 실행되게 할 수 있다.
- MCP 서버의 개념을 이해하고 공개 MCP 서버 1개를 연결해 활용할 수 있다.
- 서브에이전트로 대규모 탐색 작업을 위임하는 패턴을 경험할 수 있다.

## 📂 자료 안내

### 개념 문서
- [docs/01-skills.md](docs/01-skills.md) — 스킬(Skill) 구조와 작성법, 커스텀 커맨드와의 관계
- [docs/02-hooks.md](docs/02-hooks.md) — 훅 개념과 이벤트 종류
- [docs/03-mcp.md](docs/03-mcp.md) — MCP 개념과 서버 연결 방법
- [docs/04-subagents.md](docs/04-subagents.md) — 서브에이전트 개념과 비교표

### 실습 튜토리얼 (순서대로 진행)
1. [tutorials/01-skills.md](tutorials/01-skills.md) — **스킬 만들기** (15분)
2. [tutorials/02-hooks.md](tutorials/02-hooks.md) — **훅 설정** (15분)
3. [tutorials/03-mcp.md](tutorials/03-mcp.md) — **MCP 서버 연결** (12분)
4. [tutorials/04-subagents.md](tutorials/04-subagents.md) — **서브에이전트** (10분)

### 예제 자료
- `examples/task-manager/` — 4교시 완성본 (5교시 실습 시작 코드)
- `examples/skills/` — 스킬 예시 (SKILL.md, 새 방식)
- `examples/custom-commands/` — 레거시 커맨드 예시 (계속 동작하는 구 방식)
- `examples/hooks-config/` — 훅 설정 예시 (`settings.json`)

## ✅ 이번 시간 산출물(체크리스트)

**스킬**
- [ ] `.claude/skills/` 디렉토리에 SKILL.md 파일을 만들었다
- [ ] `/task-review`에서 `!`git diff`` 동적 주입이 동작하는 것을 확인했다
- [ ] `/task-test`가 pytest를 실행하는 것을 확인했다
- [ ] `disable-model-invocation: true`가 적용된 스킬을 만들었다
- [ ] `$ARGUMENTS`를 활용한 스킬을 만들었다

**훅**
- [ ] `.claude/settings.json`에 훅 설정을 추가했다
- [ ] task_manager.py 수정 후 pytest가 자동 실행되는 것을 확인했다

**MCP**
- [ ] MCP 서버 1개를 Claude Code에 연결했다
- [ ] 에이전트가 MCP를 통해 task-manager 파일에 접근하는 것을 확인했다

**서브에이전트**
- [ ] 서브에이전트로 task-manager 분석을 위임하고 컨텍스트 차이를 확인했다

## 🔜 다음 시간 예고

6교시는 종합 프로젝트입니다. 지금까지 배운 모든 도구(CLAUDE.md, TDD, 스킬, 훅)를 사용해서 처음부터 끝까지 작은 앱을 만들고 회고합니다.
