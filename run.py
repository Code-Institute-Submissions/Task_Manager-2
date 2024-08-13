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

if __name__ == "__main__":
    # Create an instance of ToDoList
    todo = ToDoList()

    # Add tasks and print the list to verify
    todo.add_task("Buy groceries")
    todo.add_task("Read a book")
    print(todo.get_tasks())  # Test that tasks are added

    # Complete a task and print the list again
    todo.complete_task(1)
    print(todo.get_tasks())  # Test that the task is marked as completed

    # Delete a task and print the list again
    todo.delete_task(2)
    print(todo.get_tasks())  # Test that the task is deleted


import json  # Import the JSON module to handle data storage

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

if __name__ == "__main__":
    todo = ToDoList()
    load_tasks(todo)

    # Add tasks, complete one, delete one, then save
    todo.add_task("Buy groceries")
    todo.add_task("Read a book")
    todo.complete_task(1)
    save_tasks(todo)  # Save current state

    # Load tasks to verify persistence
    todo = ToDoList()  # Start fresh
    load_tasks(todo)
    print(todo.get_tasks())  # Check that saved tasks are loaded correctly

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

