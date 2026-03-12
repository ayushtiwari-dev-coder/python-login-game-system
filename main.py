# built in
import sys
# PROJECT MODULES
from file_handler import save_user,load_user,update_user
from login_logic import create_account,login,setup_name
from rock_paper_scissor.main import play_rps
from session_manager import save_session,load_session,clear_session

def dashboard_player(name,username):
        
        while True:
                    
                        print("\n" + "="*45)
                        print("🎮  USER DASHBOARD")
                        print("="*45)

                        print(f"\n👋 Welcome back, {name}!\n")

                        print("Choose an option:\n")

                        print("1️⃣  🪨 Rock Paper Scissors")
                        print("2️⃣  🏏 Hand Cricket (Coming Soon)")
                        print("3️⃣  📊 Leaderboard (Coming Soon)")
                        print("4️⃣  📁 Profile Stats (Coming Soon)")
                        print("5️⃣  🔓 Logout")
                        print("6️⃣  ❌ Exit Application")

                        print("\n" + "-"*45)

                        option_chosen=input("enter what u want to do: ").lower().strip()

                        if option_chosen in ["1","rock paper scissor","rock paper","rock"]:
                            result=play_rps(name)
                            # TODO: COMPLTE PROFILE STATS TRACKING SYSTEM
                            '''if result:
                                 user=load_user()

                                 if result=="wins":
                                      user[username]["rps"]["wins"] +=1

                                 elif result=="losses":
                                      user[username]["rps"]["losses"] +=1

                                 elif result=="draws":
                                      user[username]["rps"]["draws"] +=1

                                 update_user(user)'''
                        elif option_chosen in ["2","hand cricket","cricket"]:
                            print("Hand Cricket is rolling out soon(stay tuned)")


                        elif option_chosen in ["3","leaderboard"]:
                            print("Leaderboard is rolling out soon(stay tuned)")


                        elif option_chosen in ["4","profile stats"]:
                            print("Profile stats are rolling out soon(stay tuned)")


                        elif option_chosen in ["5","logout"]:
                            clear_session()
                            print("\n🔓 Logging out...")
                            print("Returning to main menu...\n")
                            break


                        elif option_chosen in ["6","exit","exit application"]:
                            print("\n👋 Closing application...")
                            sys.exit()


                        else:
                            print("invalid input")

username=load_session()
if username:
     user=load_user()
     if username in user:
        name=user[username]["name"]
        dashboard_player(name,username)

while True:

    print("\n" + "="*45)
    print("🔐        LOGIN SYSTEM        🔐")
    print("="*45)

    print("\n📋 MAIN MENU\n")

    print("1️⃣   Create Account")
    print("2️⃣   Login")
    print("3️⃣   Exit")

    print("\n" + "-"*45)

    choice = input("👉 Enter your choice: ").lower().strip()

    print()

    if choice in ["1", "create account", "create"]:

        print("🆕 Creating a new account...\n")

        username, password = create_account()
        save_user(username, password)
        name = setup_name(username)
        save_session(username)
        print("\n✅ Account created successfully!\n")
        dashboard_player(name,username)
        
    elif choice in ["2", "login account", "login"]:

        print("🔑 Login to your account\n")

        result = login()

        if result:
             name,username=result
             save_session(username)
             dashboard_player(name,username)

        else:
             print("Too many wrong attempts. Account locked.\n")
             print("Returning to main menu...\n")



    elif choice in ["3", "exit"]:

        print("\n👋 Thank you for using the system!")
        print("🚪 Exiting program...\n")
        break


    else:
        print("❌ Invalid input. Please try again.\n")