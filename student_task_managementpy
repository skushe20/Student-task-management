import tkinter as tk
from tkinter import messagebox

# Store all tasks in a list
tasks = []


# Create the main window
root = tk.Tk()
root.title("Student Task Management")
root.geometry("650x550")
root.config(bg="lavender")


# Heading
heading = tk.Label(
    root,
    text="Welcome to Student Task Manager",
    font=("Arial", 18, "bold"),
    bg="lavender",
    fg="purple"
)
heading.pack(pady=15)


# Input boxes
tk.Label(root, text="Task Name:", bg="lavender").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Deadline:", bg="lavender").pack()
date_entry = tk.Entry(root, width=30)
date_entry.pack(pady=5)


# List to display tasks
task_list = tk.Listbox(root, width=65, height=12)
task_list.pack(pady=10)


# Display all tasks
def view_tasks():
    task_list.delete(0, tk.END)

    for i, task in enumerate(tasks, start=1):
        task_list.insert(
            tk.END,
            str(i) + ". " + task["name"] + " | "
            + task["deadline"] + " | " + task["status"]
        )


# Create a new task
def create_task():
    name = name_entry.get()
    deadline = date_entry.get()

    if name == "" or deadline == "":
        messagebox.showwarning("Warning", "Enter all details")
    else:
        task = {
            "name": name,
            "deadline": deadline,
            "status": "Pending"
        }

        tasks.append(task)
        view_tasks()

        name_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Task created!")


# Update a selected task
def update_task():
    selected = task_list.curselection()

    if selected:
        number = selected[0]

        name = name_entry.get()
        deadline = date_entry.get()

        if name == "" or deadline == "":
            messagebox.showwarning(
                "Warning", "Enter new task name and deadline"
            )
        else:
            tasks[number]["name"] = name
            tasks[number]["deadline"] = deadline
            view_tasks()
            messagebox.showinfo("Success", "Task updated!")
    else:
        messagebox.showwarning("Warning", "Select a task first")


# Mark a task as completed
def complete_task():
    selected = task_list.curselection()

    if selected:
        number = selected[0]
        tasks[number]["status"] = "Completed"
        view_tasks()
        messagebox.showinfo("Success", "Task completed!")
    else:
        messagebox.showwarning("Warning", "Select a task first")


# Fill input boxes when a task is selected
def select_task(event):
    selected = task_list.curselection()

    if selected:
        number = selected[0]

        name_entry.delete(0, tk.END)
        name_entry.insert(0, tasks[number]["name"])

        date_entry.delete(0, tk.END)
        date_entry.insert(0, tasks[number]["deadline"])


task_list.bind("<<ListboxSelect>>", select_task)


# Buttons
tk.Button(
    root, text="Create Task",
    command=create_task, bg="lightblue", width=15
).pack(pady=3)

tk.Button(
    root, text="Update Task",
    command=update_task, bg="lightgreen", width=15
).pack(pady=3)

tk.Button(
    root, text="View Tasks",
    command=view_tasks, bg="lightyellow", width=15
).pack(pady=3)

tk.Button(
    root, text="Complete Task",
    command=complete_task, bg="pink", width=15
).pack(pady=3)


# Thank-you message when the window is closed
def close_app():
    messagebox.showinfo(
        "Thank You",
        "Thank you for using Student Task Manager!"
    )
    root.destroy()


root.protocol("WM_DELETE_WINDOW", close_app)

# Run the application
root.mainloop() 
