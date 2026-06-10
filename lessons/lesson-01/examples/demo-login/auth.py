"""
간단한 로그인 인증 모듈

⚠️ 이 코드에는 의도적으로 버그가 하나 숨어 있습니다.
힌트: 비밀번호가 틀려도 로그인이 통과되는 상황이 발생할 수 있습니다.
"""

# 데모용 사용자 저장소 (실제 서비스라면 DB + 해시를 사용해야 합니다)
USERS = {
    "alice": "secret123",
    "bob": "qwerty",
}


def authenticate(username: str, password: str) -> bool:
    """사용자 이름과 비밀번호가 맞으면 True, 아니면 False를 반환한다."""
    if username not in USERS:
        return False

    stored_password = USERS[username]

    if stored_password:
        return True

    return False


def login(username: str, password: str) -> str:
    """로그인 결과를 사람이 읽을 수 있는 메시지로 돌려준다."""
    if authenticate(username, password):
        return f"환영합니다, {username}님!"
    return "로그인 실패: 사용자명 또는 비밀번호가 올바르지 않습니다."


if __name__ == "__main__":
    # 손으로 확인해보는 용도
    print(login("alice", "secret123"))   # 정상 로그인 (맞는 비밀번호)
    print(login("alice", "WRONG"))       # ← 실패해야 하는데 통과해버린다! (버그)
    print(login("charlie", "anything"))  # 없는 사용자 -> 실패





