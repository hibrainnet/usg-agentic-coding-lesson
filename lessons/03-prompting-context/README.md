# 3교시. 효과적인 프롬프팅과 컨텍스트 관리

> 2교시에서 Claude Code의 동작 방식을 체험했다면, 이번 시간에는 **에이전트를 더 잘 다루는 법**을 익힙니다.
> 같은 도구라도 어떻게 요청하느냐에 따라 결과가 극적으로 달라집니다.

## ⏱️ 이번 시간(60분) 구성

| 시간 | 내용 | 형태 | 자료 |
|------|------|------|------|
| 0~5분 | 오리엔테이션 + 2교시 복습 | 강의 | — |
| 5~20분 | 좋은 프롬프트의 구조와 원칙 | 강의 | `docs/01-effective-prompting.md` |
| 20~35분 | 나쁜 vs 좋은 프롬프트 비교 실습 | 따라하기 | `tutorials/01-prompt-comparison.md` |
| 35~50분 | CLAUDE.md 작성 + 계획 모드 | 따라하기 | `tutorials/02-create-claude-md.md` · `03-plan-mode.md` |
| 50~60분 | Q&A + 다음 시간 예고 | — | — |

## 🎯 학습 목표

- 모호한 요청과 좋은 요청의 차이를 구체적으로 설명하고, 효과적인 프롬프트를 작성할 수 있다.
- CLAUDE.md로 프로젝트 규칙·관례를 에이전트에게 전달하고, 결과가 달라지는 것을 확인할 수 있다.
- 계획 모드로 큰 작업을 사전에 설계하고 검토한 뒤 실행할 수 있다.

## 📂 자료 안내

- `docs/01-effective-prompting.md` — 좋은 프롬프트의 5가지 구성 요소
- `docs/02-context-management.md` — CLAUDE.md, 컨텍스트 관리, 계획 모드
- `tutorials/01-prompt-comparison.md` — 나쁜 vs 좋은 프롬프트 비교 실습
- `tutorials/02-create-claude-md.md` — CLAUDE.md 작성 실습
- `tutorials/03-plan-mode.md` — 계획 모드 실습
- `examples/contact-book/` — 실습용 샘플 프로젝트 (주소록 CLI)
- `examples/prompt-cheatsheet.md` — **프롬프트 작성 참고 카드** (강의 후에도 계속 쓸 수 있는 요약본)
- `examples/sample-CLAUDE.md` — 잘 작성된 CLAUDE.md 예시

## ✅ 이번 시간 산출물(체크리스트)

- [ ] 나쁜 프롬프트와 좋은 프롬프트의 결과 차이를 직접 확인했다
- [ ] 프롬프트 5가지 구성 요소를 활용해 직접 프롬프트를 작성했다
- [ ] `/init`으로 CLAUDE.md를 생성하고 프로젝트 규칙을 추가했다
- [ ] CLAUDE.md 있을 때와 없을 때 결과를 비교했다
- [ ] 계획 모드로 복잡한 작업을 사전 설계한 뒤 실행했다

## 🔜 다음 시간 예고

4교시에서는 실제 기능 구현부터 디버깅·테스트·Git 커밋까지, 전체 개발 사이클을 에이전트와 함께 경험합니다.
