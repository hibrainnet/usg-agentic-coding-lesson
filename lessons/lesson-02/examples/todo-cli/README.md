# todo-cli

JSON 파일 기반 할 일 관리 CLI입니다. 2교시 기본 워크플로우 실습에 사용합니다.

## 설치

```bash
pip3 install pytest
```

## 사용법

```bash
python3 todo.py add "할 일 내용"   # 항목 추가
python3 todo.py list               # 목록 출력
python3 todo.py done <번호>        # 완료 처리
```

## 테스트

```bash
pytest test_todo.py -v
```
