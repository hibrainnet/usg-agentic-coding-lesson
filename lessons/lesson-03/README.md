# 3교시. Claude Code 제대로 쓰기: 커맨드·프롬프팅·컨텍스트

> 2교시에서 Claude Code를 처음 써봤다면, 이번 시간에는 **더 잘 쓰기 위한 세 가지 도구**를 익힙니다.
> 슬래시 커맨드를 언제 쓰는지 감을 잡고, 요청을 잘 만드는 법을 배우고, CLAUDE.md로 에이전트에게 프로젝트를 기억시킵니다.

## ⏱️ 이번 시간(60분) 구성

| 시간 | 내용 | 형태 | 자료 |
|------|------|------|------|
| 0~5분 | 오리엔테이션 + 2교시 복습 | 강의 | — |
| 5~20분 | **핵심 커맨드 실전** — 상황별로 언제 어떤 커맨드를 쓰는가 | 따라하기 | [tutorials/00-key-commands.md](tutorials/00-key-commands.md) |
| 20~35분 | **효과적인 프롬프팅** — 좋은 요청의 구조와 비교 실습 | 강의 + 따라하기 | [docs/01-effective-prompting.md](docs/01-effective-prompting.md) · [tutorials/01-prompt-comparison.md](tutorials/01-prompt-comparison.md) |
| 35~50분 | **CLAUDE.md 작성** — `/init`으로 생성, 규칙 추가, 효과 확인 | 따라하기 | [tutorials/02-create-claude-md.md](tutorials/02-create-claude-md.md) |
| 50~57분 | **계획 모드** — `/plan`으로 복잡한 작업 사전 설계 | 따라하기 | [tutorials/03-plan-mode.md](tutorials/03-plan-mode.md) |
| 57~60분 | Q&A + 다음 시간 예고 | — | — |

> 커맨드 실전(5~20분)은 2교시에서 참고만 한 `/compact`, `/code-review`, `/model`, `/rewind` 등을 맥락 안에서 처음 실습하는 시간입니다.

## 🎯 학습 목표

- 상황에 따라 올바른 슬래시 커맨드를 선택하고 사용할 수 있다.
- 모호한 요청과 좋은 요청의 차이를 설명하고, 5요소를 활용해 프롬프트를 작성할 수 있다.
- `/init`으로 CLAUDE.md를 만들고 프로젝트 규칙을 추가해서 에이전트 응답이 달라지는 것을 확인할 수 있다.
- `/plan`으로 복잡한 작업을 사전에 설계하고 방향을 조정한 뒤 실행할 수 있다.

## 📂 자료 안내

### 개념 문서
- [docs/01-effective-prompting.md](docs/01-effective-prompting.md) — 좋은 프롬프트의 5가지 구성 요소
- [docs/02-context-management.md](docs/02-context-management.md) — CLAUDE.md, `/compact`, 계획 모드

### 실습 튜토리얼 (순서대로 진행)
1. [tutorials/00-key-commands.md](tutorials/00-key-commands.md) — **핵심 커맨드 실전** (시나리오 5개로 /usage·/compact·/model·/code-review·/rewind 체험)
2. [tutorials/01-prompt-comparison.md](tutorials/01-prompt-comparison.md) — **나쁜 vs 좋은 프롬프트 비교** (contact-book, 15분)
3. [tutorials/01b-prompt-comparison-advanced.md](tutorials/01b-prompt-comparison-advanced.md) — **프롬프트 비교 심화** (grade-manager, 실패 유형 3가지 직접 재현, 25분)
4. [tutorials/02-create-claude-md.md](tutorials/02-create-claude-md.md) — **CLAUDE.md 작성** (/init → 규칙 추가 → 효과 확인)
5. [tutorials/03-plan-mode.md](tutorials/03-plan-mode.md) — **계획 모드** (/plan으로 복잡한 기능 사전 설계)

> 시간이 충분하면 01 → 01b 순서로, 시간이 부족하면 01b만 진행합니다. 01b가 더 극적인 차이를 보여줍니다.

### 예제 자료
- `examples/contact-book/` — 기본 비교 실습용 (`01-prompt-comparison.md`)
- `examples/todo-api/` — **심화 비교 실습용** (`01b-prompt-comparison-advanced.md`) — Flask REST API, 3파일 구조, 실패 유형 3가지 재현
- `examples/prompt-cheatsheet.md` — **프롬프트 작성 참고 카드** (인쇄용)
- `examples/sample-CLAUDE.md` — 잘 작성된 CLAUDE.md 예시

## ✅ 이번 시간 산출물(체크리스트)

**슬래시 커맨드 실전**
- [ ] `/usage`와 `/context`로 세션 현황을 확인했다
- [ ] `/compact` 전후 토큰 변화를 비교했다
- [ ] `/code-review`로 코드를 리뷰해봤다
- [ ] `/rewind`로 이전 상태로 되돌아가는 것을 확인했다

**프롬프팅**
- [ ] 나쁜 프롬프트와 좋은 프롬프트의 결과 차이를 직접 확인했다
- [ ] 5요소를 활용해 스스로 프롬프트를 작성했다

**CLAUDE.md**
- [ ] `/init`으로 CLAUDE.md를 생성했다
- [ ] 코딩 규칙 섹션을 직접 추가했다
- [ ] CLAUDE.md 있을 때와 없을 때 결과 차이를 확인했다

**계획 모드**
- [ ] `/plan`으로 복잡한 작업의 계획을 먼저 확인했다
- [ ] 계획 일부를 수정 요청한 뒤 실행했다

## 🔜 다음 시간 예고

4교시에서는 실제 기능 구현부터 디버깅·테스트·Git 커밋까지, 전체 개발 사이클을 에이전트와 함께 경험합니다. 이번 시간에 만든 CLAUDE.md를 그대로 사용합니다.
