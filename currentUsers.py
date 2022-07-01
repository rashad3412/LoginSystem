# List current users in application
# send current users to the login.txt file
# send a messages to current users for using application

def currentUsers():
    username = input('Welcome Back!!\nEnter username: ')
    password = input('Enter password: ')
    with open('login.txt',"r") as f:
        if password != password:
            print("Passwords dont match, enter correct password.")
        elif username != username:
            print('Username does not exist. Please try again.')
currentUsers()

