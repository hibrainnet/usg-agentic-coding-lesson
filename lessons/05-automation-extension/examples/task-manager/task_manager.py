"""
태스크 관리 앱 (5교시 실습용 — 4교시 완성본)
"""

tasks = []


def add_task(title):
    if not title or not title.strip():
        raise ValueError("태스크 제목은 비어 있을 수 없습니다.")
    task_id = tasks[-1]["id"] + 1 if tasks else 1
    task = {"id": task_id, "title": title, "done": False}
    tasks.append(task)
    return task


def get_tasks():
    return tasks


def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return True
    return False


def complete_task(task_id):
    task = get_task(task_id)
    if task is None:
        return None
    task["done"] = True
    return task


def get_pending_tasks():
    return [task for task in tasks if not task["done"]]


def get_done_tasks():
    return [task for task in tasks if task["done"]]


def main():
    print("=== 태스크 관리 앱 ===")
    while True:
        print("\n1. 태스크 추가")
        print("2. 태스크 목록")
        print("3. 태스크 완료 처리")
        print("4. 태스크 삭제")
        print("5. 완료된 태스크 보기")
        print("6. 미완료 태스크 보기")
        print("0. 종료")

        choice = input("\n선택: ").strip()

        if choice == "1":
            title = input("태스크 제목: ").strip()
            try:
                task = add_task(title)
                print(f"추가됨: [{task['id']}] {task['title']}")
            except ValueError as e:
                print(f"오류: {e}")

        elif choice == "2":
            all_tasks = get_tasks()
            if not all_tasks:
                print("태스크가 없습니다.")
            else:
                for task in all_tasks:
                    status = "✓" if task["done"] else "○"
                    print(f"  {status} [{task['id']}] {task['title']}")

        elif choice == "3":
            try:
                task_id = int(input("완료 처리할 태스크 ID: "))
            except ValueError:
                print("올바른 ID를 입력해주세요.")
                continue
            result = complete_task(task_id)
            if result:
                print(f"완료 처리했습니다: [{result['id']}] {result['title']}")
            else:
                print("해당 태스크를 찾을 수 없습니다.")

        elif choice == "4":
            try:
                task_id = int(input("삭제할 태스크 ID: "))
            except ValueError:
                print("올바른 ID를 입력해주세요.")
                continue
            result = delete_task(task_id)
            if result:
                print("삭제했습니다.")
            else:
                print("해당 태스크를 찾을 수 없습니다.")

        elif choice == "5":
            done = get_done_tasks()
            if not done:
                print("완료된 태스크가 없습니다.")
            else:
                for task in done:
                    print(f"  ✓ [{task['id']}] {task['title']}")

        elif choice == "6":
            pending = get_pending_tasks()
            if not pending:
                print("미완료 태스크가 없습니다.")
            else:
                for task in pending:
                    print(f"  ○ [{task['id']}] {task['title']}")

        elif choice == "0":
            print("종료합니다.")
            break

        else:
            print("올바른 메뉴를 선택해주세요.")


if __name__ == "__main__":
    main()
