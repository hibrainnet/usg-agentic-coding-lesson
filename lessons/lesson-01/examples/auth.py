USERS = {
    "alice": "secret123",
    "bob": "qwerty",
}

def authenticate(username: str, password: str) -> bool:
    if username not in USERS:
        return False
    
    stored_password = USERS[username]

    if stored_password:
        return True

    return False


def login(username: str, password: str) -> str:
    if authenticate(username, password):
        return f"환영합니다, {username}님!"
    return "로그인 실패: 사용자명 또는 비밀번호가 올바르지 않습니다."


