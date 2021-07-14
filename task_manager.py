#datetime libary
from datetime import date

#setting user_info to empty list
user_info = {}

#opening user.txt to read username in file
with open("user.txt", "rt") as username:
    for line in username:
        username, password = line.split(", ")
        user_info[username.strip()] = password.strip() #strip to remove the whitespaces
    
user_username = input("Enter username here:\n") #asking user to enter the username: (admin)
    
#while loop  adn if statement to check if username is correct
while user_username not in user_info:
    print("Username incorrect!\n")
    user_username = input("Enter a valid username:\n")

if user_username in user_info:
    print("Username correct!\n")


user_password = input("Enter your password:\n") #asking user to enter password

#while loop and if statement to check if the password is correct
while user_password != user_info[user_username]:
    print("Invaled password\n")
    user_password = input("Enter the correct password:\n")

if user_password != user_info[user_username]:
    print("Your password is correct\n")

if user_username == 'admin':
        userchoice = input('''Please select one of the following options: 
        r - register user:
        a - add task:
        va - view all tasks:
        vm - view my task:
        d - display statistics (total number of tasks & users):
        e - exit
        ''')
else:
#user chooses which option to go into
    userchoice = input('''Please select one of the following options:
    r - register user:
    a - add task:
    va - view all tasks:
    vm - view my task:
    e - exit:\n''')

# register new user and save new username and password to the file user.txt
if userchoice == 'r':
    
    if user_username != "admin":
        print("Only the username with 'admin' can request this option!") 

    #only admin username will have the option to register a new users
    elif user_username == "admin": #The following menu will show when admin is logged i
        new_user = input("Please enter a new username:\n")
        new_user_password = input("Please enter a new password:\n")

        new_password = False

    #while loop and an if/elif statement to confirm the new password thats been entered 
        while new_password == False:
            confirm_new_password = input("Please confirm password:\n")

            if new_user_password == confirm_new_password:
                new_password = True
            print("New username and password is saved!")    

            if new_password == False:
                print("Your password does not match")

        with open("user.txt", "a") as file:
            file.write(f"\n{new_user}, {new_user_password}") #write() function to write the new username and password to the file

#add task in an elif statement and save it to the file tasks.txt
elif userchoice == 'a':

    task_file = open("tasks.txt", "a+") #opening the file tasks.txt to add new tasks 

    new_task_username = input("Please enter the username to whom the task is assigned to:\n")
    new_task_title = input("Please enter the title of the task:\n")
    new_task_description = input("Please add the description of the task:\n")
    new_task_assigned_date = input("Please enter the date the task was assigned:\n")
    new_task_due_date = date.today()
    new_task_completed = input("Is the task completed (Yes / No):\n")

    task_file.write(f"\n{new_task_username}, {new_task_title}, {new_task_description}, {new_task_assigned_date}, {new_task_due_date}, {new_task_completed}")

    task_file.close()

#view all tasks in an elif statement in the file tasks.txt 
elif userchoice == 'va':
    task_file = open("tasks.txt", "r") #opening the file tasks.txt to view all the tasks

    for info in task_file:
        new_task_username, new_task_title, new_task_description, new_task_assigned_date, new_task_due_date, new_task_completed = info.split(", ")

        print(f'''
        New task username:\t{new_task_username}
        Task title:\t\t{new_task_title}
        Task desciption:\t{new_task_description}
        Task assigned date:\t{new_task_assigned_date}
        Task due date:\t\t{new_task_due_date}
        Task completion:\t{new_task_completed}
        ''')

    task_file.close()

#view my tasks in an elif statement in the file tasks.txt
elif userchoice == 'vm':
    view_tasks = open("tasks.txt", 'r')#opening the file tasks.txt to view all my tasks
        
    for info in view_tasks:
        new_task_username, new_task_title, new_task_description, new_task_assigned_date, new_task_due_date, new_task_completed = info.split(", ")

        if user_username == new_task_username:
                print(f'''
        New task username:\t{new_task_username}
        Task title:\t{new_task_title}
        Task desciption:\t{new_task_description}
        Task assigned date:\t{new_task_assigned_date}
        Task due date:\t{new_task_due_date}
        Task completion:\t{new_task_completed}
        ''')

    view_tasks.close()

#if user chooses 'e' it should exit the menu
elif userchoice == 'e':
    print("You have exited! Bye")
    exit
    
#elif statement if the option 'd' is chosen
elif userchoice == "d" and user_username == 'admin':
    task_num = 0
    user_num = 0

    #opening the task.txt file to read all the tasks
    with open("tasks.txt", "r") as num_of_tasks:
        for line in num_of_tasks: #for loop to count the number of tasks 
            task_num += 1
            print(f"\nThe number of tasks are:: {task_num}")      

    #opening the user.txt file to read all the users
    with open("user.txt", "r") as num_of_users:
        for line in num_of_users: #for loop to count the number of users
            user_num += 1
            print(f"\nThe number of users are: {user_num}")

#option to exit the menu
else:
    print("Invalid option! Please choose a optoin that is given.") #if user doesn't choose the given options the following message will display
