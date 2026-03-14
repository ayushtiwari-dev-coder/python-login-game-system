import random

exit_choice = ["stop", "exit"]
number_choice = [1,2,3,4,5,6]
choice_toss = ["bat","bowl"]


def get_player_choice(name):
    while True:
        player_choice = input(
            f"\n{name}, choose a number (1-6)\n"
            "Type 'exit' or 'stop' to leave the match\n"
            "👉 Your choice: "
        ).lower().strip()

        if player_choice in exit_choice:
            return player_choice

        if player_choice.isdigit():
            number = int(player_choice)
            if number in number_choice:
                return number

        print("❌ Invalid input. Choose from:", number_choice)


def toss_logic(name):

    while True:
        toss_choice = input(f"\n{name}, choose ODD or EVEN: ").lower().strip()

        if toss_choice in ["odd","even"]:
            break

        print("❌ Invalid input. Choose 'odd' or 'even'")

    player_number = get_player_choice(name)

    if player_number in exit_choice:
        return "exit"

    computer_number = random.choice(number_choice)

    print(f"\n🎲 Toss numbers → {name}: {player_number} | Computer: {computer_number}")

    total = player_number + computer_number

    result = "even" if total % 2 == 0 else "odd"

    if toss_choice == result:
        print(f"🏆 {name} won the toss!\n")
        return "player"

    else:
        print("💻 Computer won the toss!\n")
        return "computer"


def decide_innings(name):

    toss_winner = toss_logic(name)

    if toss_winner == "player":

        while True:
            toss_decision = input(f"{name}, do you want to BAT or BOWL? ").lower().strip()

            if toss_decision in choice_toss:
                break

            print("❌ Invalid choice. Choose:", choice_toss)

    else:
        toss_decision = random.choice(choice_toss)
        print(f"💻 Computer chooses to {toss_decision.upper()}\n")

    if toss_decision == "bat":
        batting = toss_winner
        bowling = "computer" if toss_winner == "player" else "player"

    else:
        bowling = toss_winner
        batting = "computer" if toss_winner == "player" else "player"

    return batting, bowling, toss_winner, toss_decision


def play_ball(batting, bowling, name):

    if batting == "player":
        batter_choice = get_player_choice(name)
        bowler_choice = random.choice(number_choice)

        print(f"{name}: {batter_choice} | Computer: {bowler_choice}")

    else:
        batter_choice = random.choice(number_choice)
        bowler_choice = get_player_choice(name)

        print(f"Computer: {batter_choice} | {name}: {bowler_choice}")

    if batter_choice == bowler_choice:
        print(f"💥 OUT! {name if batting=='player' else 'Computer'} is dismissed!\n")
        return "out"

    return batter_choice


def first_inning(batting, bowling, name):

    print("\n🏏 FIRST INNINGS START\n")

    score = 0
    balls = 0

    while True:

        result = play_ball(batting, bowling, name)

        balls += 1

        if result == "out":
            break

        score += result

        print(f"Score: {score} | Balls: {balls}\n")

    print(f"✅ First innings finished → {score} runs ({balls} balls)\n")

    return score, balls


def second_innings(batting, bowling, first_score, name):

    target = first_score + 1

    print("\n🏏 SECOND INNINGS START\n")
    print(f"🎯 Target: {target}\n")

    score = 0
    balls = 0

    while True:

        result = play_ball(batting, bowling, name)

        balls += 1

        if result == "out":
            break

        score += result

        if score >= target:
            print("🎯 Target chased!\n")
            break

        print(f"Score: {score} | Balls: {balls}\n")

    print(f"✅ Second innings finished → {score} runs ({balls} balls)\n")

    return score, balls


def win_announcement(first_batter, first_score, first_balls, second_score, second_balls, toss_winner, toss_decision, name):

    print("\n" + "="*40)
    print("🏏        MATCH SUMMARY        🏏")
    print("="*40)

    winner_name = name if toss_winner == "player" else "Computer"

    print(f"\n🎲 Toss: {winner_name} won the toss and chose to {toss_decision.upper()} first\n")

    print("📊 SCOREBOARD\n")

    print(f"First Innings  : {first_score} runs ({first_balls} balls)")
    print(f"Second Innings : {second_score} runs ({second_balls} balls)\n")

    if first_balls > 0:
        sr1 = (first_score / first_balls) * 100
        print(f"⚡ First Innings Strike Rate  : {sr1:.2f}")

    if second_balls > 0:
        sr2 = (second_score / second_balls) * 100
        print(f"⚡ Second Innings Strike Rate : {sr2:.2f}")

    print("\n" + "-"*40)

    if second_score > first_score:
        winner = "computer" if first_batter == "player" else "player"

    elif second_score < first_score:
        winner = first_batter

    else:
        winner = "draw"

    if winner == "player":
        print(f"\n🔥 {name} WINS THE MATCH!\n")
        return "wins"

    elif winner == "computer":
        print("\n💻 COMPUTER WINS THE MATCH!\n")
        return "losses"

    else:
        print("\n⚖️ MATCH DRAW!\n")
        return "draws"


def endless_mode(name):

    batting, bowling, toss_winner, toss_decision = decide_innings(name)

    first_batter = batting

    first_score, first_balls = first_inning(batting, bowling, name)

    batting, bowling = bowling, batting

    second_score, second_balls = second_innings(batting, bowling, first_score, name)

    result = win_announcement(
        first_batter,
        first_score,
        first_balls,
        second_score,
        second_balls,
        toss_winner,
        toss_decision,
        name
    )

    return result
