# contact-book

JSON 파일 기반 주소록 CLI입니다. 3교시 프롬프팅·컨텍스트 관리 실습에 사용합니다.

## 설치

```bash
pip3 install pytest
```

## 사용법

```bash
python3 contacts.py add "홍길동" "010-1234-5678"               # 이름+전화번호
python3 contacts.py add "김철수" "010-9999-0000" "k@test.com"  # 이메일 포함
python3 contacts.py list                                        # 전체 목록
python3 contacts.py search "홍"                                 # 이름/전화번호 검색
python3 contacts.py delete 1                                    # ID로 삭제
```

## 테스트

```bash
pytest test_contacts.py -v
```

## 파일 구조

| 파일 | 역할 |
|------|------|
| `contacts.py` | CLI 진입점, 사용자 인터페이스 |
| `storage.py` | 파일 I/O 전담 (`contacts.json` 관리) |
| `test_contacts.py` | 전체 기능 테스트 |
