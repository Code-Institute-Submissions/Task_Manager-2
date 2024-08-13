import json  # Import the JSON module to handle data storage

class ToDoList:
    """Manages the To-Do List."""
    
    def __init__(self):
        """Initializes an empty list to store tasks."""
        self.tasks = []

    def add_task(self, task):
        """Adds a new task to the tasks list."""
        self.tasks.append({"task": task, "completed": False})

    def get_tasks(self):
        """Returns the list of tasks."""
        return self.tasks

    def complete_task(self, task_number):
        """Marks a task as completed by setting its 'completed' status to True."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True

    def delete_task(self, task_number):
        """Deletes a task from the tasks list."""
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]


def save_tasks(todo, filename="tasks.json"):
    """Saves the current list of tasks to a file in JSON format."""
    with open(filename, "w") as file:
        json.dump(todo.get_tasks(), file)

def load_tasks(todo, filename="tasks.json"):
    """Loads tasks from a file and adds them to the ToDoList instance."""
    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                todo.add_task(task['task'])
                if task['completed']:
                    todo.complete_task(len(todo.get_tasks()))
    except FileNotFoundError:
        print("No saved tasks found. Starting fresh.")


def display_tasks(todo):
    """Displays all tasks with their status (Pending or Done)."""
    tasks = todo.get_tasks()
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} [{status}]")

def add_new_task(todo):
    """Prompts the user to add a new task."""
    task = input("Enter a new task: ")
    todo.add_task(task)
    print("Task added!")

def mark_task_as_completed(todo):
    """Prompts the user to select a task to mark as completed."""
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        todo.complete_task(task_number)
        print("Task marked as completed!")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def remove_task(todo):
    """Prompts the user to select a task to delete."""
    try:
        task_number = int(input("Enter the task number to delete: "))
        todo.delete_task(task_number)
        print("Task deleted!")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def display_menu():
    """Displays the menu options to the user."""
    print("\nTo-Do List Manager")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Complete a task")
    print("4. Remove a task")
    print("5. Save and exit")


def main():
    """Main function to run the To-Do List application."""
    todo = ToDoList()  # Create an instance of ToDoList
    load_tasks(todo)  # Load tasks from file if available

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(todo)
        elif choice == "2":
            add_new_task(todo)
        elif choice == "3":
            mark_task_as_completed(todo)
        elif choice == "4":
            remove_task(todo)
        elif choice == "5":
            save_tasks(todo)  # Save tasks to file before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


