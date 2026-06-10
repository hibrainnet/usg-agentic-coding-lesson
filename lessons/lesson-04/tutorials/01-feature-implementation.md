# 실습 1: TDD 스타일 기능 구현 (20분)

## 준비

이번 실습에서는 `examples/task-manager/` 앱에 새 기능을 추가합니다.  
Claude Code를 열고 task-manager 디렉토리로 이동해주세요.

```bash
cd lessons/lesson-04/examples/task-manager
```

먼저 앱 구조를 파악합니다.

```
Claude Code에서:
"task_manager.py 파일의 구조를 설명해줘. 어떤 함수들이 있고, 각각 무슨 역할인지 알려줘."
```

---

## Step 1: 기존 테스트 실행해보기

구현 전에 현재 테스트 상태를 확인합니다.

```bash
pytest test_task_manager.py -v
```

결과를 보고 어떤 테스트가 있는지 파악합니다.

> `test_add_task_empty_title_raises`와 `test_delete_task_returns_false_for_missing` 2개는 의도적인 버그로 실패합니다 — Tutorial 02에서 수정합니다.

---

## Step 2: 구현할 기능 정의하기

오늘 추가할 기능: **태스크 완료 처리 (`complete_task`)**

요구사항:
- `complete_task(task_id)` 함수를 만든다
- 해당 id의 태스크를 찾아 `done: True`로 변경한다
- 존재하지 않는 id를 넣으면 `None`을 반환한다
- 성공하면 완료된 태스크 딕셔너리를 반환한다

에이전트에게 요구사항을 정리해달라고 해봅니다.

```
"complete_task(task_id) 함수를 구현하려고 합니다.
다음 요구사항을 정리해서 테스트 케이스로 만들기 좋게 표로 정리해줘:
- 존재하는 id를 넣으면 해당 태스크의 done이 True가 되어야 한다
- 존재하지 않는 id를 넣으면 None을 반환해야 한다
- 성공 시 완료된 태스크 딕셔너리를 반환해야 한다"
```

---

## Step 3: 테스트 먼저 작성하기 (Red)

요구사항을 바탕으로 테스트를 먼저 작성합니다.

```
"test_task_manager.py에 complete_task 함수를 위한 테스트를 추가해줘.
구현은 하지 말고 테스트만 작성해줘.
테스트는 다음 케이스를 포함해야 해:
1. 존재하는 태스크를 완료 처리하면 done이 True가 된다
2. 존재하지 않는 id로 호출하면 None을 반환한다"
```

테스트를 작성한 후 실행합니다.

```bash
pytest test_task_manager.py -v -k "complete"
```

테스트가 **실패**하는 것을 확인합니다. (구현이 없으니 당연히 실패해야 합니다)

---

## Step 4: 구현하기 (Green)

이제 테스트를 통과하는 구현을 요청합니다.

```
"test_task_manager.py의 complete_task 테스트를 통과하는
complete_task(task_id) 함수를 task_manager.py에 구현해줘.
구현 후 pytest를 실행해서 테스트가 통과하는지 확인해줘."
```

에이전트가 코드를 작성하고 테스트를 실행하는 것을 관찰합니다.

---

## Step 5: 기존 테스트도 확인하기

새 기능을 추가했을 때 기존 기능이 깨지지 않았는지 확인합니다.

```bash
pytest test_task_manager.py -v
```

complete_task 관련 테스트가 모두 통과하면 성공입니다.  
`test_add_task_empty_title_raises`와 `test_delete_task_returns_false_for_missing` 2개는 Tutorial 02에서 수정할 버그로 인해 아직 실패합니다 — 정상입니다.

---

## Step 6: (심화) 두 번째 기능 구현

시간이 남으면 **태스크 검색 기능**을 추가해봅니다.

요구사항:
- `search_tasks(keyword)` 함수를 만든다
- `title`에 keyword가 포함된 태스크만 반환한다
- 대소문자를 구분하지 않는다
- 결과가 없으면 빈 리스트를 반환한다

테스트 먼저 → 구현 순서로 진행해보세요.

전체 테스트를 실행하면:

```bash
pytest test_task_manager.py -v
```

`test_add_task_empty_title_raises`와 `test_delete_task_returns_false_for_missing` 2개는 여전히 실패합니다 — Tutorial 02에서 수정할 버그이므로 정상입니다.

---

## 체크리스트

- [ ] 기존 테스트를 먼저 실행해서 현재 상태를 파악했다
- [ ] 테스트를 먼저 작성하고 실패하는 것을 확인했다
- [ ] 구현 후 테스트가 통과하는 것을 확인했다
- [ ] 전체 테스트를 실행해서 기존 기능이 깨지지 않은 것을 확인했다
