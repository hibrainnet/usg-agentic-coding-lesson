"""
태스크 관리 앱 (실습용)
"""

tasks = []


def add_task(title):
    # BUG 1: tasks가 비어있을 때 tasks[-1]에 접근하면 IndexError 발생
    task_id = tasks[-1]["id"] + 1
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
    # BUG 3: 존재하지 않는 ID를 삭제해도 성공 메시지 출력 (실제 삭제 없음)
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return True
    return True  # 없는 ID도 True 반환 (버그)


def get_pending_tasks():
    return [task for task in tasks if not task["done"]]


def get_done_tasks():
    return [task for task in tasks if task["done"]]


def main():
    print("=== 태스크 관리 앱 ===")
    while True:
        print("\n1. 태스크 추가")
        print("2. 태스크 목록")
        print("3. 태스크 삭제")
        print("4. 완료된 태스크 보기")
        print("0. 종료")

        choice = input("\n선택: ").strip()

        if choice == "1":
            title = input("태스크 제목: ").strip()
            # BUG 2: 빈 제목 검증 없음 — 빈 문자열 태스크가 추가됨
            task = add_task(title)
            print(f"추가됨: [{task['id']}] {task['title']}")

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
                task_id = int(input("삭제할 태스크 ID: "))
            except ValueError:
                print("올바른 ID를 입력해주세요.")
                continue
            result = delete_task(task_id)
            if result:
                print("삭제했습니다.")

        elif choice == "4":
            done = get_done_tasks()
            if not done:
                print("완료된 태스크가 없습니다.")
            else:
                for task in done:
                    print(f"  ✓ [{task['id']}] {task['title']}")

        elif choice == "0":
            print("종료합니다.")
            break

        else:
            print("올바른 메뉴를 선택해주세요.")


if __name__ == "__main__":
    main()
