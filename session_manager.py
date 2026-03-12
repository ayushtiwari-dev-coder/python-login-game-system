import os
def save_session(username):
    os.makedirs("login_system/data", exist_ok=True)
    with open("login_system/data/session_user.txt", "w") as f:
        f.write(username)


def load_session():
    try:
        with open("login_system/data/session_user.txt", "r") as f:
            username = f.read().strip()
            if username == "":
                return None
            return username
    except FileNotFoundError:
        return None


def clear_session():
    with open("login_system/data/session_user.txt", "w") as f:
        f.write("")   
        

    