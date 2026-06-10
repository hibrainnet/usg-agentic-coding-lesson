"""
task_manager.py 테스트
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


def test_delete_task_returns_false_for_missing():
    """존재하지 않는 ID로 삭제하면 False를 반환해야 한다."""
    result = task_manager.delete_task(999)
    assert result is False


# ── get_pending_tasks / get_done_tasks 테스트 ───────────────────────────────

def test_get_pending_tasks_returns_undone():
    task_manager.add_task("미완료")
    assert len(task_manager.get_pending_tasks()) == 1


def test_get_done_tasks_returns_empty_initially():
    task_manager.add_task("태스크")
    assert task_manager.get_done_tasks() == []


# ── complete_task 테스트 ────────────────────────────────────────────────────
# 실습 1에서 직접 작성합니다.
