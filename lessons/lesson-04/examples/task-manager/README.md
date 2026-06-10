# 태스크 관리 앱 (실습용)

4교시 실습에 사용하는 간단한 태스크 관리 CLI 앱입니다.

## 파일 구조

```
task-manager/
├── task_manager.py       # 앱 메인 코드 (버그 포함)
├── test_task_manager.py  # 테스트 파일
└── README.md
```

## 실행 방법

```bash
python task_manager.py
```

## 테스트 실행

```bash
pip install pytest
pytest test_task_manager.py -v
```

## 현재 기능

- 태스크 추가
- 태스크 목록 조회
- 태스크 삭제
- 완료된 태스크 보기

## 실습 목표

### 버그 수정 (실습 2)

이 앱에는 의도적으로 심어둔 버그 2개가 있습니다.  
에러 메시지를 단서로 직접 찾아보거나, 에이전트에게 도움을 받으세요.

### 기능 추가 (실습 1)

다음 기능을 TDD 방식으로 추가합니다:
- `complete_task(task_id)` — 태스크를 완료 처리
- `search_tasks(keyword)` — 키워드로 태스크 검색 (심화)
