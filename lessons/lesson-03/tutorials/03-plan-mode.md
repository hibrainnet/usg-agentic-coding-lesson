# [실습] 계획 모드로 복잡한 작업 설계하기

> 🎯 목표: 여러 파일과 기능을 동시에 변경하는 복잡한 작업에서 계획 모드를 사용해 사전에 검토하고 방향을 조정한다.
> ⏱️ 예상 시간: 10분
> 💡 CLAUDE.md가 이미 작성된 contact-book 폴더에서 진행합니다.

---

## 상황 설정

다음 기능을 contact-book에 추가하려 합니다.

> "연락처에 즐겨찾기(favorite) 기능 추가. `favorite` 명령으로 토글, `list --favorites`로 즐겨찾기만 조회."

이 작업은:
- contacts.py 수정 (새 명령어 추가)
- storage.py 수정 (favorite 필드 처리)
- test_contacts.py 수정 (새 테스트)
- 기존 contacts.json 형식 호환 유지

여러 파일을 동시에 건드리고 데이터 형식도 바뀌므로, 바로 실행하기 전에 계획을 먼저 보는 것이 안전합니다.

---

## STEP 1. 계획 모드 활성화

**방법 A — Shift+Tab 토글:**
Claude Code 입력란에서 `Shift+Tab`을 누르면 계획 모드(Plan Mode)가 활성화됩니다. 입력창에 아이콘이 표시됩니다.

**방법 B — 요청에 명시:**

```
> 구현하기 전에 변경할 내용의 계획을 먼저 설명해줘.
> 내가 확인한 뒤 "진행해줘"라고 하면 그때 구현해줘.
>
> 요청: contact-book에 즐겨찾기(favorite) 기능을 추가해줘.
> - python3 contacts.py favorite <ID> 로 즐겨찾기 on/off 토글
> - python3 contacts.py list --favorites 로 즐겨찾기 연락처만 출력
> - 기존 contacts.json에 이미 저장된 연락처는 favorite 필드가 없어도 오류 없이 동작
> - 관련 테스트 케이스 작성
```

---

## STEP 2. 계획 검토

Claude가 계획을 제시합니다. 다음 항목을 확인하세요.

- 어느 파일을 수정한다고 했나요?
- storage.py에서 기존 데이터 호환을 어떻게 처리한다고 했나요?
- 테스트는 몇 건 추가한다고 했나요?
- 순서가 논리적인가요?

---

## STEP 3. 계획 수정 요청

계획의 일부가 마음에 들지 않으면, 실행 전에 수정합니다.

예시 수정 요청:

```
> 계획 2번에서 storage.py는 수정하지 말고, contacts.py 안에서 favorite 필드 처리를 해줘.
> 나머지는 괜찮아. 이렇게 수정된 계획으로 진행해줘.
```

또는 전체 승인:

```
> 계획 좋아. 진행해줘.
```

---

## STEP 4. 결과 확인

구현이 완료되면 직접 테스트합니다.

```bash
python3 contacts.py add "홍길동" "010-1234-5678"
python3 contacts.py add "김철수" "010-9999-0000"
python3 contacts.py favorite 1
python3 contacts.py list
python3 contacts.py list --favorites
pytest test_contacts.py -v
```

---

## ✅ 완료 체크리스트

- [ ] 계획 모드로 구현 계획을 먼저 확인했다
- [ ] 계획의 일부를 수정 요청했다 (또는 검토 후 그대로 승인했다)
- [ ] 즐겨찾기 토글(`favorite`)이 동작한다
- [ ] `list --favorites`로 즐겨찾기만 출력된다
- [ ] 기존 연락처(favorite 필드 없음)도 오류 없이 동작한다
- [ ] pytest 전체 통과를 확인했다

---

## 🤔 생각해보기

**Q. 계획 모드를 매번 쓰는 것이 좋을까, 아니면 특정 상황에서만 쓰는 것이 좋을까?**

**Q. 계획이 마음에 들지 않을 때 그냥 "아니오"라고 하면 어떻게 될까?**
