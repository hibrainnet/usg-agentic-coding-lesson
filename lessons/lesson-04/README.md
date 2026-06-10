# 4교시. 실전 개발: 기능 구현부터 디버깅·테스트·Git까지

> 3교시에서 CLAUDE.md와 프롬프팅을 익혔다면, 이번 시간에는 **실제 개발 사이클** 전체를 에이전트와 함께 경험합니다.
> 요구사항 → 구현 → 테스트 → 디버깅 → 커밋까지, 현업에서 쓰는 워크플로우를 그대로 따라합니다.

## ⏱️ 이번 시간 구성

| 시간 | 내용 | 형태 | 자료 |
|------|------|------|------|
| 0~5분 | 오리엔테이션 + 3교시 복습 | 강의 | — |
| 5~20분 | **TDD 스타일 기능 구현** — 요구사항 → 테스트 → 구현 순서로 | 강의 + 따라하기 | [docs/01-tdd-with-agent.md](docs/01-tdd-with-agent.md) · [tutorials/01-feature-implementation.md](tutorials/01-feature-implementation.md) |
| 20~40분 | **에러 기반 디버깅** — 스택트레이스를 에이전트에게 넘기기 | 강의 + 따라하기 | [docs/02-debugging-loop.md](docs/02-debugging-loop.md) · [tutorials/02-debugging-practice.md](tutorials/02-debugging-practice.md) |
| 40~55분 | **Git 연동** — 커밋 메시지 작성, (선택) PR 생성 | 따라하기 | [tutorials/03-git-workflow.md](tutorials/03-git-workflow.md) |
| 55~60분 | Q&A + 다음 시간 예고 | — | — |

## 🎯 학습 목표

- 작은 기능을 요구사항 → 테스트 → 구현 순서로 에이전트와 함께 완성할 수 있다.
- 에러 메시지와 스택트레이스를 에이전트에게 효과적으로 전달해 버그를 찾고 수정할 수 있다.
- 변경 사항을 Git으로 커밋하고 의미 있는 커밋 메시지를 작성할 수 있다.

## 📂 자료 안내

### 개념 문서
- [docs/01-tdd-with-agent.md](docs/01-tdd-with-agent.md) — TDD 스타일 에이전트 협업 패턴
- [docs/02-debugging-loop.md](docs/02-debugging-loop.md) — 에러 기반 디버깅 루프

### 실습 튜토리얼 (순서대로 진행)
1. [tutorials/01-feature-implementation.md](tutorials/01-feature-implementation.md) — **기능 구현** (요구사항 → 테스트 작성 → 구현)
2. [tutorials/02-debugging-practice.md](tutorials/02-debugging-practice.md) — **버그 찾기와 수정** (에러 로그 기반 디버깅)
3. [tutorials/03-git-workflow.md](tutorials/03-git-workflow.md) — **Git 커밋과 PR** (변경 사항 커밋)

### 예제 자료
- `examples/task-manager/` — 실습용 태스크 관리 앱 (버그 포함, 구현할 기능 포함)

## ✅ 이번 시간 산출물(체크리스트)

**기능 구현**
- [ ] 요구사항을 먼저 에이전트와 정리했다
- [ ] 테스트를 먼저 작성하고 구현을 요청했다
- [ ] 새 기능이 기존 테스트를 깨지 않는 것을 확인했다

**디버깅**
- [ ] 에러 메시지를 그대로 에이전트에게 붙여넣어 원인을 파악했다
- [ ] 버그를 수정하고 수정 이유를 이해했다
- [ ] 수정 후 테스트가 통과하는 것을 확인했다

**Git**
- [ ] `git diff`로 변경 사항을 에이전트와 함께 리뷰했다
- [ ] 의미 있는 커밋 메시지를 작성해 커밋했다
- [ ] (선택) PR을 생성하고 설명을 작성했다

## 🔜 다음 시간 예고

5교시에서는 반복 작업을 자동화합니다. 커스텀 슬래시 커맨드, 훅(Hooks), MCP 서버 연결을 통해 개발 흐름을 더 빠르게 만듭니다.
