# 개발 환경 구성 개요

## 왜 이 도구들이 필요한가

Claude Code를 실제로 활용하려면 Claude Code 단독 설치만으로는 부족합니다. 에이전트는 여러분의 **터미널·Git·Python·에디터**를 함께 사용하기 때문입니다.

```
[터미널]  ← Claude Code가 동작하는 공간, 명령을 실행하는 창구
   │
[Git]     ← 코드 변경 이력 관리, 에이전트가 커밋·diff를 활용
   │
[Python]  ← 이 강의 실습 예제의 실행 환경
   │
[VSCode]  ← 코드를 직접 확인하고 편집하는 에디터 (Claude Code와 병행)
   │
[Claude Code] ← 에이전트 CLI, 위 모든 도구를 도구로 사용
```

에이전트는 "파일을 읽고, 코드를 수정하고, 테스트를 실행하고, Git으로 커밋"하는 일을 합니다. 그 과정에서 터미널·Git·Python을 직접 호출합니다. **이 도구들이 없으면 에이전트도 할 수 없습니다.**

---

## 설치 목록

| 도구 | macOS | Windows | 역할 |
|------|-------|---------|------|
| 터미널 | **Ghostty** | **Windows Terminal** | Claude Code 실행 환경 |
| 패키지 관리자 | **Homebrew** | (winget 내장) | 나머지 도구 설치 도구 |
| Git | `brew install git` | Git for Windows | 코드 버전 관리 |
| Python 3 | `brew install python` | python.org | 실습 예제 실행 |
| VSCode | `brew install --cask visual-studio-code` | code.visualstudio.com | 코드 에디터 |
| Node.js | `brew install node` | nodejs.org | Claude Code 실행 전제 |
| Claude Code | `npm install -g @anthropic-ai/claude-code` | 동일 | AI 코딩 에이전트 |

---

## 설치 순서

의존 관계가 있으므로 반드시 아래 순서를 따릅니다.

```
① 터미널  →  ② 패키지 관리자  →  ③ Git  →  ④ Python3  →  ⑤ VSCode  →  ⑥ Node.js  →  ⑦ Claude Code
```

단계별 상세 가이드:
- macOS → `tutorials/01-macos-setup.md`
- Windows → `tutorials/02-windows-setup.md`

---

## 설치 완료 최종 검증

모든 도구가 설치됐는지 터미널에서 한 번에 확인합니다.

```bash
git --version      # git version 2.x.x
python3 --version  # Python 3.x.x
code --version     # 1.x.x
node --version     # v22.x.x
claude --version   # claude-code x.x.x
```

다섯 줄 모두 버전 번호가 나오면 환경 설정 완료입니다.
