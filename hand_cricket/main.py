from .game_logic import endless_mode
from .game_logic import limited_mode


def hand_cricket_dashboard(name):

    while True:

        print("\n" + "="*45)
        print("🏏              HAND CRICKET              🏏")
        print("="*45)

        print(f"\n👋 Welcome {name}!\n")

        print("Choose a mode:\n")

        print("1️⃣  Endless Mode")
        print("2️⃣  Limited Mode")
        print("3️⃣  Back to Dashboard")

        print("\n" + "-"*45)

        choice = input("👉 Enter your choice: ").lower().strip()

        if choice in ["1", "endless", "endless mode"]:

            print("\n🚀 Starting Endless Mode...\n")

            result = endless_mode(name)
            if result=="cancel_match":
                continue

            return result


        elif choice in ["2", "limited", "limited mode"]:
            result=limited_mode(name)

            if result=="cancel_match":
                continue
            return result


        elif choice in ["3", "back", "exit"]:

            print("\n🔙 Returning to dashboard...\n")
            return "cancel_match"


        else:
            print("\n❌ Invalid choice. Please try again.")


    