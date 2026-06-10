# [실습] CLAUDE.md 작성하기

> 🎯 목표: contact-book 프로젝트용 CLAUDE.md를 만들고, 있을 때와 없을 때의 차이를 확인한다.
> ⏱️ 예상 시간: 15분
> 💡 프롬프트 비교 실습(`01-prompt-comparison.md`)에 이어서 진행합니다. `/clear`로 대화를 초기화한 상태에서 시작합니다.

---

## STEP 1. /init으로 CLAUDE.md 초안 생성

contact-book 폴더에서 Claude Code를 실행합니다.

```bash
cd 경로/lessons/lesson-03/examples/contact-book
claude
```

`/init` 커맨드를 실행합니다.

```
> /init
```

Claude가 프로젝트를 분석해 `CLAUDE.md` 초안을 생성합니다. 생성된 파일을 확인합니다.

```bash
cat CLAUDE.md
```

---

## STEP 2. 생성된 초안 검토

자동 생성된 CLAUDE.md를 읽어보세요. 아마 다음과 같이 구성되어 있을 것입니다.

- 프로젝트 개요
- 실행 방법
- 파일 구조 설명

**하지만 빠진 것들이 있습니다.** 에이전트가 자동으로 알 수 없는 것들, 즉 팀/프로젝트만의 규칙이 없습니다.

`examples/sample-CLAUDE.md`를 참고해 아래 내용을 추가합니다.

---

## STEP 3. CLAUDE.md 커스터마이징

VSCode로 CLAUDE.md를 열어 수정합니다.

```bash
code CLAUDE.md
```

아래 내용을 추가하세요.

```markdown
## 코딩 규칙

- 모든 함수에 한국어 docstring 작성
- 타입 힌트 필수 (파라미터와 반환값 모두)
- 파일 I/O는 반드시 `storage.py`에서만 처리
- 에러 메시지는 한국어로, "오류: " 접두어 사용
- 새 기능 추가 시 `test_contacts.py`에 테스트도 반드시 함께 작성

## 테스트

pytest test_contacts.py -v

## 아키텍처

- contacts.py: CLI 진입점, 사용자 인터페이스
- storage.py: 파일 I/O 전담 (contacts.json 관리)
- test_contacts.py: 전체 기능 테스트
```

---

## STEP 4. CLAUDE.md 효과 확인

CLAUDE.md가 적용된 상태에서 새 요청을 합니다. (Claude Code를 재시작하면 CLAUDE.md를 자동으로 읽습니다.)

```bash
claude
```

규칙을 명시하지 않고 간단하게만 요청합니다.

```
> search_contacts()가 이메일 필드도 검색하도록 수정해줘.
```

응답을 확인하세요. CLAUDE.md에 적어둔 규칙들이 자동으로 적용되는지 봅니다.

- 타입 힌트가 추가됐는가?
- 한국어 docstring이 있는가?
- 테스트가 자동으로 추가됐는가?

---

## STEP 5. 비교 (선택)

여유가 있다면, 같은 요청을 CLAUDE.md 없이 해봅니다.

1. 다른 폴더에 contact-book 복사 (CLAUDE.md 제외)
2. 동일한 요청 전송
3. 결과 비교

---

## 🤔 생각해보기

**Q. CLAUDE.md에 어떤 내용을 넣으면 가장 도움이 될까? 팀 프로젝트라면?**

**Q. CLAUDE.md를 너무 길게 쓰면 오히려 역효과가 날 수 있을까?**
