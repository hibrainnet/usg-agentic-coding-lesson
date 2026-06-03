# 실습 1: 미니 프로젝트 기획 (10분)

## 오늘 만들 것

**메모 관리 CLI** — 터미널에서 메모를 저장·조회·검색·삭제하는 앱

`examples/note-cli/` 폴더에 뼈대 코드가 있습니다.  
이 뼈대를 시작점으로 해서 기능을 구현합니다.

---

## Step 1: 뼈대 코드 파악하기

`examples/note-cli/` 폴더를 Claude Code로 탐색합니다.

```
"examples/note-cli/ 폴더의 구조와 note_app.py 파일을 설명해줘.
어떤 함수가 있고, 어떤 기능이 이미 구현되어 있는지 알려줘.
어떤 기능이 아직 빈 껍데기인지도 알려줘."
```

---

## Step 2: 구현할 기능 목록 확인

뼈대 코드에는 다음 기능이 준비되어 있습니다.

| 함수 | 상태 | 설명 |
|------|------|------|
| `add_note(title, content)` | 구현 필요 | 메모 추가 |
| `get_notes()` | 구현 필요 | 전체 메모 조회 |
| `get_note(note_id)` | 구현 필요 | 특정 메모 조회 |
| `delete_note(note_id)` | 구현 필요 | 메모 삭제 |
| `search_notes(keyword)` | 구현 필요 | 키워드 검색 |
| `save_to_file()` / `load_from_file()` | 구현 완료 | JSON 파일 저장·불러오기 |

오늘은 위 기능을 순서대로 구현합니다.

---

## Step 3: CLAUDE.md 작성하기

미니 프로젝트용 CLAUDE.md를 만듭니다.

```
"note-cli 프로젝트를 위한 CLAUDE.md를 만들어줘.
다음 내용을 포함해줘:
- 프로젝트 설명 (메모 관리 CLI)
- 코딩 규칙: Python, pytest, 함수는 snake_case
- 실행 명령어: python note_app.py
- 테스트 실행: pytest test_note_app.py -v
- 에러 처리 규칙: 없는 ID는 None 반환, 빈 입력은 ValueError 발생"
```

---

## Step 4: 개발 계획 세우기

계획 모드(plan mode)로 전체 구현 순서를 먼저 정합니다.

```
"note_app.py의 빈 함수들을 TDD 방식으로 구현하려고 해.
test_note_app.py의 테스트를 보고 어떤 순서로 구현할지 계획을 알려줘.
지금은 계획만, 코드는 작성하지 말아줘."
```

계획을 검토하고 OK 신호를 주면 구현을 시작합니다.

---

## 체크리스트

- [ ] 뼈대 코드의 구조와 구현할 함수 목록을 파악했다
- [ ] note-cli용 CLAUDE.md를 작성했다
- [ ] 구현 순서 계획을 에이전트와 함께 세웠다
