# To-Do List Python Project

This is a simple Python project for managing a to-do list. You can add, remove, and view tasks.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setting Up the Project](#setting-up-the-project)
- [Running the To-Do List](#running-the-to-do-list)
- [Running the Tests](#running-the-tests)
- [Explanation of the Code](#explanation-of-the-code)
- [Using `.gitignore`](#using-gitignore)
- [Additional Resources](#additional-resources)

## Prerequisites

- [Python](https://www.python.org/downloads/) installed on your system

## Project Structure

The project has the following structure:

```
todo-list/
│
├── .gitignore
├── todo.py
├── test_todo.py
└── README.md
```

- `todo.py`: The main Python script that implements the to-do list functionality.
- `test_todo.py`: Unit tests for the to-do list functions.
- `.gitignore`: A file specifying which files and directories to ignore in the Git repository.
- `README.md`: A comprehensive tutorial on how to set up and run the to-do list project.

## Setting Up the Project

1. **Clone the Repository**

   First, clone the repository to your local machine. Open your terminal and run the following command:

   ```sh
   git clone https://github.com/your-username/todo-list.git
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```sh
   cd todo-list
   ```

## Running the To-Do List

To run the to-do list, execute the following command in your terminal:

```sh
python todo.py
```

Follow the prompts to add, remove, or view tasks.

## Running the Tests

To run the unit tests for the to-do list functions, execute the following command in your terminal:

```sh
python -m unittest test_todo.py
```

You should see output indicating that the tests passed.

## Explanation of the Code

### `todo.py`

The `todo.py` script defines a `TodoList` class with methods for adding, removing, and getting tasks. The script also handles user input to manage the to-do list interactively.

### `test_todo.py`

The `test_todo.py` script contains unit tests for the `TodoList` class methods (`add_task()`, `remove_task()`, `get_tasks()`). It uses the `unittest` framework to assert expected results against actual method outputs.

## Using `.gitignore`

The `.gitignore` file specifies files and directories that Git should ignore, such as temporary files, build artifacts, and environment-specific directories.

Here are some common entries in the `.gitignore` file:

- `__pycache__/`: Python's bytecode cache directory
- `*.pyc`: Compiled Python files
- `venv/`, `env/`: Virtual environment directories

## Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [unittest Documentation](https://docs.python.org/3/library/unittest.html)