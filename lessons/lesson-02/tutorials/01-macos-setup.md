# 실습 1: macOS 환경 설정

> 🎯 목표: macOS에 개발 도구 전체를 설치하고, Claude Code 첫 실행까지 완료한다.
> ⏱️ 예상 시간: 25~30분
> 💡 막히면 손을 들어 강사/조교를 부르세요.

---

## 사전 확인

- [ ] macOS 12 Monterey 이상 (Apple Silicon M1/M2/M3 또는 Intel 모두 가능)
- [ ] 인터넷 연결
- [ ] Anthropic 계정 (Claude.ai 구독 또는 API 키)

---

## STEP 1. Ghostty 설치

Ghostty는 빠르고 현대적인 터미널 에뮬레이터입니다.

1. [https://ghostty.org](https://ghostty.org) 에서 **Download** 클릭
2. 다운로드된 `.dmg` 파일을 열고 **Ghostty.app을 Applications 폴더로 드래그**
3. Launchpad 또는 Spotlight(`⌘+Space`)에서 **Ghostty** 실행
4. "개발자를 확인할 수 없음" 경고가 나오면 → **시스템 환경설정 > 개인 정보 보호 및 보안 > 어디서나 허용**

이후 모든 터미널 작업은 **Ghostty에서 진행**합니다.

---

## STEP 2. Homebrew 설치

Homebrew는 macOS의 패키지 관리자입니다. 이후 대부분의 도구를 Homebrew로 설치합니다.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

> 비밀번호를 물어보면 Mac 로그인 비밀번호를 입력합니다. 입력 중 화면에 아무것도 표시되지 않는 것은 정상입니다.

### Apple Silicon(M1/M2/M3) 추가 설정

설치 완료 후 화면에 나타나는 "Next steps" 안내를 따라 PATH를 설정합니다.

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### 설치 확인

```bash
brew --version
# Homebrew x.x.x
```

---

## STEP 3. Git 설치

```bash
brew install git
```

### Git 기본 설정 (처음 한 번만)

```bash
git config --global user.name "홍길동"
git config --global user.email "your@email.com"
```

### 설치 확인

```bash
git --version
# git version 2.x.x
```

---

## STEP 4. Python3 설치

```bash
brew install python
```

### 설치 확인

```bash
python3 --version
# Python 3.x.x

pip3 --version
# pip x.x.x
```

---

## STEP 5. VSCode 설치

```bash
brew install --cask visual-studio-code
```

### PATH 설정 (터미널에서 `code` 명령 사용)

VSCode를 실행한 뒤 `⌘+Shift+P` → **"Shell Command: Install 'code' command in PATH"** 선택.

### 설치 확인

```bash
code --version
# 1.x.x
```

---

## STEP 6. Node.js 설치

Claude Code는 Node.js 위에서 동작합니다.

```bash
brew install node
```

### 설치 확인

```bash
node --version
# v22.x.x

npm --version
# 10.x.x
```

---

## STEP 7. Claude Code 설치

```bash
npm install -g @anthropic-ai/claude-code
```

### 설치 확인

```bash
claude --version
# claude-code x.x.x
```

---

## STEP 8. Claude Code 인증

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

터미널에서 아래를 순서대로 실행합니다.

```bash
git --version      # git version 2.x.x
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
| `brew: command not found` | 터미널 새로 열기 → 그래도 안 되면 STEP 2의 PATH 설정 재실행 |
| `python3: command not found` | `brew install python` 재실행 후 터미널 재시작 |
| `code: command not found` | VSCode 실행 후 `⌘+Shift+P` → "Install 'code' command in PATH" |
| `npm install` 권한 오류 | `sudo npm install -g @anthropic-ai/claude-code` |
| Ghostty 실행 시 "개발자 확인 불가" | 시스템 환경설정 > 개인 정보 보호 및 보안 > 그래도 열기 |

---

macOS 설정 완료! 이제 `tutorials/03-first-workflow.md`로 이동합니다.
