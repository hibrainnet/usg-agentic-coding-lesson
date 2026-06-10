---
description: staged 변경 사항을 분석해서 Git 커밋 메시지를 제안한다
disable-model-invocation: true
---

## Staged 변경 사항

!`git diff --staged`

## 커밋 메시지 작성

위 변경 사항에 맞는 Git 커밋 메시지를 작성해줘.

**형식:**
```
타입: 짧은 설명 (50자 이내)

- 변경 사항 1
- 변경 사항 2
```

**타입 선택 기준:**
- `feat` — 새 기능 추가
- `fix` — 버그 수정
- `refactor` — 기능 변경 없는 코드 개선
- `test` — 테스트 추가 또는 수정
- `docs` — 문서 수정

staged 변경 사항이 없으면 "`git add` 먼저 해주세요."라고 안내해줘.
커밋 메시지만 출력해줘. 설명은 최소화해줘.
