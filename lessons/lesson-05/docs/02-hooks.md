# 훅(Hooks): 특정 시점에 자동 실행

## 훅이란?

Claude Code가 특정 이벤트를 처리할 때 **자동으로 실행되는 쉘 명령어**입니다.  
에이전트에게 지시하지 않아도, 설정한 시점에 항상 실행됩니다.

스킬이 "사람이 호출"하는 방식이라면, 훅은 **이벤트가 발생하면 자동으로 실행**됩니다.

---

## 설정 위치

`~/.claude/settings.json` (글로벌) 또는 `.claude/settings.json` (프로젝트)

```json
{
  "hooks": {
    "이벤트이름": [
      {
        "matcher": "매칭 조건 (선택)",
        "hooks": [
          {
            "type": "command",
            "command": "실행할 쉘 명령어"
          }
        ]
      }
    ]
  }
}
```

---

## 주요 이벤트

| 이벤트 | 발생 시점 |
|--------|-----------|
| `Stop` | 에이전트가 응답을 완료한 후 |
| `PostToolUse` | 에이전트가 도구를 사용한 직후 |
| `PreToolUse` | 에이전트가 도구를 사용하기 직전 |
| `Notification` | 에이전트가 알림을 보낼 때 |

`matcher`는 도구 이름으로 필터링합니다. 예: `"Write|Edit"` → Write 또는 Edit 도구 사용 시에만 실행.

---

## 예시 1: 작업 완료 시 터미널 알림 (공통)

`echo`는 macOS · Windows · Linux 모두 동작합니다.

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Claude 작업 완료!'"
          }
        ]
      }
    ]
  }
}
```

## 예시 2: 소리 알림 (OS별)

OS에 맞는 명령어를 사용합니다.

**macOS:**
```json
{ "type": "command", "command": "afplay /System/Library/Sounds/Glass.aiff" }
```

**Windows (PowerShell):**
```json
{ "type": "command", "command": "powershell -c \"[console]::beep(800, 400)\"" }
```

**Linux:**
```json
{ "type": "command", "command": "paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || true" }
```

## 예시 3: task_manager.py 수정 후 자동 테스트 실행

파일이 수정될 때마다 pytest가 자동으로 실행됩니다.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "cd lessons/lesson-05/examples/task-manager && python -m pytest -q 2>&1 | tail -5 || true"
          }
        ]
      }
    ]
  }
}
```

## 예시 4: Python 파일 수정 후 자동 포맷

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "black . --quiet 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

---

## 주의사항

- 훅은 **에이전트가 제어할 수 없습니다** — 설정된 명령어가 이벤트 발생 시 항상 실행됩니다.
- 무거운 명령어(전체 빌드, 오래 걸리는 테스트)를 훅에 넣으면 매우 느려집니다.
- `|| true`를 붙이면 훅 실패 시 에이전트 동작이 중단되지 않습니다.
- 여러 훅을 `hooks` 배열에 나란히 나열하면 순서대로 실행됩니다.

---

## 핵심 정리

```
✅ 훅 = 이벤트 발생 시 자동 실행되는 쉘 명령어
✅ Stop 이벤트 → 응답 완료 후 실행
✅ PostToolUse + matcher → 특정 도구 사용 후 실행
✅ 설정 위치: .claude/settings.json
```
