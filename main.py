# built in
import sys
# PROJECT MODULES
from file_handler import save_user,load_user,update_user
from login_logic import create_account,login,setup_name
from rock_paper_scissor.main import play_rps
from session_manager import save_session,load_session,clear_session
from hand_cricket.main import hand_cricket_dashboard

def profile_stats(name, username):

    user = load_user()

    print("\n" + "="*50)
    print("📁                PROFILE STATS")
    print("="*50)

    print(f"\n👤 Player : {name}\n")

    # -------- ROCK PAPER SCISSORS --------
    rps_matches = user[username]["rps"]["matches"]
    rps_wins = user[username]["rps"]["wins"]
    rps_losses = user[username]["rps"]["losses"]
    rps_draws = user[username]["rps"]["draws"]

    if rps_matches > 0:
        rps_win_rate = (rps_wins / rps_matches) * 100
    else:
        rps_win_rate = 0

    print("🪨 ROCK PAPER SCISSORS")
    print("-"*40)

    print(f"🎮 Matches Played : {rps_matches}")
    print(f"🏆 Wins           : {rps_wins}")
    print(f"💀 Losses         : {rps_losses}")
    print(f"🤝 Draws          : {rps_draws}")
    print(f"📈 Win Rate       : {rps_win_rate:.2f}%")

    print("\n" + "-"*50)

    # -------- HAND CRICKET --------
    hc_matches = user[username]["hand_cricket"]["matches"]
    hc_wins = user[username]["hand_cricket"]["wins"]
    hc_losses = user[username]["hand_cricket"]["losses"]

    if hc_matches > 0:
        hc_win_rate = (hc_wins / hc_matches) * 100
    else:
        hc_win_rate = 0

    print("\n🏏 HAND CRICKET")
    print("-"*40)

    print(f"🎮 Matches Played : {hc_matches}")
    print(f"🏆 Wins           : {hc_wins}")
    print(f"💀 Losses         : {hc_losses}")
    print(f"📈 Win Rate       : {hc_win_rate:.2f}%")

    print("\n" + "="*50)

    input("\nPress Enter to return to dashboard...")

def dashboard_player(name,username):
        
        while True:
                    
                        print("\n" + "="*45)
                        print("🎮  USER DASHBOARD")
                        print("="*45)

                        print(f"\n👋 Welcome back, {name}!\n")

                        print("Choose an option:\n")

                        print("1️⃣  🪨 Rock Paper Scissors")
                        print("2️⃣  🏏 Hand Cricket ")
                        print("3️⃣  📁 Profile Stats")
                        print("4️⃣  📊 Leaderboard (Coming Soon)")
                        print("5️⃣  🔓 Logout")
                        print("6️⃣  ❌ Exit Application")

                        print("\n" + "-"*45)

                        option_chosen=input("enter what u want to do: ").lower().strip()

                        if option_chosen in ["1","rock paper scissor","rock paper","rock"]:
                            while True:
                                result=play_rps(name)
                                if result == "exit":
                                     break
                                if result:
                                     user=load_user()
                                     user[username]["rps"]["matches"] +=1
                                     if result == "wins":
                                          user[username]["rps"]["wins"] +=1
                                     elif result == "losses":
                                          user[username]["rps"]["losses"] +=1
                                     elif result == "draws":
                                          user[username]["rps"]["draws"] +=1

                                     update_user(user)                                

                        elif option_chosen in ["2","hand cricket","cricket"]:
                            while True:
                                 result=hand_cricket_dashboard(name)
                                 if result == "cancel_match":
                                      break
                                 if result:
                                      user=load_user()
                                      user[username]["hand_cricket"]["matches"] +=1
                                      if result == "wins":
                                          user[username]["hand_cricket"]["wins"] +=1
                                      elif result == "losses":
                                          user[username]["hand_cricket"]["losses"] +=1

                                      update_user(user)                       
                                      


                        elif option_chosen in ["3","profile stats"]:
                            profile_stats(name,username)


                        elif option_chosen in ["4","leaderboard"]:
                             print("Leaderboards is rolling out soon(stay tuned)")
                            

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
