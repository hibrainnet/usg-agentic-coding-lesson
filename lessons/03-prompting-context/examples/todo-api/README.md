# todo-api

Flask 기반 간단한 Todo REST API입니다. 3교시 프롬프트 비교 심화 실습에 사용합니다.

## 환경 설정

```bash
# 1. 가상환경 생성
python3 -m venv .venv

# 2. 활성화
# macOS / Linux
source .venv/bin/activate

# Windows (Git Bash)
source .venv/Scripts/activate

# Windows (PowerShell / CMD)
.venv\Scripts\activate

# 3. 의존성 설치
pip install -r requirements.txt
```

> 이후 모든 명령은 가상환경이 활성화된 상태 (`(.venv)` 프롬프트 표시)에서 실행합니다.

## 테스트 실행 (서버 없이)

```bash
pytest test_app.py -v
```

## 서버 실행

```bash
python app.py
# http://localhost:4000 에서 실행됨
```

## API 동작 확인 (curl)

서버가 실행 중일 때:

```bash
# 목록 조회
curl http://localhost:4000/todos

# 생성
curl -X POST http://localhost:4000/todos \
     -H "Content-Type: application/json" \
     -d '{"title": "우유 사기"}'

# 단일 조회
curl http://localhost:4000/todos/1

# 수정
curl -X PUT http://localhost:4000/todos/1 \
     -H "Content-Type: application/json" \
     -d '{"done": true}'

# 삭제
curl -X DELETE http://localhost:4000/todos/1
```

## 가상환경 비활성화

```bash
deactivate
```

## 파일 구조

| 파일 | 역할 |
|------|------|
| `app.py` | Flask 라우터 (엔드포인트 정의) |
| `models.py` | 인메모리 저장소 (`TodoStore`) |
| `test_app.py` | Flask 테스트 클라이언트 기반 테스트 |
| `requirements.txt` | 의존성 목록 |
