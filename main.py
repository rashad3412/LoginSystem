# Create a program to for user input
# Program should run through terminal
# User should enter username and password
# User should be notified when the username and password is correct
# Create login account with email, username, and password.
# Login system
# Confirmed password in a text file.
# save info and validate information and allow them to login.
# print('Login Information')

user_name = input('Username: ')
password = input('Password: ')

if user_name == 'rashad3412':
    print('username is correct')
elif user_name == 'meez12':
    print('username is correct')
else:
    print('please enter the correct username.')
if password == '1234':
    print('password is correct')
elif password == '456':
    print('password is correct')
else:
    print('please enter the correct password.')
print()


def new_login():
    login = input(f'update username: ')
    if login != ' ':
        print("username updated: ")

    return login


print(new_login())

print()


def new_password():
    password2 = input('password expired create new password: ')
    if password2 != ' ':
        print('Your password has been updated: ')

    return password2


print(new_password())



















