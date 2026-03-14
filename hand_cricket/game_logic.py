import random

exit_choice = ["stop", "exit"]
number_choice = [1, 2, 3, 4, 5, 6]
choice_toss = ["bat", "bowl"]


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

        print("❌ Invalid input. Choose a number between 1 and 6.")


def toss_logic(name):

    print("\n" + "=" * 35)
    print("🎲 TOSS TIME")
    print("=" * 35)

    while True:
        toss_choice = input(f"\n{name}, choose ODD or EVEN: ").lower().strip()

        if toss_choice in ["odd", "even"]:
            break

        print("❌ Invalid choice. Type 'odd' or 'even'.")

    player_number = get_player_choice(name)

    if player_number in exit_choice:
        return "cancel_match"

    computer_number = random.choice(number_choice)

    print(f"\n🎲 Toss numbers → {name}: {player_number} | Computer: {computer_number}")

    total = player_number + computer_number
    result = "even" if total % 2 == 0 else "odd"

    if toss_choice == result:
        print(f"\n🏆 {name} WON THE TOSS!")
        return "player"
    else:
        print("\n💻 Computer WON THE TOSS!")
        return "computer"


def decide_innings(name):

    toss_winner = toss_logic(name)

    if toss_winner == "cancel_match":
        return "cancel_match"

    if toss_winner == "player":

        while True:
            toss_decision = input(
                f"\n{name}, choose your decision:\n"
                "👉 Type 'bat' or 'bowl': "
            ).lower().strip()

            if toss_decision in choice_toss:
                break

            print("❌ Invalid choice. Choose 'bat' or 'bowl'.")

    else:
        toss_decision = random.choice(choice_toss)
        print(f"\n💻 Computer chooses to {toss_decision.upper()} first.\n")

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
        print(f"🎯 Ball → {name}: {batter_choice} | Computer: {bowler_choice}")

    else:
        batter_choice = random.choice(number_choice)
        bowler_choice = get_player_choice(name)
        print(f"🎯 Ball → Computer: {batter_choice} | {name}: {bowler_choice}")

    if batter_choice in exit_choice:
        return "cancel_match"

    if bowler_choice in exit_choice:
        return "cancel_match"

    if batter_choice == bowler_choice:
        print(f"💥 OUT! {name if batting=='player' else 'Computer'} is dismissed!\n")
        return "out"

    return batter_choice


def first_inning(batting, bowling, name):

    print("\n" + "=" * 35)
    print("🏏 FIRST INNINGS START")
    print("=" * 35)

    score = 0
    balls = 0

    while True:

        result = play_ball(batting, bowling, name)

        if result == "cancel_match":
            return "cancel_match"

        balls += 1

        if result == "out":
            break

        score += result

        print(f"📊 Score: {score} | Balls: {balls}\n")

    print(f"\n✅ First Innings Finished → {score} runs ({balls} balls)\n")

    return score, balls


def second_innings(batting, bowling, first_score, name):

    target = first_score + 1

    print("\n" + "=" * 35)
    print("🏏 SECOND INNINGS START")
    print("=" * 35)

    print(f"\n🎯 Target to chase: {target}\n")

    score = 0
    balls = 0

    while True:

        result = play_ball(batting, bowling, name)

        if result == "cancel_match":
            return "cancel_match"

        balls += 1

        if result == "out":
            break

        score += result

        if score >= target:
            print("🎯 Target chased successfully!\n")
            break

        print(f"📊 Score: {score} | Balls: {balls}\n")

    print(f"\n✅ Second Innings Finished → {score} runs ({balls} balls)\n")

    return score, balls


def first_inning_limited(batting, bowling, name, total_balls):

    print("\n" + "=" * 35)
    print("🏏 FIRST INNINGS START (LIMITED MODE)")
    print("=" * 35)

    score = 0
    balls = 0

    while True:

        result = play_ball(batting, bowling, name)

        if result == "cancel_match":
            return "cancel_match"

        balls += 1

        if result == "out":
            break

        score += result

        if balls >= total_balls:
            print("\n⏱ Overs completed!")
            break

        print(f"📊 Score: {score} | Balls: {balls}\n")

    print(f"\n✅ First Innings Finished → {score} runs ({balls} balls)\n")

    return score, balls


def second_innings_limited(batting, bowling, first_score, name, total_balls):

    target = first_score + 1

    print("\n" + "=" * 35)
    print("🏏 SECOND INNINGS START (LIMITED MODE)")
    print("=" * 35)

    print(f"\n🎯 Target to chase: {target}\n")

    score = 0
    balls = 0

    while True:

        result = play_ball(batting, bowling, name)

        if result == "cancel_match":
            return "cancel_match"

        balls += 1

        if result == "out":
            break

        score += result

        if score >= target:
            print("🎯 Target chased successfully!\n")
            break

        if balls >= total_balls:
            print("\n⏱ Overs completed!")
            break

        print(f"📊 Score: {score} | Balls: {balls}\n")

    print(f"\n✅ Second Innings Finished → {score} runs ({balls} balls)\n")

    return score, balls


def win_announcement(first_batter, first_score, first_balls, second_score, second_balls, toss_winner, toss_decision, name):

    print("\n" + "=" * 40)
    print("🏏        MATCH SUMMARY        🏏")
    print("=" * 40)

    winner_name = name if toss_winner == "player" else "Computer"

    print(f"\n🎲 Toss: {winner_name} won the toss and chose to {toss_decision.upper()} first\n")

    print("📊 SCOREBOARD\n")

    print(f"1️⃣  First Innings  : {first_score} runs ({first_balls} balls)")
    print(f"2️⃣  Second Innings : {second_score} runs ({second_balls} balls)\n")

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

    result = decide_innings(name)

    if result == "cancel_match":
        return "cancel_match"

    batting, bowling, toss_winner, toss_decision = result

    first_batter = batting

    result = first_inning(batting, bowling, name)

    if result == "cancel_match":
        return "cancel_match"

    first_score, first_balls = result

    batting, bowling = bowling, batting

    result = second_innings(batting, bowling, first_score, name)

    if result == "cancel_match":
        return "cancel_match"

    second_score, second_balls = result

    return win_announcement(
        first_batter,
        first_score,
        first_balls,
        second_score,
        second_balls,
        toss_winner,
        toss_decision,
        name
    )


def limited_mode(name):

    while True:
        overs = input(f"\n{name}, enter number of overs (1-10): ").strip()

        if overs.isdigit():
            overs = int(overs)
            if 1 <= overs <= 10:
                break

        print("❌ Invalid input. Choose between 1 and 10 overs.")

    total_balls = overs * 6

    result = decide_innings(name)

    if result == "cancel_match":
        return "cancel_match"

    batting, bowling, toss_winner, toss_decision = result

    first_batter = batting

    result = first_inning_limited(batting, bowling, name, total_balls)

    if result == "cancel_match":
        return "cancel_match"

    first_score, first_balls = result

    batting, bowling = bowling, batting

    result = second_innings_limited(batting, bowling, first_score, name, total_balls)

    if result == "cancel_match":
        return "cancel_match"

    second_score, second_balls = result

    return win_announcement(
        first_batter,
        first_score,
        first_balls,
        second_score,
        second_balls,
        toss_winner,
        toss_decision,
        name
    )
