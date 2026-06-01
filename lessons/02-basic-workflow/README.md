# 2교시. 개발 환경 설정과 기본 워크플로우

> 1교시에서 이해한 개념을 직접 손으로 체험합니다. 먼저 개발 환경을 갖추고, 첫 번째 실전 워크플로우를 경험합니다.

## ⏱️ 이번 시간(60분) 구성

| 시간 | 내용 | 형태 | 자료 |
|------|------|------|------|
| 0~5분 | 오리엔테이션 + 1교시 핵심 복습 | 강의 | — |
| 5~35분 | **환경 설정 실습** (OS별 트랙) | 따라하기 | `tutorials/01-macos-setup.md` / `02-windows-setup.md` |
| 35~55분 | **첫 번째 워크플로우** (샘플 프로젝트 탐색·수정) | 따라하기 | `tutorials/03-first-workflow.md` |
| 55~60분 | Q&A + 다음 시간 예고 | — | — |

> macOS와 Windows가 섞여 있을 경우, 각자 자신의 OS 튜토리얼을 따라가면 됩니다.

## 🎯 학습 목표

- macOS 또는 Windows 환경에 개발 도구 전체를 설치하고 동작을 확인할 수 있다.
- Claude Code를 실행하고 인증을 완료할 수 있다.
- 기존 코드베이스를 Claude Code로 탐색하고 구조를 이해할 수 있다.
- 자연어 요청으로 버그를 찾아 수정하고 변경 사항을 확인할 수 있다.

## 📂 자료 안내

- `docs/01-environment-setup.md` — 설치 개요: 무엇을 왜 설치하는가
- `docs/02-basic-workflow.md` — 기본 워크플로우 개념: 탐색·질문·수정·검증
- `docs/03-slash-commands.md` — **슬래시 커맨드 & CLI 전체 레퍼런스** (강의 후에도 계속 참고)
- `tutorials/01-macos-setup.md` — **macOS 환경 설정 따라하기** (Ghostty · Homebrew · Git · Python3 · VSCode · Claude Code)
- `tutorials/02-windows-setup.md` — **Windows 환경 설정 따라하기** (Windows Terminal · Git · Python3 · VSCode · Claude Code)
- `tutorials/03-first-workflow.md` — **첫 번째 워크플로우** (To-Do CLI 탐색·수정)
- `examples/todo-cli/` — 실습용 샘플 프로젝트

## ✅ 이번 시간 산출물(체크리스트)

**환경 설정**
- [ ] 터미널 실행 가능
- [ ] `git --version` 정상 출력
- [ ] `python3 --version` 정상 출력
- [ ] `code --version` 정상 출력
- [ ] `claude --version` 정상 출력
- [ ] `claude` 실행 및 인증 성공

**기본 워크플로우**
- [ ] 샘플 프로젝트(todo-cli)에 대한 코드 구조 설명 받기
- [ ] 버그 1건을 Claude Code로 찾아 수정
- [ ] `/help`, `/clear` 슬래시 커맨드 사용 경험

## 🔜 다음 시간 예고

3교시에서는 더 나은 프롬프트를 작성하는 법과 `CLAUDE.md`로 프로젝트 컨텍스트를 주입하는 방법을 배웁니다.
