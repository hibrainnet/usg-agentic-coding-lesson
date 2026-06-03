# 메모 앱 프로젝트

## 프로젝트 개요

터미널에서 메모를 관리하는 CLI 앱입니다.
메모 추가·조회·검색·삭제 기능을 제공합니다.

## 기술 스택

- Python 3.8+
- pytest (테스트)
- JSON 파일 저장

## 명령어

```bash
# 앱 실행
python note_app.py

# 테스트 실행
pytest test_note_app.py -v

# 특정 테스트만 실행
pytest test_note_app.py -v -k "search"
```

## 코딩 규칙

- 함수명: snake_case
- 빈 입력(title="")은 ValueError 발생
- 없는 ID 조회/삭제는 None/False 반환 (예외 발생 금지)
- 타입 힌트 생략 가능 (간결함 우선)

## 데이터 구조

```python
note = {
    "id": int,       # 1부터 시작, 자동 증가
    "title": str,    # 메모 제목
    "content": str   # 메모 내용
}
```

## 구현 우선순위

1. add_note → 2. get_notes / get_note → 3. delete_note → 4. search_notes
