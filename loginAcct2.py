def register():
    db = open("login.txt", "r")
    username = input("Create username: ")
    password = input("Create password: ")
    password1 = input("confirm password: ")
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))
        print(data)

    if password != password1:
        print(f"\nPasswords dont match, enter correct password.")
        register()
    else:
        if len(password) <= 6:
            print(f"\npassword to short, re-enter password: ")
            register()
        elif username in d:
            print(f"\nusername exists")
            register()
        else:
            db = open("login.txt", "a")
            db.write(username+",  "+password+"\n")
            print("Success")

def access():
    db = open("login.txt", "r")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not len(username or password) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        print(data)
        try:
            if data [username]:
                try:
                    if password == data[username]:
                        print('Login Successful')
                        print('Welcome')
                    else:
                        print('password incorrect')
                except:
                    print('Wrong Password')
            else:
                print('Username does not exsits')
        except:
            print('login error')

def home(option=None):
    option = input("Login | Signup: ")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter a option")
home(option=None)





