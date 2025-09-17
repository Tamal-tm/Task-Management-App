def task():
    tasks=[] # empty list to store tasks
    print("Welcome to Task Management App")

    while True:
        try:
            total_task = int(input("Enter how many tasks you want to add: "))  # 5
            break
        except ValueError:
            print("Please enter a valid number!")
        
    for i in range(1, total_task+1): # 6
        task_name=input(f"Enter task {i} = ")
        tasks.append(task_name)
    print(f"\nToday's task are\n {tasks}")

    while True: # Menu Loop
        try:
            operation = int(input("\nEnter Your Choice:\n1. Add\n2. Update\n3. Delete\n4. View\n5. Exit/Stop\n-------> "))
            if operation == 1:
                add =input("Enter the task you want to add: ")
                tasks.append(add)
                print(f"Task {add} has been successfully added.")

            elif operation == 2:
                updated_val=input("Enter the task name you want to upodate: ")
                if updated_val in tasks:
                    update=input("Enter new task: ")
                    index = tasks.index(updated_val) # 2
                    tasks[index]=update
                    print(f"Updates task {update}")

            elif operation == 3:
                del_val= input("Which task you want to delete?: ")
                if del_val in tasks:
                    index=tasks.index(del_val)
                    del tasks[index]
                    print(f"Task {del_val} has been deleted.")
            
            elif operation == 4:
                print(f"Total tasks = {tasks}")
            
            elif operation == 5:
                print("Closing the Program")
                break
            
            else:
                print("Invalid Input. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

task()