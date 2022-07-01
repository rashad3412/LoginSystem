# Create login account with email, username, and password.
# Login system
# Confirmed password in a text file.
# save info and validate information and allow them to login.
# create another txt file for current users
# create another txt file for block users


def currentUsers():
    db = open('login.txt', "r")
    username = input('Enter username: ')
    password = input('Enter password: ')
    if not len(username or password) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print('Welcome Back!')
                        print('Login Successful!')
                    else:
                        print('password incorrect')
                except:
                    print('Wrong Password')
            else:
                print('Username does not exsits')
        except:
            print('login error, check username or password.')


def user_email():
    email = input(f'\nEnter your email: ')
    email2 = input('Confirm email: ')
    with open('login.txt', 'r') as e:
        if email == email2:
            if email2 in e:
                print('Email already exists.')
                user_email()
            else:
                db = open("login.txt", 'a')
                db.write(email + ", " + 'email address' + "\n")
                print("Email confirmed.")
            new_login()
        else:
            print("Please re-enter email, emails don't match. ")
            user_email()


def new_login():
    username = input(f'\ncreate a new username please: ')
    password = input('create a new password: ')
    password1 = input('confirm password: ')
    with open('login.txt', 'r') as f:
        if password != password1:
            print("Passwords dont match, enter correct password.")
        else:
            if len(password) <= 6:
                print("password to short, re-enter password: ")
                new_login()
            elif username in f:
                print("username exists")
                new_login()
            else:
                db = open("login.txt", 'a')
                db.write(username + ", " + password + '\n')
                print("You have successfully created an account.")


def register():
    new_user = input("If you would like to create an account type signup: ")
    if new_user == 'signup':
        print('Welcome to our Login System: ')
        print('Follow steps below to finish created your account.')
        user_email()
    current_users = input('\nType login to access account: ')
    if current_users == 'login':
        currentUsers()
    else:
        print('Thank you for visiting our site and enjoy your day.')

register()
