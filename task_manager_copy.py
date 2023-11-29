print("Welcome to the task manager login page!")
# import modules
import datetime
# New user registration function creation.
def reg_user(new_username, new_password, confirm_password):
    with open ('user.txt', 'r') as users:
        for lines in users:
            user_list = lines.split(",")
            if new_username == user_list[0]:
                print("Username already exists.Try a new one")
                break
            if new_password == confirm_password:
                print("Thank you!You have been registered.")
                break    
            else:
                print("Password confirmation did not match new password.Register again.")
                break

# cretae function to add new task to a txt file.
def add_task(txt_file_name = 'user.txt'):
    with open(txt_file_name, '+a') as tasks_page:
        tasks_page.write(f"\n{task_username}, {task_title}, {task_description}, {task_assign_date}, {task_due_date}, {task_completion}")
        
# Create function to view all tasks store in txt file
def view_all(txt_file_name = 'tasks.txt'):
    with open(txt_file_name, 'r') as tasks_page:
        for lines in tasks_page:
            task_line = lines.split(",")
            print(f'''Task information;
Assigned user: {task_line[0]}
Task title:{task_line[1]}
Task description:{task_line[2]}
Date assigned:{task_line[3]}
Due date:{task_line[4]}
Task completed:{task_line[5]}''')



# create a function to view only the users tasks and edit
def view_mine(txt_file_name = 'tasks.txt'):
        user_task_list = []
        with open(txt_file_name,'r+') as tasks_page:
            for i, lines in enumerate(tasks_page,1):
                task_line = lines.split(",")
                
                if username == task_line[0]:
                    user_task_list += [i]
                    print(f'''{i}
                        Task information;
                        Assigned user: {task_line[0]}
                        Task title:{task_line[1]}
                        Task description:{task_line[2]}
                        Date assigned:{task_line[3]}
                        Due date:{task_line[4]}
                        Task completed:{task_line[5]}''')
                    print(f"Select a corresponding task number({user_task_list}) for a task you would like to edit OR enter '-1' to reurn to main menu.")
            task_selection = int(input("Enter task selection:\n"))
            if task_selection in user_task_list:
                print('''Select an action by entering the corresponding number:
                        1 - Edit new assigned user to task.
                        2 - Edit completion status.
                        3 - Edit due date.''')
                edit_selection = input("Enter selection number:\n")
                if edit_selection == "1":
                    user_edit = input("Enter newly assigned user for task:\n")
                    with open('tasks.txt','r+') as tasks_page:
                        for lines in tasks_page:
                            task_line = lines.split(",")
                            task_line[0] = task_line[4].replace(task_line[0],user_edit)
                if edit_selection == "2":
                    completion_edit = input("Enter status of completion 'Yes' or 'No'")
                    with open('tasks.txt','r+'):
                        for lines in tasks_page:
                            task_line = lines.split(",")
                            task_line[5] = task_line[4].replace(task_line[5],completion_edit)
                if edit_selection == "3":
                    due_date_edit = input("Enter new date in format e.g 30 oct 2019")
                    with open('tasks.txt','r+'):
                        for lines in tasks_page:
                            task_line = lines.split(",")
                            task_line[4] = task_line[4].replace(task_line[4],due_date_edit)
            elif task_selection == "-1":
                    print("Returning to menu...")
            else:
                print("Invalid entry.")
# create a function that reads and seperates lines in a txt file to elements for task overview
def print_tasks_overview(file_path):
    line_count = 0
    completed_count = 0
    incomplete_count = 0
    current_date = datetime.datetime.today()
    overdue_count = 0
    not_overdue_count = 0
    incomplete_overdue_count = 0
    date_format = "%d %b %Y"
    try:
        with open(file_path, 'r+') as task_file:
            for task_lines in task_file:
                task_lines = task_lines.split(",")
                line_count += 1
                due_date_str = task_lines[4].strip()
                print(due_date_str)
                due_date = datetime.datetime.strptime(due_date_str, date_format)
                print(due_date)
                # working out completion counts
                if task_lines[5].strip() == "No":
                    incomplete_count += 1
                else:
                    completed_count += 1
                # working out date counts
                if due_date < current_date:
                    print(due_date)
                    overdue_count += 1
                if task_lines[5].strip() == "No" and due_date < current_date:
                    incomplete_overdue_count += 1
                else:
                    not_overdue_count += 1
            
            # Formulate overview statement
            percentage_incomplete = (incomplete_count/line_count) * 100
            percentage_incomplete_overdue = (incomplete_overdue_count/line_count) * 100
            percentage_overdue = (overdue_count/line_count) * 100
            with open('task_overview','w+') as task_overview_print:
                task_overview_print.write(f'''--Task overview--
            Total number of tasks logged: {line_count}
            Total number of completed tasks: {completed_count}
            Total number of uncompleted tasks: {incomplete_count}
            Total tasks uncompleted and overdue: {percentage_incomplete_overdue}%
            Percentage of incomplete tasks: {percentage_incomplete}%
            Percentage of tasks overdue: {percentage_overdue}%''')

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    
    
