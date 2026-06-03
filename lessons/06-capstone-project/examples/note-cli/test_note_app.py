"""
note_app.py 테스트
"""

import pytest
import note_app


@pytest.fixture(autouse=True)
def clear_notes():
    """각 테스트 전후로 notes 리스트와 파일을 초기화한다."""
    note_app.notes.clear()
    yield
    note_app.notes.clear()


# ── add_note 테스트 ─────────────────────────────────────────────────────────

def test_add_note_returns_note():
    note = note_app.add_note("첫 번째 메모", "내용입니다")
    assert note["title"] == "첫 번째 메모"
    assert note["content"] == "내용입니다"


def test_add_note_assigns_id_1_when_empty():
    note = note_app.add_note("첫 번째", "내용")
    assert note["id"] == 1


def test_add_note_increments_id():
    note_app.add_note("첫 번째", "내용1")
    note2 = note_app.add_note("두 번째", "내용2")
    assert note2["id"] == 2


def test_add_note_empty_title_raises():
    """빈 제목이면 ValueError가 발생해야 한다."""
    with pytest.raises(ValueError):
        note_app.add_note("", "내용")


# ── get_notes 테스트 ────────────────────────────────────────────────────────

def test_get_notes_returns_empty_list():
    assert note_app.get_notes() == []


def test_get_notes_returns_all():
    note_app.add_note("A", "내용A")
    note_app.add_note("B", "내용B")
    assert len(note_app.get_notes()) == 2


# ── get_note 테스트 ─────────────────────────────────────────────────────────

def test_get_note_returns_correct_note():
    note_app.add_note("찾을 메모", "내용")
    note = note_app.get_note(1)
    assert note["title"] == "찾을 메모"


def test_get_note_returns_none_for_missing():
    result = note_app.get_note(999)
    assert result is None


# ── delete_note 테스트 ──────────────────────────────────────────────────────

def test_delete_note_removes_note():
    note_app.add_note("삭제할 메모", "내용")
    note_app.delete_note(1)
    assert note_app.get_note(1) is None


def test_delete_note_returns_true_on_success():
    note_app.add_note("메모", "내용")
    result = note_app.delete_note(1)
    assert result is True


def test_delete_note_returns_false_for_missing():
    """없는 ID 삭제는 False를 반환해야 한다."""
    result = note_app.delete_note(999)
    assert result is False


# ── search_notes 테스트 ─────────────────────────────────────────────────────

def test_search_notes_finds_by_title():
    note_app.add_note("Python 배우기", "파이썬 공부")
    note_app.add_note("점심 메뉴", "김치찌개")
    results = note_app.search_notes("Python")
    assert len(results) == 1
    assert results[0]["title"] == "Python 배우기"


def test_search_notes_finds_by_content():
    note_app.add_note("오늘 일기", "파이썬으로 프로젝트를 만들었다")
    results = note_app.search_notes("파이썬")
    assert len(results) == 1


def test_search_notes_case_insensitive():
    """대소문자를 구분하지 않아야 한다."""
    note_app.add_note("python study", "내용")
    results = note_app.search_notes("PYTHON")
    assert len(results) == 1


def test_search_notes_returns_empty_list_when_no_match():
    note_app.add_note("메모", "내용")
    results = note_app.search_notes("존재하지않는키워드")
    assert results == []
