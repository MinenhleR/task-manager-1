# Import hashlib for password hashing
import hashlib  

# Modify the read_user function to read hashed passwords
def read_user():
    user = {}
    with open("user.txt", "r") as file:
        for line in file:
            username, hashed_password = line.strip().split(', ')
            user[username] = hashed_password.strip()
    return user

# Use bcrypt for password hashing
import bcrypt

# Modify the register_user function to hash passwords
def register_user(user):
    while True:
        new_username = input("Please enter a new username: ")
        if new_username == "admin":
            print("User is unable to register.")
            continue
        if new_username in user:
            print("Username already taken. Please enter a new username.")
            continue
        new_password = input("Please enter a new password: ")
        confirm_new_password = input("Confirm new password: ")
        if new_password == confirm_new_password:
            # Hash the password before storing it
            hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
            user[new_username] = hashed_password
            write_user(user)
            print("User signed up successfully.")
            break
        else:
            print("Passwords entered do not match. Please try again.")

# Modify the user_input_validation function to compare hashed passwords
def user_input_validation(user):
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if username in user and bcrypt.checkpw(password.encode(), user[username].encode()):
            print("Login successful.")
            return username
        else:
            print("Invalid username or password. Please try again.")