import random

def play_rps(name):

    # Game rules
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    options = ["rock", "paper", "scissors","stop","exit"]
    moves=["rock","paper","scissors"]


    def get_player_choice():
        """Ask player for a valid choice."""
        while True:

            choice = input("Enter rock, paper, scissors  ('exit' or 'stop'): ").lower().strip()
            if choice=="scissor":
                choice="scissors"

            if choice not in options:
                print("Invalid option, try again.")

            else:
                return choice


    def rules(player, computer):
        """winner decider for each round."""
        if player == computer:
            return "draw"

        elif beats[player] == computer:
            return "player"

        else:
            return "computer"


    def update_score(result, player_score, computer_score, name):
        """update and print score."""
        if result == "player":
            player_score += 1
            print(f"🔥 {name} wins this round!")
            
        elif result == "computer":
            computer_score += 1
            print("💻 Computer wins this round!")
            
        else:
            print("🤝 It's a draw!")
            

        return player_score, computer_score


    def print_scoreboard(name, player_score, computer_score):
        """Display current scoreboard."""

        print("\n📊 Scoreboard")
        print(f"{name}: {player_score}  |  Computer: {computer_score}\n")


    def announce_winner(name, player_score, computer_score):
        """Announce match winner."""

        if player_score > computer_score:
            print(f"\n🏆 {name} is the CHAMPION!\n")
            return "wins"

        elif player_score == computer_score:
            print("\n⚖️ Match ended in a DRAW!\n")
            return "draws"
        else:
            print("\n💻 Computer wins the MATCH!\n")
            return "losses"


    # Game Modes
    def endless_mode(name):
        print("\nType 'exit or stop' anytime to return to dashboard")
        player_score, computer_score = 0, 0

        while True:

            player = get_player_choice()
            if player in ["rock","paper","scissors"]:


                computer = random.choice(moves)

                print(f"🤖 Computer chose: {computer.upper()}")

                result = rules(player, computer)

                player_score, computer_score = update_score(result, player_score, computer_score, name)

                print_scoreboard(name, player_score, computer_score)

            elif player in ["stop","exit"]:

                result=announce_winner(name, player_score, computer_score)

                print(f"Which mode next, {name}?")
                return result


    def limited_mode(name, rounds):
        print("\nType 'exit or stop' anytime to return to dashboard")
        while True:

            player_score, computer_score = 0, 0

            for current_round in range(1, rounds + 1):

                print(f"\n⚔️  Round {current_round} – Fight!\n")

                player = get_player_choice()
                if player in ["stop","exit"]:
                    print("game stopped early")
                    result=announce_winner(name,player_score,computer_score)
                    return result

                computer = random.choice(moves)

                print(f"🤖 Computer chose: {computer.upper()}")

                result = rules(player, computer)

                player_score, computer_score = update_score(result, player_score, computer_score, name)

                print_scoreboard(name, player_score, computer_score)

            result=announce_winner(name, player_score, computer_score)
            while True:
                play = input("Replay same mode? (yes/no): ").lower().strip()

                if play in ["no", "n"]:

                    print(f"Which mode next, {name}")
                    return result
                elif play in ["yes","ye","y"]:
                    break
                else:
                    print("invalid input,please type 'yes or no' ")

    print("\n" + "="*40)
    print(f"🔥 Welcome {name} to ROCK PAPER SCISSORS 🔥")
    print("="*40 + "\n")


    while True:

        print("\n🎮 Choose Game Mode:")
        print("1️⃣  Endless Mode")
        print("2️⃣  Limited Mode")
        print("3️⃣  Exit\n")

        mode = input("Enter 1 or 2 or 3: ").lower()

        if mode in ["1", "endless", "e", "en"]:
            endless_mode(name)

        elif mode in ["2", "limited", "limit", "li"]:

            while True:
                try:
                    rounds = int(input("Enter number of rounds (3, 5, or 10): "))

                    if 0 < rounds <= 20:
                        break

                    else:
                        print("Invalid input, try again.")

                except ValueError:
                    print("Invalid input, please enter a number.")

            limited_mode(name, rounds)

        elif mode in ["3", "exit", "exi", "ex"]:

            print("\n🎮 Thanks for playing! See you again!\n")
            return

        else:
            print("Invalid input, please try again.")