"""
메모 관리 CLI 앱 (종합 프로젝트 시작 스캐폴드)

구현해야 할 함수:
  - add_note(title, content)
  - get_notes()
  - get_note(note_id)
  - delete_note(note_id)
  - search_notes(keyword)

이미 구현된 함수:
  - save_to_file() / load_from_file()  — JSON 파일 저장·불러오기
  - main()                              — CLI 메뉴 루프
"""

import json
import os

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.json")
notes = []


# ── 파일 저장·불러오기 (구현 완료) ─────────────────────────────────────────

def save_to_file():
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


def load_from_file():
    global notes
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            notes = json.load(f)
    else:
        notes = []


# ── 구현이 필요한 함수 ──────────────────────────────────────────────────────

def add_note(title, content):
    """메모를 추가하고 추가된 메모 딕셔너리를 반환한다.

    Args:
        title: 메모 제목 (빈 문자열이면 ValueError)
        content: 메모 내용

    Returns:
        {"id": int, "title": str, "content": str} 딕셔너리

    Raises:
        ValueError: title이 빈 문자열일 때
    """
    # TODO: 구현해주세요
    pass


def get_notes():
    """저장된 모든 메모 리스트를 반환한다."""
    # TODO: 구현해주세요
    pass


def get_note(note_id):
    """id에 해당하는 메모를 반환한다. 없으면 None을 반환한다."""
    # TODO: 구현해주세요
    pass


def delete_note(note_id):
    """id에 해당하는 메모를 삭제한다.

    Returns:
        True: 삭제 성공
        False: 해당 id가 없음
    """
    # TODO: 구현해주세요
    pass


def search_notes(keyword):
    """keyword가 title 또는 content에 포함된 메모 리스트를 반환한다.

    대소문자를 구분하지 않는다.
    결과가 없으면 빈 리스트를 반환한다.
    """
    # TODO: 구현해주세요
    pass


# ── CLI 메뉴 (구현 완료) ────────────────────────────────────────────────────

def main():
    load_from_file()
    print("=== 메모 앱 ===")

    while True:
        print("\n1. 메모 추가")
        print("2. 전체 메모 보기")
        print("3. 메모 검색")
        print("4. 메모 삭제")
        print("0. 종료")

        choice = input("\n선택: ").strip()

        if choice == "1":
            title = input("제목: ").strip()
            content = input("내용: ").strip()
            try:
                note = add_note(title, content)
                save_to_file()
                print(f"추가됨: [{note['id']}] {note['title']}")
            except ValueError as e:
                print(f"오류: {e}")

        elif choice == "2":
            all_notes = get_notes()
            if not all_notes:
                print("메모가 없습니다.")
            else:
                for note in all_notes:
                    print(f"  [{note['id']}] {note['title']}")
                    print(f"       {note['content'][:50]}{'...' if len(note['content']) > 50 else ''}")

        elif choice == "3":
            keyword = input("검색어: ").strip()
            results = search_notes(keyword)
            if not results:
                print(f"'{keyword}'에 해당하는 메모가 없습니다.")
            else:
                print(f"{len(results)}개 결과:")
                for note in results:
                    print(f"  [{note['id']}] {note['title']}")

        elif choice == "4":
            try:
                note_id = int(input("삭제할 메모 ID: "))
            except ValueError:
                print("올바른 ID를 입력해주세요.")
                continue
            if delete_note(note_id):
                save_to_file()
                print("삭제했습니다.")
            else:
                print("해당 ID의 메모가 없습니다.")

        elif choice == "0":
            print("종료합니다.")
            break

        else:
            print("올바른 메뉴를 선택해주세요.")


if __name__ == "__main__":
    main()
