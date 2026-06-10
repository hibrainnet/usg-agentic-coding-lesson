"""
todo 모듈 테스트

실행:
    pytest test_todo.py -v
"""

import os
import pytest
from todo import add_todo, complete_todo, load_todos

DATA_FILE = "todos.json"


def setup_function():
    """테스트 전 데이터 파일 초기화."""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)


def test_add_todo():
    add_todo("우유 사기")
    todos = load_todos()
    assert len(todos) == 1
    assert todos[0]["text"] == "우유 사기"
    assert todos[0]["done"] is False


def test_complete_todo_marks_done():
    """1번 항목을 완료 처리하면 done이 True가 되어야 한다."""
    add_todo("우유 사기")
    add_todo("빵 사기")
    complete_todo(1)
    todos = load_todos()
    assert todos[0]["done"] is True


def test_complete_todo_invalid_number():
    """범위를 벗어난 번호는 목록을 변경하지 않는다."""
    add_todo("우유 사기")
    complete_todo(99)
    todos = load_todos()
    assert todos[0]["done"] is False
