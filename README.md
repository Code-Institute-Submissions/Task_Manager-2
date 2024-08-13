# To-Do List Manager
## Overview
The To-Do List Manager is a simple command-line application written in Python that allows users to manage their daily tasks efficiently. With this tool, users can add new tasks, mark tasks as completed, delete tasks, and save their tasks to a file. The application is designed to be easy to use, making it a perfect tool for anyone who wants to stay organized.

## Features
- Add New Tasks: Easily add new tasks to your to-do list.
- View All Tasks: View all tasks with their status (Pending or Done).
- Mark Tasks as Completed: Mark tasks as completed to track progress.
- Delete Tasks: Remove tasks that are no longer needed.
- Save and Load Tasks: Save tasks to a file and load them when you start the application.

## Technologies Used
Python: The application is written entirely in Python.
JSON: Used to save and load tasks from a file.


## Instructions & Usage
When you run the application, you will be presented with a menu that allows you to:

1. View all tasks: See the full list of tasks and their statuses.
2. Add a new task: Add a new task to the list.
3. Complete a task: Mark a task as completed.
4. Remove a task: Delete a task from the list.
5. Save and exit: Save your current tasks and exit the application.

## Example Usage

To-Do List Manager
1. View all tasks
2. Add a new task
3. Complete a task
4. Remove a task
5. Save and exit
Choose an option: 1

1. Buy groceries [Pending]
2. Clean the house [Done]

Choose an option: 3
Enter the task number to mark as completed: 1

Task marked as completed!
Saving and Loading Tasks

Saving Tasks: When you choose the "Save and exit" option, your tasks will be saved to tasks.json in the project directory.

Loading Tasks: When you start the application, it will automatically load any previously saved tasks from tasks.json.

## Testing
The following methods were used to test the application:

1. Manual Testing
Each function in the To-Do List Manager was manually tested to ensure correct functionality. The following scenarios were covered:

- Adding Tasks: Verified that new tasks are correctly added to the list and are marked as pending.
- Viewing Tasks: Ensured that all tasks are displayed with the correct status.
- Completing Tasks: Confirmed that marking a task as completed updates its status accordingly.
- Deleting Tasks: Checked that deleting a task removes it from the list.
- Saving Tasks: Verified that tasks are saved to the tasks.json file.
- Loading Tasks: Ensured that tasks are correctly loaded from the tasks.json file on startup.

2. Edge Case Testing
The application was tested for edge cases, including:

- Empty Input: Tested how the application handles empty task descriptions.
- Invalid Input: Tested how the application handles invalid task numbers (e.g., out-of-range numbers or non-integer input).
- File Handling: Checked the behavior when the tasks.json file is missing or corrupt.

3. Code Validation
- PEP8 Compliance: The code was run through a PEP8 linter to ensure it follows Python’s style guidelines.
- Error Handling: Ensured that appropriate error handling is in place for invalid inputs and file operations.

4. Functional Testing
- To verify the overall functionality, the application was run multiple times with various tasks added, completed, and deleted. Tasks were saved and loaded to ensure data persistence.

5. Errors Found in PEP8
- Add a second blank line where required.
- Remove any trailing whitespace on blank lines.
- Break up any lines that exceed 79 characters.
- Remove the blank line at the end of the file.

## Deployment
This project is deployed using code institutes mock terminal for Heroku. 

- Steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildbacks to Python and NodeJS in that order
  - Link the Heroku app to the respository
  - Click on Deploy


## Project Goals
Modularity: Each function in the code is designed to perform a single task, making the codebase easy to understand and maintain.

User Experience: The application provides clear instructions and feedback to the user at every step.

## Future Improvements
- Search and Filter: Add the ability to search for tasks or filter tasks by their status.
- Due Dates: Allow users to assign due dates to tasks and notify them of upcoming deadlines.
- Recurring Tasks: Support for recurring tasks that reset after a certain period.

Acknowledgments
Special thanks to the Code Institute for providing the framework and guidelines for this project.
Inspiration for this project was drawn from various task management tools, as well as the Love Sandwhich Project.
