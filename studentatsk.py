tasks = []
def create_task():
 name = input("Enter task name: ").strip()
 if name:
 tasks.append({"name": name, "status": "Pending"})
 print("Task added successfully!")
 else:
 print("Task name cannot be empty.")
def update_task():
 view_tasks()
 if not tasks:
 return
 try:
 number = int(input("Enter task number to update: "))
 if 1 <= number <= len(tasks):
 new_name = input("Enter new task name: ").strip()
 if new_name:
 tasks[number - 1]["name"] = new_name
 print("Task updated successfully!")
 else:
 print("Task name cannot be empty.")
 else:
 print("Invalid task number.")
 except ValueError:
 print("Please enter a valid number.")
def view_tasks():
 if not tasks:
 print("No tasks available.")
 return
 print("\nCurrent tasks:")
 for i, task in enumerate(tasks, start=1):
 print(f"{i}. {task['name']} [{task['status']}]")
def complete_task():
 view_tasks()
 if not tasks:
 return
 try:
 number = int(input("Enter task number to complete: "))
 if 1 <= number <= len(tasks):
 tasks[number - 1]["status"] = "Completed"
 print("Task marked as completed!")
 else:
 print("Invalid task number.")
 except ValueError:
 print("Please enter a valid number.")
while True:
 print("\n===== STUDENT TASK MANAGEMENT =====")
 print("1. Create task")
 print("2. Update task")
 print("3. View tasks")
 print("4. Complete task")
 print("5. Exit")
 choice = input("Enter choice: ")
 if choice == "1":
 create_task()
 elif choice == "2":
 update_task()
 elif choice == "3":
 view_tasks()
 elif choice == "4":
 complete_task()
 elif choice == "5":
 print("Thank you!")
 break
 else:
 print("Invalid choice. Try again.")

           
