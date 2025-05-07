# Command-Line To-Do List Manager

#### Video Demo:  [Live Demo](https://youtu.be/BJKQr8R4tG4)

#### Description:

The **Command-Line To-Do List Manager** is a Python-based application that allows users to manage their daily tasks from the terminal in a fast, simple, and engaging way. Designed to be intuitive and lightweight, it enables users to add tasks, view their to-do list, mark items as completed, delete unwanted tasks, and even save their progress to a file for future reference.

This project was created as a personal productivity tool and an exercise in building a command-line interface (CLI) with a clean and responsive design. The addition of friendly feedback messages and emoji-based UI elements makes it both practical and enjoyable to use.

---

## 📁 Project Structure and File Descriptions
```bash
project/
├── project.py
├── test_project.py
├── requirements.txt
└── README.md
```

### `project.py`

This is the main script and contains all the code for the project. It features a simple yet powerful menu-driven loop that accepts the following commands:

- **A** (Add a task): Prompts the user to input a task and adds it to the list with a default status of `pending`.
- **D** (Delete a task): Displays the current list and lets the user remove a task by its number.
- **M** (Mark a task as done): Lets the user mark any listed task as `done`, visually confirmed with a ✅.
- **V** (View tasks): Shows the current list, formatted with icons to indicate task status.
- **S** (Save): Saves the current to-do list to a local file (`todo-list.txt`) in a clean, readable format.
- **E** (Exit): Ends the session with a thank-you message.

Each of these commands is tied to a specific function in the file:
- `add(task)` adds a new dictionary object to the `database` list.
- `delete(i)` removes an item from the list using `pop()`, after validating the index.
- `display()` formats and prints the list using checkboxes for better clarity.
- `save()` writes the list to a file with index numbers and task statuses.

All tasks are stored temporarily in the global `database` list during the session.

### `test_project.py`

This file contains unit tests written using `pytest`. Each test resets the database and verifies the functionality of:
- Adding tasks
- Deleting tasks
- Marking tasks as done
- Saving tasks to `todo-list.txt`
- Display output

This test suite ensures that each function behaves correctly and that the app handles edge cases, such as invalid input or out-of-range deletions.

### `requirements.txt`

This file lists the project’s Python dependencies:

`tabulate`
`pytest`


---

## 🧠 Design Choices

One deliberate choice was **not implementing persistent storage** (e.g., JSON, SQLite, or CSV) for simplicity. Instead, users are encouraged to manually save their progress using the 'S' key, which outputs a plain text file. This decision reflects the philosophy of building lightweight, modular tools that do one thing well.

To make the terminal interface more pleasant, we incorporated the [`tabulate`](https://pypi.org/project/tabulate/) library. While this introduces a single external dependency, it dramatically improves the visual structure of the help menu and makes the app more intuitive.

The decision to use emoji in output messages—such as ✅ for completed tasks and (˶ᵔ ᵕ ᵔ˶) in confirmation prompts—was based on a desire to create a tool that felt more friendly and modern. These touches improve user experience without compromising performance or simplicity.

We also implemented basic error handling for non-numeric input during deletion or marking tasks, which prevents crashes and provides user feedback to correct mistakes.

---

## 📄 Output File

When saved, the `todo-list.txt` file looks like this:
1. Exercise [DONE]
2. Walk my dog [DONE]
3. Study Python [PENDING]


This file is saved in the project root directory and overwrites itself each time the user saves.

---

## 📌 Possible Enhancements

If continued, this project could benefit from:
- Persistent data storage using a JSON file or SQLite.
- Task editing (rename or change status back to `pending`).
- Support for task priority levels or due dates.
- A GUI version using Tkinter or a web front end.
- Integration with notifications or calendar APIs.

---

## 🎓 Conclusion

This project demonstrates how a small, focused script can make managing daily tasks more efficient without needing a full-fledged application or internet connection. By blending simplicity with helpful UX design and terminal aesthetics, the To-Do List Manager offers a solid foundation for further development and customization.


