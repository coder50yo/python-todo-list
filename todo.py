# todo.py

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append(task)
            return True
        return False

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False

    def get_tasks(self):
        return self.tasks

if __name__ == "__main__":
    todo_list = TodoList()
    
    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            task = input("Enter a new task: ")
            if todo_list.add_task(task):
                print(f"Task '{task}' added.")
            else:
                print("Failed to add task.")
        elif choice == '2':
            task = input("Enter the task to remove: ")
            if todo_list.remove_task(task):
                print(f"Task '{task}' removed.")
            else:
                print("Failed to remove task.")
        elif choice == '3':
            tasks = todo_list.get_tasks()
            if tasks:
                print("Your tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks found.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
