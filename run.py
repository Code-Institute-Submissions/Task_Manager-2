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
