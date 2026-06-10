# Contact Book 프로젝트

## 프로젝트 개요

JSON 파일 기반 주소록 CLI 도구 (Python 3.10+)

## 실행 방법

```bash
python3 contacts.py add "이름" "010-xxxx-xxxx" ["email@example.com"]
python3 contacts.py list
python3 contacts.py search "키워드"
python3 contacts.py delete <ID>
```

## 테스트

```bash
pytest test_contacts.py -v
```

## 코딩 규칙

- 모든 함수에 한국어 docstring 작성
- 타입 힌트 필수 (파라미터와 반환값 모두)
- 파일 I/O는 반드시 `storage.py`에서만 처리 — `contacts.py`에서 직접 json 다루지 말 것
- 에러 메시지는 한국어로, "오류: " 접두어 사용
- 새 기능 추가 시 `test_contacts.py`에 테스트도 반드시 함께 작성

## 아키텍처

```
contacts.py      ← CLI 진입점, 사용자 인터페이스
storage.py       ← 파일 I/O 전담 (contacts.json 관리)
test_contacts.py ← 전체 기능 테스트
contacts.json    ← 데이터 파일 (자동 생성)
```

## 데이터 형식

```json
[
  {
    "id": 1,
    "name": "홍길동",
    "phone": "010-1234-5678",
    "email": "hong@example.com"
  }
]
```
