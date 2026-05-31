"""
auth 모듈 테스트

실행:
    pytest test_auth.py -v
"""

from auth import authenticate


def test_correct_password():
    """맞는 비밀번호는 통과해야 한다."""
    assert authenticate("alice", "secret123") is True


def test_wrong_password():
    """틀린 비밀번호는 거부되어야 한다. (← 버그 때문에 처음엔 실패)"""
    assert authenticate("alice", "WRONG") is False


def test_unknown_user():
    """없는 사용자는 거부되어야 한다."""
    assert authenticate("charlie", "anything") is False
