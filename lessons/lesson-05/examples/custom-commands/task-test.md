---
description: task-manager의 pytest 테스트를 실행하고 결과를 요약한다
---

다음 명령어를 실행하고 결과를 요약해줘:

```bash
cd lessons/lesson-04/examples/task-manager && python -m pytest -v
```

테스트 결과를 다음 형식으로 요약해줘:
- 전체 테스트 수 / 통과 수 / 실패 수
- 실패한 테스트가 있으면 파일명:줄번호와 함께 실패 원인과 수정 방법 제안
- 모두 통과하면 "✅ 모든 테스트 통과"라고 알려줘

pytest가 설치되어 있지 않으면 설치 방법을 안내해줘:
```bash
pip install pytest
```
