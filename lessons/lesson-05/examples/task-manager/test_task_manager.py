"""
task_manager.py 테스트 (5교시 실습용 — 4교시 완성본)
"""

import pytest
import task_manager


@pytest.fixture(autouse=True)
def clear_tasks():
    """각 테스트 전에 tasks 리스트를 초기화한다."""
    task_manager.tasks.clear()
    yield
    task_manager.tasks.clear()


# ── add_task 테스트 ─────────────────────────────────────────────────────────

def test_add_task_returns_task():
    task = task_manager.add_task("첫 번째 태스크")
    assert task["title"] == "첫 번째 태스크"
    assert task["done"] is False


def test_add_task_assigns_id_1_when_empty():
    """비어있는 목록에 첫 태스크를 추가하면 id가 1이어야 한다."""
    task = task_manager.add_task("첫 태스크")
    assert task["id"] == 1


def test_add_task_increments_id():
    """두 번째 태스크는 id가 2여야 한다."""
    task_manager.add_task("첫 번째")
    task2 = task_manager.add_task("두 번째")
    assert task2["id"] == 2


def test_add_task_empty_title_raises():
    """빈 제목으로 태스크를 추가하면 ValueError가 발생해야 한다."""
    with pytest.raises(ValueError):
        task_manager.add_task("")


def test_add_task_whitespace_only_raises():
    """공백만 있는 제목도 ValueError가 발생해야 한다."""
    with pytest.raises(ValueError):
        task_manager.add_task("   ")


# ── get_tasks 테스트 ────────────────────────────────────────────────────────

def test_get_tasks_returns_empty_list():
    assert task_manager.get_tasks() == []


def test_get_tasks_returns_all():
    task_manager.add_task("A")
    task_manager.add_task("B")
    assert len(task_manager.get_tasks()) == 2


# ── get_task 테스트 ─────────────────────────────────────────────────────────

def test_get_task_returns_correct_task():
    task_manager.add_task("찾을 태스크")
    task = task_manager.get_task(1)
    assert task["title"] == "찾을 태스크"


def test_get_task_returns_none_for_missing():
    result = task_manager.get_task(999)
    assert result is None


# ── delete_task 테스트 ──────────────────────────────────────────────────────

def test_delete_task_removes_task():
    task_manager.add_task("삭제할 태스크")
    task_manager.delete_task(1)
    assert task_manager.get_task(1) is None


def test_delete_task_returns_true_on_success():
    task_manager.add_task("삭제할 태스크")
    result = task_manager.delete_task(1)
    assert result is True


def test_delete_task_returns_false_for_missing():
    """존재하지 않는 ID로 삭제하면 False를 반환해야 한다."""
    result = task_manager.delete_task(999)
    assert result is False


# ── complete_task 테스트 ────────────────────────────────────────────────────

def test_complete_task_sets_done_true():
    """존재하는 태스크를 완료 처리하면 done이 True가 된다."""
    task_manager.add_task("완료할 태스크")
    result = task_manager.complete_task(1)
    assert result["done"] is True


def test_complete_task_returns_task():
    """완료 처리 시 태스크 딕셔너리를 반환해야 한다."""
    task_manager.add_task("완료할 태스크")
    result = task_manager.complete_task(1)
    assert result["id"] == 1
    assert result["title"] == "완료할 태스크"


def test_complete_task_returns_none_for_missing():
    """존재하지 않는 id로 호출하면 None을 반환한다."""
    result = task_manager.complete_task(999)
    assert result is None


# ── get_pending_tasks / get_done_tasks 테스트 ───────────────────────────────

def test_get_pending_tasks_returns_undone():
    task_manager.add_task("미완료")
    assert len(task_manager.get_pending_tasks()) == 1


def test_get_pending_tasks_excludes_completed():
    """완료된 태스크는 미완료 목록에 포함되지 않아야 한다."""
    task_manager.add_task("태스크1")
    task_manager.add_task("태스크2")
    task_manager.complete_task(1)
    pending = task_manager.get_pending_tasks()
    assert len(pending) == 1
    assert pending[0]["id"] == 2


def test_get_done_tasks_returns_empty_initially():
    task_manager.add_task("태스크")
    assert task_manager.get_done_tasks() == []


def test_get_done_tasks_returns_completed():
    """완료 처리한 태스크가 완료 목록에 포함되어야 한다."""
    task_manager.add_task("태스크1")
    task_manager.add_task("태스크2")
    task_manager.complete_task(1)
    done = task_manager.get_done_tasks()
    assert len(done) == 1
    assert done[0]["id"] == 1
