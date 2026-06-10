# [실습] 첫 번째 워크플로우

> 🎯 목표: Claude Code로 실제 코드를 탐색하고, 버그를 찾아 수정하는 첫 번째 에이전트 협업을 경험한다.
> ⏱️ 예상 시간: 20~25분
> 💡 환경 설정(`01-macos-setup.md` 또는 `02-windows-setup.md`)이 완료된 상태에서 진행합니다.

---

## STEP 0. 샘플 프로젝트 준비

실습에 사용할 To-Do CLI 프로젝트 폴더로 이동합니다.

```bash
cd 경로/lessons/lesson-02/examples/todo-cli
```

> 강의 저장소 전체를 다운로드한 경우, 아래처럼 경로를 맞춥니다.
> ```bash
> cd ~/Downloads/usg-agentic-coding-lesson/lessons/lesson-02/examples/todo-cli
> ```

내용을 확인합니다.

```bash
ls
# README.md  todo.py  test_todo.py
```

---

## STEP 1. Claude Code 실행

```bash
claude
```

대화 프롬프트(`>`)가 나타나면 준비됩니다.

---

## STEP 2. 코드 구조 탐색

### 2-1. 프로젝트 설명 요청

```
> 이 프로젝트의 구조와 각 파일의 역할을 설명해줘.
```

Claude가 `todo.py`와 `test_todo.py`를 읽고 전체 구조를 설명합니다.

### 2-2. 특정 함수 설명 요청

```
> complete_todo 함수가 하는 일을 설명해줘.
```

### 2-3. 동작 확인 (새 터미널 탭에서)

Claude에게 물어보기 전에 직접 실행해 봅니다.

```bash
python3 todo.py add "우유 사기"
python3 todo.py add "빵 사기"
python3 todo.py list
```

출력:
```
추가됨: 우유 사기
추가됨: 빵 사기
1. [○] 우유 사기
2. [○] 빵 사기
```

1번 항목을 완료 처리해 봅니다.

```bash
python3 todo.py done 1
python3 todo.py list
```

뭔가 이상하지 않나요? 결과를 관찰하세요.

---

## STEP 3. 버그 발견

테스트를 실행해서 무엇이 실패하는지 확인합니다.

```bash
pytest test_todo.py -v
```

테스트 중 하나가 실패하는 것을 확인했습니다. 이제 Claude Code에게 원인을 찾아달라고 합니다.

```
> pytest test_todo.py -v 를 실행하면 test_complete_todo_marks_done이 실패해.
  원인을 찾아서 설명해줘. (아직 고치지 말고 설명만)
```

Claude가 코드를 읽고 버그 원인을 설명합니다. 설명을 이해하고 나서 다음 단계로 넘어갑니다.

> 🔑 "바로 고쳐줘"라고 하는 것보다 "설명만 해줘"라고 먼저 요청하는 게 좋은 습관입니다. 이해하지 못한 수정을 승인하는 것은 위험합니다.

---

## STEP 4. 버그 수정

원인을 이해했다면 이제 수정을 요청합니다.

```
> 방금 설명한 버그를 고쳐줘. 수정 전에 변경 내용을 보여줘.
```

Claude가 변경 내용 미리보기를 보여줍니다.

```diff
  todo.py를 수정하려고 합니다:

-     todos[n]["done"] = True
+     todos[n - 1]["done"] = True
  ...
-     print(f"완료: {todos[n]['text']}")
+     print(f"완료: {todos[n - 1]['text']}")

  이 변경을 적용할까요?
```

**변경 내용을 직접 읽고 이해한 뒤** 허용합니다.

---

## STEP 5. 수정 결과 검증

수정됐는지 직접 확인합니다.

```
> 방금 수정이 맞는지 pytest를 실행해서 확인해줘.
```

Claude가 테스트를 실행하고 결과를 보여줍니다.

```
test_todo.py::test_add_todo               PASSED
test_todo.py::test_complete_todo_marks_done PASSED  ← 이제 통과!
test_todo.py::test_complete_todo_invalid_number PASSED
```

직접도 확인합니다.

```bash
python3 todo.py done 1
python3 todo.py list
```

```
완료: 우유 사기
1. [✓] 우유 사기
2. [○] 빵 사기
```

---

## STEP 6. 슬래시 커맨드 체험

```
> /help
```

사용 가능한 커맨드 목록을 확인합니다.

새 작업을 시작하기 전에 맥락을 초기화합니다.

```
> /clear
```

세션을 종료합니다.

```
> /exit
```

---

## STEP 7. (선택) 기능 추가 실습

여유가 있다면 새로운 기능을 추가해 봅니다.

```bash
claude
```

```
> todo.py에 할 일을 삭제하는 기능을 추가해줘.
  명령어는 "python3 todo.py delete <번호>" 형태로 만들어줘.
  기능을 추가한 뒤 테스트 케이스도 작성해줘.
```

---

## ✅ 완료 체크리스트

- [ ] `claude`를 실행하고 코드 구조 설명을 받았다
- [ ] `complete_todo` 함수의 역할을 이해했다
- [ ] 버그 원인을 Claude에게 설명으로 먼저 들었다
- [ ] 변경 미리보기를 읽고 이해한 뒤 허용했다
- [ ] pytest 전체 통과를 확인했다
- [ ] `/help`, `/clear`, `/exit`를 사용해봤다

---

## 🤔 생각해보기

**Q. 버그를 수정할 때 "설명만 해줘"라고 먼저 요청한 것과 바로 "고쳐줘"라고 한 것은 왜 다를까?**

**Q. 변경 미리보기를 꼼꼼히 읽어야 하는 이유는 무엇일까?**

**Q. 이번 실습에서 에이전트의 탐색→계획→실행→검증 루프를 어느 단계에서 확인했는가?**
