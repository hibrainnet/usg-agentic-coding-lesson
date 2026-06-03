# 실습 2: 훅(Hooks) 설정 (15분)

## 준비

훅은 Claude Code의 이벤트에 반응해 자동으로 쉘 명령어를 실행합니다.  
이번 실습에서는 두 가지 훅을 설정합니다.

1. **작업 완료 알림** — 에이전트가 응답을 마치면 소리/메시지 출력
2. **파일 저장 후 자동 포맷** — Python 파일 수정 후 자동으로 `black` 실행

---

## Step 1: 현재 settings.json 확인

프로젝트 설정 파일을 확인합니다.

```bash
cat .claude/settings.json 2>/dev/null || echo "파일 없음"
```

없으면 에이전트에게 생성을 요청합니다.

```
"이 프로젝트의 `.claude/settings.json` 파일을 만들어줘.
기본 구조만 있는 빈 JSON 파일이면 돼."
```

---

## Step 2: 작업 완료 알림 훅 추가

에이전트 응답 완료 시 터미널에 메시지를 출력하는 훅을 추가합니다.

```
"`.claude/settings.json`에 훅을 추가해줘.
에이전트 응답이 완료될 때(Stop 이벤트) 터미널에
'✅ Claude 작업 완료!' 를 출력하는 훅이야.
echo 명령어를 사용해줘."
```

추가 후 Claude Code에서 아무 요청이나 보내보고, 응답 후 메시지가 출력되는지 확인합니다.

---

## Step 3: macOS 소리 알림 훅 (macOS 사용자)

macOS를 사용한다면 소리 알림도 추가할 수 있습니다.

```
"Stop 훅에 macOS 소리 알림도 추가해줘.
afplay /System/Library/Sounds/Glass.aiff 명령어를 사용해.
기존 echo 훅과 함께 실행되어야 해."
```

Windows/Linux 사용자는 이 단계를 건너뜁니다.

---

## Step 4: Python 파일 자동 포맷 훅 추가

Python 파일이 수정될 때 자동으로 `black`으로 포맷하는 훅을 추가합니다.

먼저 black이 설치되어 있는지 확인합니다.

```bash
black --version 2>/dev/null || pip install black
```

그다음 훅을 추가합니다.

```
"`.claude/settings.json`에 PostToolUse 훅을 추가해줘.
Write나 Edit 도구가 사용된 후 black으로 Python 파일을 자동 포맷하는 훅이야.
black이 없어도 오류가 나지 않도록 `|| true`를 붙여줘."
```

테스트: task-manager의 `task_manager.py`를 열고 에이전트에게 작은 변경을 요청한 뒤, 저장 후 자동으로 포맷되는지 확인합니다.

---

## Step 5: 최종 설정 파일 확인

```bash
cat .claude/settings.json
```

설정이 올바른지 확인하고, `examples/hooks-config/settings.json`의 예시와 비교합니다.

---

## 훅 비활성화 방법

훅이 너무 방해된다면 해당 항목을 `settings.json`에서 삭제하거나 주석 처리합니다.  
JSON은 주석을 지원하지 않으므로, 잠시 비활성화하려면 훅 배열을 비워둡니다.

```json
"Stop": []
```

---

## 체크리스트

- [ ] `.claude/settings.json`에 훅 설정을 추가했다
- [ ] Stop 훅이 실행되는 것을 직접 확인했다
- [ ] PostToolUse 훅으로 파일 수정 후 자동 동작이 실행되는 것을 확인했다
- [ ] 최종 settings.json이 유효한 JSON인지 확인했다