# create a function that reads and seperates lines in a txt file to elements for user overview
def user_overview_print(file_name):     
     file_name = 'user.txt'
     with open(file_name,'r+') as users:
            user_list_storage = []
            for line in users:
                login_entry = line.split(',')
                login_entry[1] = login_entry[1].strip()
                user_list_storage = user_list_storage + [login_entry[0]]
                task_list_storage = [0] * len(user_list_storage)
                total_tasks = 0
                completed_count = 0
                incomplete_count = 0
                overdue_count = 0
                not_overdue_count = 0
                current_date = datetime.datetime.today()
                incomplete_and_due_count = 0
            with open('tasks.txt','r') as tasks_page:
                for line in tasks_page:
                    task_string = line.split(',')  
                    user_index = user_list_storage.index(task_string[0])
                    user_tasks = task_list_storage[user_index]
                    task_list_storage[user_index] = user_tasks +1

                with open('user_overview.txt','w') as user_overview_page:
                    for i, user in enumerate(user_list_storage):
                        due_date_str = task_string[4].strip()
                        due_date = datetime.datetime.strptime(due_date_str, "%d %b %Y")
                        total_tasks += task_list_storage[i]
                        if task_string[5].strip() == "Yes":
                            completed_count += 1
                        elif task_string[5].strip() == "No":
                            incomplete_count += 1
                        
                        elif task_string[5].strip() == "No" and due_date < current_date:
                            incomplete_and_due_count += 1
                        
                        percentage_user_tasks = (task_list_storage[i]/total_tasks) * 100
                        percentage_user_completed = (completed_count/total_tasks) * 100
                        percentage_user_incomplete = 100 - (percentage_user_completed)
                        percentage_user_incomplete_overdue = (incomplete_and_due_count/total_tasks) * 100

                        user_overview_page.write(f'''---User overview---
                        Total users:{len(user_list_storage)}
                        Total tasks:{total_tasks}

                        {user}:
                        Total number of tasks assigned to user: {task_list_storage[i]}
                        Percentage of total number of tasks assigned to user: {percentage_user_tasks}%
                        Percentage of completed tasks assigned to user: {percentage_user_completed}
                        Percentage of incomplete tasks assigned to user: {percentage_user_incomplete}
                        Percentage of tasks incomplete and overdue by user: {percentage_user_incomplete_overdue}
                        ''')

# user login info acess and string manipulations for list formats
user_list_storage = []
password_list_storage = []
login_entry = []
with open('user.txt','r+') as users:
    for line in users:
        login_entry = line.split(',')
        login_entry[1] = login_entry[1].strip()
        user_list_storage = user_list_storage + [login_entry[0]]
        password_list_storage = password_list_storage + [login_entry[1]]
    print(user_list_storage)
    print(password_list_storage)

# Login verifications  
    while True: # while the conditions of a succesful login have not been met, loop continues.
        username = (input("Enter username: \n")).lower()
        password = (input("Enter password: \n")).lower()
        if username in user_list_storage:
            i = user_list_storage.index(username)
            if password == password_list_storage[i]:
                print("You have been succesfully authenticated.")
                break # stop the loop if all logins are correct.
            else:
                print("Incorrect password.Try again.")
        else:
            print("Incorrect username.Try again.")

# Menu selection options
while True:
    if username == "admin":
         menu = input('''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate reports              
        d - display task statistics              
        e - exit
        \n''').lower()

    else:
        menu = input('''Select one of the following options:
        r - register a user
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        \n''').lower()

# New user registartion
    if menu == "r":
        if username == "admin":
            new_username = input("Enter new username:\n")
            new_password = input("Enter new password:\n")
            confirm_password = input("Confirm new password: \n")  
            reg_user(new_username, new_password, confirm_password) #calling user registration function.
            break            
        else:
            print("Please note, only user with admin credintials is permitted to log a new user.")
        
# New task addition
    elif menu == "a":
        task_username = input("Enter username of person assigned to task: \n").lower()
        task_title = input("Enter task title: \n").lower()
        task_description = input("Enter task description: \n").lower()
        date_format = "%d %b %Y"
        task_completion = "No"
        task_assign_date = datetime.date.today().strftime(date_format)
        
        while True:
            task_due_date = input("Enter task due date(e.g format: 30 Oct 2019): \n")
            try:
                datetime.datetime.strptime(task_due_date,date_format)
                print("Task requirements captured.")
                break
            except:
                print("Invalid date format.Try again.")
        add_task()
    
# View all tasks
    elif menu == "va":
        view_all()
                
# view user tasks
    elif menu == "vm":
        view_mine()
# generate task overview reports
    elif menu == "gr":
        print_tasks_overview('tasks.txt')
        with open('task_overview', 'r') as task_file_read:
            content = task_file_read.read()
            print(content)
        
    # generate user overview reports
        user_overview_print('user.txt')
        with open('user_overview','r') as user_file_read:
            content = user_file_read.read()
            print(content)
        
# Display task statistics
    elif menu == "d":
        with open('user.txt','r+') as users:
            user_list_storage = []
            for line in users:
                login_entry = line.split(',')
                login_entry[1] = login_entry[1].strip()
                user_list_storage = user_list_storage + [login_entry[0]]
            task_list_storage = [0] * len(user_list_storage)
            total_tasks = 0
            with open('tasks.txt','r') as tasks_page:
                for line in tasks_page:
                    task_string = line.split(',')  
                    user_index = user_list_storage.index(task_string[0])
                    user_tasks = task_list_storage[user_index]
                    task_list_storage[user_index] = user_tasks +1
                print(task_list_storage)  
                for i, user in enumerate(user_list_storage):
                    total_tasks += task_list_storage[i]
                    print(f"{user}: {task_list_storage[i]} task(s)")
                    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
                print(f"Total users:{len(user_list_storage)} \nTotal tasks:{total_tasks}")
                break
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made entered an invalid input. Please try again")