# [실습] Windows 환경 설정

> 🎯 목표: Windows에 개발 도구 전체를 설치하고, Claude Code 첫 실행까지 완료한다.
> ⏱️ 예상 시간: 25~30분
> 💡 막히면 손을 들어 강사/조교를 부르세요.

---

## 사전 확인

- [ ] Windows 10 (22H2 이상) 또는 Windows 11
- [ ] 인터넷 연결
- [ ] Anthropic 계정 (Claude.ai 구독 또는 API 키)

---

## STEP 1. Windows Terminal 설치

Windows Terminal은 PowerShell, Command Prompt, Git Bash를 하나의 창에서 사용하는 현대적 터미널입니다.

**방법 A — Microsoft Store (권장)**
1. 시작 메뉴에서 **Microsoft Store** 검색 후 실행
2. "Windows Terminal" 검색 후 **설치**

**방법 B — winget**
PowerShell 또는 Command Prompt를 관리자 권한으로 열고:
```powershell
winget install Microsoft.WindowsTerminal
```

### 확인
시작 메뉴에서 **Windows Terminal** 실행. 이후 모든 작업은 Windows Terminal에서 진행합니다.

> 💡 Windows Terminal에서 탭별로 PowerShell, Git Bash를 전환할 수 있습니다. 설치 후에는 **Git Bash 탭을 기본으로 사용**합니다.

---

## STEP 2. Git 설치

Git for Windows를 설치하면 Git Bash(Linux 스타일 터미널)도 함께 설치됩니다.

1. [https://git-scm.com/download/win](https://git-scm.com/download/win) 에서 **64-bit Git for Windows Setup** 다운로드
2. 설치 진행 — 대부분 기본값 유지, 아래 항목만 확인:
   - **"Adjusting your PATH environment"** → **"Git from the command line and also from 3rd-party software"** 선택
   - **"Default branch name"** → `main` 입력 권장

### Git 기본 설정

Git Bash를 열고 실행:

```bash
git config --global user.name "홍길동"
git config --global user.email "your@email.com"
```

### 설치 확인

```bash
git --version
# git version 2.x.x.windows.x
```

---

## STEP 3. Python3 설치

1. [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) 에서 **최신 Python 3.x (64-bit)** 다운로드
2. 설치 시 **반드시** 아래 항목 체크:
   - ✅ **"Add Python 3.x to PATH"** ← 이것을 빠뜨리면 `python` 명령이 작동하지 않습니다
3. **"Install Now"** 클릭

> ⚠️ "Add to PATH" 체크를 놓쳤다면 제어판 → 프로그램 제거에서 Python을 제거하고 다시 설치하는 것이 가장 빠릅니다.

### 설치 확인

Windows Terminal(Git Bash)에서:

```bash
python3 --version
# Python 3.x.x

pip3 --version
# pip x.x.x
```

> 💡 Windows에서는 `python`과 `python3` 모두 동작하는 경우가 있습니다. 이 강의에서는 `python3`을 사용합니다.

---

## STEP 4. VSCode 설치

**방법 A — 공식 사이트**
1. [https://code.visualstudio.com](https://code.visualstudio.com) 에서 **Windows용 다운로드**
2. 설치 중 아래 항목 체크 권장:
   - ✅ "Add to PATH"
   - ✅ "Register Code as an editor for supported file types"

**방법 B — winget**
```powershell
winget install Microsoft.VisualStudioCode
```

### 설치 확인

Git Bash에서:

```bash
code --version
# 1.x.x
```

---

## STEP 5. Node.js 설치

Claude Code는 Node.js 위에서 동작합니다.

1. [https://nodejs.org](https://nodejs.org) 에서 **LTS 버전** 다운로드
2. 설치 진행 — 기본값 그대로 진행 (`npm` 포함 설치됨)

**또는 winget:**
```powershell
winget install OpenJS.NodeJS.LTS
```

### 설치 확인

Git Bash에서:

```bash
node --version
# v22.x.x

npm --version
# 10.x.x
```

---

## STEP 6. Claude Code 설치

Git Bash에서:

```bash
npm install -g @anthropic-ai/claude-code
```

### 설치 확인

```bash
claude --version
# claude-code x.x.x
```

---

## STEP 7. Claude Code 인증

```bash
mkdir ~/claude-practice
cd ~/claude-practice
claude
```

처음 실행하면 인증 방식을 선택합니다.

```
How would you like to authenticate?
❯ 1. Sign in with Claude.ai (browser)
  2. Enter API key manually
```

- **Claude.ai 구독 있음** → 1번 선택 후 브라우저에서 로그인
- **API 키 있음** → 2번 선택 후 키 붙여넣기

인증이 완료되면 대화 프롬프트(`>`)가 나타납니다.

---

## ✅ 최종 확인 체크리스트

Git Bash에서 아래를 순서대로 실행합니다.

```bash
git --version      # git version 2.x.x.windows.x
python3 --version  # Python 3.x.x
code --version     # 1.x.x
node --version     # v22.x.x
claude --version   # claude-code x.x.x
```

5줄 모두 버전이 출력되면 완료입니다.

---

## 🆘 자주 막히는 부분

| 증상 | 해결 |
|------|------|
| `python3: command not found` | 제어판에서 Python 제거 후 "Add to PATH" 체크하고 재설치 |
| `code: command not found` | VSCode 재설치 시 "Add to PATH" 체크, 또는 Git Bash 재시작 |
| `npm install` 권한 오류 | PowerShell을 **관리자 권한**으로 열고 재실행 |
| `claude` 실행 시 바이러스 경고 | Windows Defender → 허용 목록에 추가 (강사에게 문의) |
| 인증 브라우저 창이 안 열림 | `claude auth` 명령으로 다시 시도 |

---

Windows 설정 완료! 이제 `tutorials/03-first-workflow.md`로 이동합니다.
