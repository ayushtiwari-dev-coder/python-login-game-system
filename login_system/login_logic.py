import time
from file_handler import load_user
from file_handler import update_user
from file_handler import hashing_password

def password_attempt(username):

    user = load_user()
    attempts = 0

    while attempts < 3:

        password = input("enter your password:")

        if user[username]["password"] == hashing_password(password):
            print("login successfully")
            name = user[username]["name"]
            return name, username

        else:
            print("wrong password try again")
            attempts += 1

    user[username]["lock_until"] = int(time.time()) + 300
    update_user(user)
    return None

def setup_name(username):
                        user=load_user()
                        
                        print("\n" + "="*40)
                        print("👋 PROFILE SETUP")
                        print("="*40)
                        print("\nWelcome! Let's personalize your experience.\n")
                        print("To make your experience better,")
                        print("we would like to know your name.")
                        print("This will only be asked once.\n")
                        while True: 
                            name = input("👤 Enter your name: ").title().strip()
                            error=False
                            if name=="":
                                 print("name cannot be empty")
                                 error=True
                            if len(name)>25:
                                 print("Name is to long")
                                 error=True
                            if not name.replace(" ","").isalnum():
                                 print("name should only contain alphabet and number")
                                 error=True

                            if error==False:
                                     
                                user[username]["name"]=name
                                update_user(user)
                                print(f"\n✅ Thanks {name}! Your profile is now set.\n")
                                return name

                     

def create_account():

    user = load_user()

    while True:

        username = input("enter username: ").strip().lower()

        # username validation
        error = False

        if username == "":
            print("username cannot be empty")
            error = True

        if " " in username:
            print("username cannot contain spaces")
            error = True

        if len(username) > 20:
            print("username too long (max 20 characters)")
            error = True

        if username.replace("_","").replace("-","") == "":
            print("username must contain letters or numbers")
            error = True

        if not username.replace("_","").replace("-","").isalnum():
            print("username can only contain letters, numbers, '_' and '-'")
            error = True

        if username in user:
            print("username already exist try another")
            error = True

        if error:
            print()
            continue

        print("username is available")

        print("NOTE:")
        print("password must have:")
        print("1. At least 8 character")
        print("2. one UPPER CASE letter")
        print("3. atleast one number")
        print("4. one special character")
        print("5. no spaces")

        # PASSWORD VALIDATION
        while True:

            password = input("enter password:")
            error = False

            if(len(password) < 8):
                print("password is less than 8 character")
                error = True

            if(len(password)>32):
                 print("password is to long (max 32 characters)")
                 error=True

            if not any(char.isupper() for char in password):
                print("password must have one uppercase")
                error = True

            if not any(char.isdigit() for char in password):
                print("password must contain a number")
                error = True

            if not any(not char.isalnum() for char in password):
                print("ATLEAST one special character")
                error = True

            if " " in password:
                print("There should be no spaces")
                error = True

            if error == False:
                print("password is ready")
                password = hashing_password(password)
                return username, password

def login():
    user=load_user()

    while True:

        username = input("enter your username:")

        if username not in user:
            print("username does not exist,try again")
            continue

        lock_until = user[username]["lock_until"]
        current_time = int(time.time())

        if(current_time < lock_until):
            print("account is locked")
            print("lock time:", lock_until - current_time)
            continue
        else:
            break

    return password_attempt(username)