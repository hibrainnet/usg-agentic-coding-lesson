# demo-login

로그인 인증 예제 코드입니다. 의도적으로 버그가 심어져 있으며, 1교시에서 Claude Code의 **탐색→계획→실행→검증 루프**를 직접 보여주는 데 사용합니다.

## 파일 구성

| 파일 | 설명 |
|------|------|
| `auth.py` | 로그인 인증 모듈 (버그 포함) |
| `test_auth.py` | 인증 테스트 3개 |

## 실행 방법

```bash
# 버그 확인
python3 auth.py

# 테스트 실행
pytest test_auth.py -v
```
