# todo.py

class ToDoList:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]
            return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List =====")
        print("I. Show Tasks\nII. Add Task\nIII. Remove Task\n0. Exit\n")

        choice = input("Enter your choice: ")

        if choice == 'I':
            todo_list.show_tasks()
        elif choice == 'II':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == 'III':
            todo_list.show_tasks()
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '0':
            print("Exiting the To-Do List application. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
