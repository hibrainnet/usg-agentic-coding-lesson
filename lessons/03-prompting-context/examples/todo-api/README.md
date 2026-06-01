# todo-api

Flask 기반 간단한 Todo REST API입니다. 3교시 프롬프트 비교 심화 실습에 사용합니다.

## 설치

```bash
pip3 install flask pytest
```

## 서버 실행

```bash
python3 app.py
# http://localhost:5000 에서 실행됨
```

## API 동작 확인 (curl)

```bash
# 목록 조회
curl http://localhost:5000/todos

# 생성
curl -X POST http://localhost:5000/todos \
     -H "Content-Type: application/json" \
     -d '{"title": "우유 사기"}'

# 단일 조회
curl http://localhost:5000/todos/1

# 수정
curl -X PUT http://localhost:5000/todos/1 \
     -H "Content-Type: application/json" \
     -d '{"done": true}'

# 삭제
curl -X DELETE http://localhost:5000/todos/1
```

## 테스트 (서버 실행 없이)

```bash
pytest test_app.py -v
```

## 파일 구조

| 파일 | 역할 |
|------|------|
| `app.py` | Flask 라우터 (엔드포인트 정의) |
| `models.py` | 인메모리 저장소 (`TodoStore`) |
| `test_app.py` | Flask 테스트 클라이언트 기반 테스트 |
