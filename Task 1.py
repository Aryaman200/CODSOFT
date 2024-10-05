def run_app():
    todo_list = []

    while True:
        print("\n==== Task Manager ====")
        print("1. Add a new task")
        print("2. Display all tasks")
        print("3. Complete a task")
        print("4. Exit the program")

        user_input = input("Select an option (1-4): ")

        if user_input == '1':
            print()
            num_of_tasks = int(input("How many tasks do you want to add? "))

            for i in range(num_of_tasks):
                new_task = input(f"Enter task {i + 1}: ")
                todo_list.append({"description": new_task, "completed": False})
                print("Task added successfully!")

        elif user_input == '2':
            print("\nYour Tasks:")
            if not todo_list:
                print("No tasks available.")
            else:
                for idx, task in enumerate(todo_list):
                    status = "Completed" if task["completed"] else "Pending"
                    print(f"{idx + 1}. {task['description']} - {status}")

        elif user_input == '3':
            task_no = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_no < len(todo_list):
                todo_list[task_no]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number. Please try again.")

        elif user_input == '4':
            print("Closing the Task Manager. Goodbye!")
            break

        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    run_app()
