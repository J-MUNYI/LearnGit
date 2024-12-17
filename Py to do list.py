class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, priority):
        """Add a new task with a given priority"""
        self.tasks.append({"task": task_name, "priority": priority})

    def remove_task(self, task_name):
        """Remove a task by name"""
        self.tasks = [task for task in self.tasks if task["task"] != task_name]

    def view_tasks(self):
        """View all tasks sorted by priority (highest first)"""
        sorted_tasks = sorted(self.tasks, key=lambda x: x["priority"], reverse=True)
        if not sorted_tasks:
            print("No tasks to display.")
        else:
            print("\nTo-Do List:")
            for task in sorted_tasks:
                print(f"Task: {task['task']} | Priority: {task['priority']}")

    def update_priority(self, task_name, new_priority):
        """Update the priority of a task"""
        for task in self.tasks:
            if task["task"] == task_name:
                task["priority"] = new_priority
                print(f"Priority for '{task_name}' updated to {new_priority}.")
                return
        print(f"Task '{task_name}' not found!")

# Example Usage
def main():
    todo_list = TodoList()

    while True:
        print("\n--- Todo List Menu ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Update Task Priority")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            priority = int(input("Enter priority (1 - highest, 5 - lowest): "))
            todo_list.add_task(task_name, priority)
        elif choice == "2":
            task_name = input("Enter task name to remove: ")
            todo_list.remove_task(task_name)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            task_name = input("Enter task name to update priority: ")
            new_priority = int(input("Enter new priority (1 - highest, 5 - lowest): "))
            todo_list.update_priority(task_name, new_priority)
        elif choice == "5":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
