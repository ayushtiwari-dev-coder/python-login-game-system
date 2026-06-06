
import sys
from database.sql_handler import create_user,get_user,update_hand_cricket_stats,update_rps_stats,get_profile_stats,get_leaderboard
from login_logic import create_account,login,setup_name
from rock_paper_scissor.main import play_rps
from session_manager import save_session,load_session,clear_session
from hand_cricket.main import hand_cricket_dashboard


def print_leaderboard(data):

    print("\n🏆 Leaderboard")

    for player in data:
        print(
            f"{player['username']} | "
            f"Wins: {player['wins']} | "
            f"Matches: {player['matches']} | "
            f"Win Rate: {player['win_rate']:.2f}%"
        )


def profile_stats(name, username):

    stats = get_profile_stats(username)

    rps = stats["rps"]
    hc = stats["hand_cricket"]

    print("\n" + "="*50)
    print("📁                PROFILE STATS")
    print("="*50)

    print(f"\n👤 Player : {name}\n")

    rps_matches = rps["matches"]
    rps_wins = rps["wins"]
    rps_losses = rps["losses"]
    rps_draws = rps["draws"]

    rps_win_rate = (rps_wins / rps_matches * 100) if rps_matches else 0

    print("🪨 ROCK PAPER SCISSORS")
    print("-"*40)

    print(f"🎮 Matches Played : {rps_matches}")
    print(f"🏆 Wins           : {rps_wins}")
    print(f"💀 Losses         : {rps_losses}")
    print(f"🤝 Draws          : {rps_draws}")
    print(f"📈 Win Rate       : {rps_win_rate:.2f}%")

    print("\n" + "-"*50)

    hc_matches = hc["matches"]
    hc_wins = hc["wins"]
    hc_losses = hc["losses"]

    hc_win_rate = (hc_wins / hc_matches * 100) if hc_matches else 0

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
                        print("4️⃣  📊 Leaderboard")
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
                                     update_rps_stats(username,result)                                

                        elif option_chosen in ["2","hand cricket","cricket"]:
                            while True:
                                 result=hand_cricket_dashboard(name)
                                 if result == "cancel_match":
                                      break
                                 if result:
                                      update_hand_cricket_stats(username,result)                       
                                      


                        elif option_chosen in ["3","profile stats"]:
                             profile_stats(name,username)


                        elif option_chosen in ["4","leaderboard"]:
                             while True:
                                  print("\n Leaderboard")
                                  print("1. rock paper scissors")
                                  print("2. hand cricket")
                                  print("3.back")
                                  choice=input("choose leaderboard: ").strip().lower()
                                  if choice in ["1","rps","rock paper scissors"]:
                                       data=get_leaderboard("rps")
                                       print_leaderboard(data)

                                  elif choice in ["2","hc","hand cricket"]:
                                       data=get_leaderboard("hand_cricket")
                                       print_leaderboard(data)

                                  elif choice in ["3","exit"]:
                                       break
                                  else:
                                       print("invalid input")

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
     user=get_user(username)
     if user:
        name=user["name"]
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
        name = setup_name(username)
        create_user(username,name,password)
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