# 실습 2: 훅(Hooks) 설정 (15분)

## 이번 실습 목표

훅은 Claude Code의 이벤트에 반응해 자동으로 쉘 명령어를 실행합니다.  
task-manager 프로젝트를 예시로, 두 가지 훅을 설정합니다.

1. **작업 완료 알림** — 에이전트 응답 완료 시 터미널에 메시지 출력
2. **자동 테스트 실행** — task_manager.py 수정 후 pytest 자동 실행

> **Windows/macOS 모두 지원합니다.** OS별 차이가 있는 단계는 별도 표기합니다.

---

## Step 1: 현재 settings.json 확인

**macOS / Linux:**
```bash
cat .claude/settings.json 2>/dev/null || echo "파일 없음"
```

**Windows (PowerShell):**
```powershell
if (Test-Path .claude/settings.json) { Get-Content .claude/settings.json } else { echo "파일 없음" }
```

없으면 에이전트에게 생성을 요청합니다.

```
"이 프로젝트의 `.claude/settings.json` 파일을 만들어줘.
기본 구조만 있는 빈 JSON 파일이면 돼."
```

---

## Step 2: 작업 완료 알림 훅 추가 (공통)

에이전트 응답 완료 시 터미널에 메시지를 출력하는 훅입니다.  
`echo` 명령어는 macOS · Windows · Linux 모두에서 동작합니다.

```
"`.claude/settings.json`에 훅을 추가해줘.
에이전트 응답이 완료될 때(Stop 이벤트) 터미널에
'Claude 작업 완료!' 를 출력하는 훅이야.
echo 명령어를 사용해줘."
```

추가 후 Claude Code에서 아무 요청이나 보내보고, 응답 후 메시지가 출력되는지 확인합니다.

---

## Step 3: 알림 센터 패키지 설치 및 훅 추가 (OS별)

에이전트 응답 완료 시 OS 알림 센터에 팝업을 띄웁니다.  
**본인 OS에 맞는 단계**를 따라주세요.

### macOS — terminal-notifier 설치

```bash
brew install terminal-notifier
```

설치 확인:
```bash
terminal-notifier -message "테스트" -title "Claude Code"
```

알림이 뜨면 에이전트에게 훅 추가를 요청합니다.

```
"Stop 훅에 알림 센터 알림을 추가해줘.
명령어: terminal-notifier -message 'Claude 작업 완료!' -title 'Claude Code'
기존 echo 훅과 함께 실행되어야 해."
```

### Windows — BurntToast 설치 (PowerShell)

PowerShell을 **관리자 권한**으로 실행 후:

```powershell
Install-Module -Name BurntToast -Force -Scope CurrentUser
```

설치 확인:
```powershell
New-BurntToastNotification -Text "Claude Code", "테스트"
```

알림이 뜨면 에이전트에게 훅 추가를 요청합니다.

```
"Stop 훅에 알림 센터 알림을 추가해줘.
명령어: powershell -c \"New-BurntToastNotification -Text 'Claude Code', 'Claude 작업 완료!'\"
기존 echo 훅과 함께 실행되어야 해."
```

> **Windows 주의**: 실행 정책 오류가 발생하면 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` 를 먼저 실행하세요.

---

## Step 4: 소리 알림 훅 추가 (OS별)

에이전트 응답 완료 시 소리로 알림을 줍니다.  
**본인 OS에 맞는 명령어**를 사용해주세요.

### macOS

```
"Stop 훅에 소리 알림을 추가해줘.
명령어: afplay /System/Library/Sounds/Glass.aiff
기존 훅들과 함께 실행되어야 해."
```

### Windows (PowerShell)

```
"Stop 훅에 소리 알림을 추가해줘.
명령어: powershell -c \"[console]::beep(800, 400)\"
기존 훅들과 함께 실행되어야 해."
```

### Linux

```
"Stop 훅에 소리 알림을 추가해줘.
명령어: paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || true
기존 훅들과 함께 실행되어야 해."
```

---

## Step 5: task_manager.py 수정 후 pytest 자동 실행 훅 (공통)

`task_manager.py`가 수정될 때마다 pytest가 자동으로 실행됩니다.  
`python -m pytest` 는 macOS · Windows · Linux 모두 동작합니다.

```
"`.claude/settings.json`에 PostToolUse 훅을 추가해줘.
Write나 Edit 도구가 사용된 후 task-manager의 pytest를 자동 실행하는 훅이야.
실행 명령어:
  cd lessons/lesson-05/examples/task-manager && python -m pytest --tb=short -q
pytest가 없어도 오류가 나지 않도록 || true (macOS/Linux) 또는 ; exit 0 (Windows) 을 붙여줘.
내 OS는 [macOS / Windows / Linux]야."
```

테스트:
1. 에이전트에게 `task_manager.py`에 작은 변경을 요청합니다.
   ```
   "task_manager.py의 add_task 함수에 공백 한 줄을 추가해줘."
   ```
2. 파일이 저장되자마자 pytest가 자동 실행되는지 확인합니다.

---

## Step 6: 최종 설정 파일 확인

**macOS / Linux:**
```bash
cat .claude/settings.json
```

**Windows (PowerShell):**
```powershell
Get-Content .claude/settings.json
```

설정이 올바른지 확인하고, `examples/hooks-config/settings.json`의 예시와 비교합니다.

최종 settings.json은 아래와 같은 구조가 됩니다.

**macOS 예시:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Claude 작업 완료!'"
          },
          {
            "type": "command",
            "command": "terminal-notifier -message 'Claude 작업 완료!' -title 'Claude Code'"
          },
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "cd lessons/lesson-05/examples/task-manager && python -m pytest --tb=short -q || true"
          }
        ]
      }
    ]
  }
}
```

**Windows 예시:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo Claude 작업 완료!"
          },
          {
            "type": "command",
            "command": "powershell -c \"New-BurntToastNotification -Text 'Claude Code', 'Claude 작업 완료!'\""
          },
          {
            "type": "command",
            "command": "powershell -c \"[console]::beep(800, 400)\""
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "cd lessons/lesson-05/examples/task-manager && python -m pytest --tb=short -q"
          }
        ]
      }
    ]
  }
}
```

---

## 훅 비활성화 방법

훅이 너무 방해된다면 해당 배열을 비워둡니다.  
JSON은 주석을 지원하지 않으므로 삭제 대신 빈 배열로 두는 것이 안전합니다.

```json
"PostToolUse": []
```

---

## 체크리스트

- [ ] `.claude/settings.json`에 훅 설정을 추가했다
- [ ] Stop 훅(echo 알림)이 실행되는 것을 직접 확인했다
- [ ] 내 OS에 맞는 알림 센터 패키지를 설치했다 (macOS: terminal-notifier / Windows: BurntToast)
- [ ] 알림 센터 팝업이 뜨는 것을 확인했다
- [ ] 내 OS에 맞는 소리 알림 훅을 추가했다
- [ ] task_manager.py 수정 후 pytest가 자동 실행되는 것을 확인했다
- [ ] 최종 settings.json이 유효한 JSON인지 확인했다
