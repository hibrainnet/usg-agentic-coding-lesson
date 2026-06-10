# 태스크 관리 앱 (5교시 실습용 시작 코드)

4교시 실습을 모두 마친 상태의 완성본입니다.  
5교시 스킬·훅·MCP·서브에이전트 실습은 이 코드를 기준으로 진행합니다.

## 파일 구조

```
task-manager/
├── task_manager.py       # 앱 메인 코드 (4교시 완성본)
├── test_task_manager.py  # pytest 테스트 (전체 커버리지)
├── requirements.txt      # pytest 의존성
└── README.md
```

## 실행 방법

```bash
# 의존성 설치
pip install -r requirements.txt

# 앱 실행
python task_manager.py

# 테스트 실행
pytest test_task_manager.py -v
```

## 구현된 기능

| 함수 | 설명 |
|------|------|
| `add_task(title)` | 태스크 추가 (빈 제목 검증 포함) |
| `get_tasks()` | 전체 태스크 목록 반환 |
| `get_task(task_id)` | ID로 태스크 조회 |
| `delete_task(task_id)` | 태스크 삭제 |
| `complete_task(task_id)` | 태스크 완료 처리 |
| `get_pending_tasks()` | 미완료 태스크 목록 |
| `get_done_tasks()` | 완료된 태스크 목록 |

## 5교시 실습 연결 포인트

이 코드를 사용해서 다음을 실습합니다.

- **스킬**: `/task-review`, `/task-test`, `/task-commit` 스킬 만들기
- **훅**: `task_manager.py` 수정 후 pytest 자동 실행
- **MCP**: 이 디렉토리를 MCP 서버로 등록해서 에이전트가 파일 접근
- **서브에이전트**: 이 프로젝트의 테스트 커버리지 분석 위임
