"""
간단한 주소록 CLI

사용법:
    python3 contacts.py add <이름> <전화번호> [이메일]
    python3 contacts.py list
    python3 contacts.py search <키워드>
    python3 contacts.py delete <ID>
"""

import sys
from storage import load_contacts, save_contacts


def add_contact(name: str, phone: str, email: str = "") -> None:
    """새 연락처를 추가한다."""
    contacts = load_contacts()
    new_id = max((c["id"] for c in contacts), default=0) + 1
    contacts.append({"id": new_id, "name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"추가됨: [{new_id}] {name} ({phone})")


def list_contacts() -> None:
    """저장된 모든 연락처를 출력한다."""
    contacts = load_contacts()
    if not contacts:
        print("저장된 연락처가 없습니다.")
        return
    for c in contacts:
        email_str = f" / {c['email']}" if c.get("email") else ""
        print(f"[{c['id']}] {c['name']} — {c['phone']}{email_str}")


def search_contacts(keyword: str) -> None:
    """이름 또는 전화번호에서 키워드로 검색한다."""
    contacts = load_contacts()
    results = [
        c for c in contacts
        if keyword in c["name"] or keyword in c["phone"]
    ]
    if not results:
        print(f"'{keyword}'에 해당하는 연락처가 없습니다.")
        return
    for c in results:
        email_str = f" / {c['email']}" if c.get("email") else ""
        print(f"[{c['id']}] {c['name']} — {c['phone']}{email_str}")


def delete_contact(contact_id: int) -> None:
    """ID에 해당하는 연락처를 삭제한다."""
    contacts = load_contacts()
    original_count = len(contacts)
    contacts = [c for c in contacts if c["id"] != contact_id]
    if len(contacts) == original_count:
        print(f"오류: ID {contact_id}에 해당하는 연락처가 없습니다.")
        return
    save_contacts(contacts)
    print(f"삭제됨: ID {contact_id}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python3 contacts.py [add|list|search|delete] [인수]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print("사용법: python3 contacts.py add <이름> <전화번호> [이메일]")
        else:
            email = sys.argv[4] if len(sys.argv) > 4 else ""
            add_contact(sys.argv[2], sys.argv[3], email)
    elif command == "list":
        list_contacts()
    elif command == "search":
        if len(sys.argv) < 3:
            print("사용법: python3 contacts.py search <키워드>")
        else:
            search_contacts(sys.argv[2])
    elif command == "delete":
        if len(sys.argv) < 3:
            print("사용법: python3 contacts.py delete <ID>")
        else:
            delete_contact(int(sys.argv[2]))
    else:
        print(f"알 수 없는 명령: {command}")
        print("사용법: python3 contacts.py [add|list|search|delete] [인수]")
