import json
import hashlib
def load_user():
    try:

        with open("login_system/data/data_user.txt", "r") as f:
            user=json.loads(f.read())
            return user
    except:
        return {}
def save_user(username,password):

    user=load_user()
    user[username]={
    "name": "",
    "password": password,
    "lock_until": 0,

    "rps": {
        "wins": 0,
        "losses": 0,
        "matches": 0,
        "draws": 0
    },

    "hand_cricket": {
        "wins": 0,
        "losses": 0,
        "matches": 0,
        "highest_score": 0
    }
}

    with open("login_system/data/data_user.txt","w") as f:
        json.dump(user,f,indent=4)

def update_user(user):
    with open("login_system/data/data_user.txt","w") as f:
        json.dump(user,f,indent=4)

def hashing_password(password):
    encoded=password.encode()
    hashed=hashlib.sha256(encoded).hexdigest()
    return hashed