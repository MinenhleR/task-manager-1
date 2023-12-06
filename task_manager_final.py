# import functions 
import math 
import datetime


# make a dictionary of key-values
# in this regard, username to password pairs
# only applicable to dictionary objects. And a dictionary object ensure uniquesness.
# open user text file in read mode
# use strip function to remove whitespaces and split the usernames and passwords

def read_user():
    user = {}
    file = open("user.txt", "r")
    for line in file:
        username, password = line.strip().split(', ')
        user[username] = password.strip()
        file.close()
        return user

# open user text file in write mode to write user logins in text file 

def write_user(user):
    file = open("user.txt", "w")
    for username, password in user.items():
        file.write(f"{username}, {password}\n")
    file.close()

# using while loop for input validation
# using while loop until user input is correct and matches login in user text file 

def user_input_validation(user):
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter users password: ")
        if username in user and user[username] == password:
            print("Login successful. ")
            return username
        else:
            print("Invalid username or password. Please try again.")


# use while loop to allow other users to register until user registers successfully
# if username is taken or password does not match ask user to repeat 
# open usert text file in append mode to add new username
# use strip fuction to remove whitespaces 

def register_user(user):
    while True:
        new_username = input("Please enter new username: ")
        if new_username == "admin":
            print("User is unable to register. ")
            continue
        if new_username in user:
            print("Username already taken. Please enter new username. ")
            continue
        new_password = input("Please enter new password: ")
        confirm_new_password = input("Confirm new password: ")
        if new_password == confirm_new_password:
            user[new_username] = new_password
            write_user(user)
            print("User signed in successfully. ")    
            break
        else:
            print("Password entered not the same. Please try again.")


# ask for user input to open task, which the user has been assigned 
# use imported libraries dates 
# f-string to write task details and add the "NO" value at the end of the task to indicate incompletion of task 

def task():
    username = input("Enter username of whom the task is assigned : ")
    title = input("Enter the title of the task : ")
    description = input("Enter description og the task : ")
    date_assigned = input("Enter the date that the task was assigned to the user (year/month/day) : ")
    due_date = input("Enter due date for the task (year/month/date): ")
    task = (f"{username}, {title}, {description}, {date_assigned}, {due_date}, No\n")
# open text file in append mode   
    file = open("tasks.txt", "a")
    file.write(task)
    file.close()
    print("\n Task has been successfully added. ")

# open task text file in readable mode to read file  
# print each heading to make program more readable 
def read_task():
    file = open("tasks.txt", "r")
    for line in file:
        text_task = line.strip().split(', ')
        username, title, description, date_assigned, due_date, completion_status = text_task
        print(f"Task assigned to : {username}")
        print(f"Title of task : {title}")
        print(f"Description of task : {description}")
        print(f"Task assigned date : {date_assigned}")
        print(f"Task due date : {due_date}")
        print(f"Completion Status: {completion_status}")
        print()
    file.close()

# open task text file in readable mode for users that are assigned to a task 
def user_task(username):
    file = open("tasks.txt", "r")
    for line in file:
        text_task = line.strip().split(', ')
        task_username, title, description, date_assigned, due_date, completion_status = text_task
        if task_username == username :
            print(f"Title of task : {title}")
            print(f"Description of task : {description}")
            print(f"Task assigned date : {date_assigned}")
            print(f"Task due date : {due_date}")
            print(f"Completion Status: {completion_status}")
            print()
    file.close()

# user menu that allows to display statistics 

# create variables to calculate the total number of users and tasks 
# use len fuction to calculate the total number of users 

def statistics(users):
    total_users = len(users)
# initialize variable to keep track of each of the total number of tasks 
    total_tasks = 0
    file = open("tasks.txt", "r")
    for line in file: 
# increment variable by 1 for each iteration to count the total number of tasks in text file 
        total_tasks += 1
    file.close()
    print(f"The total number of users is : {total_users}")
    print(f"The tota; number of tasks is : {total_tasks}")


# presenting menu to the user 
print("Welcome to the Task Management Program!")
user = read_user()
username = user_input_validation(user)
while True:
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task             
ds - Display Statistics                
e - Exit
: ''').lower()
    if menu == 'r':
        register_user(user)
    elif menu == 'a':
        task()
    elif menu == 'va':
        read_task()
    elif menu == 'vm':
        user_task(username)
# menu option that shows the total number of tasks and total number of users 
    elif menu == 'ds':
        statistics(user)
    elif menu == 'e':
        print('Goodbye!!!')
        break
    else:
        print("You have made a wrong choice, Please Try again")
    print()

    print("\n Shoe Inventory menu")
    print("1. Read Shoe Data" )
    print("2. Capture Shoe Data")
    print("3. View All Shoes")
    print("4. View Shoes That Need To Be Re-stocked")
    print("5. Search For Shoe")
    print("6. Calculate Total Value Per Item")
    print("7. Find Shoe With Highest Quantity")
    print("8. Exit")
