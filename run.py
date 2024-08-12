class ToDoList:
    """Manages the To-Do List."""

    def __init__(self):
        """Initializes an empty list to store tasks."""
        self.tasks = []


    def add_task(self, task):
        """Adds a new task to the tasks list."""
        self.tasks.append({"task": task, "completed": False})