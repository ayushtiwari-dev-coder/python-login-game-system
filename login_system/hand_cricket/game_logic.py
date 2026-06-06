import random
import time
from .ai_brainlogic import get_motive,pick_number,get_bowling_choice,get_batting_choice


random_commentary = [
"Both players hiding their fingers carefully...",
"The bowler squints at the batter's hand trying to guess the number.",
"A quick shake of the hands before the next throw.",
"The batter looks at the bowler suspiciously.",
"The bowler adjusts his fingers slowly.",
"Mind games happening between both players.",
"The crowd watches the fingers closely.",
"A moment of silence before the fingers are revealed.",
"The batter smiles while showing the number.",
"The bowler quickly flashes a number with confidence.",
"Both players try to read each other's mind.",
"A quick hand movement from the batter.",
"The bowler hesitates before showing fingers.",
"The tension rises as both reveal their numbers.",
"The batter hides his hand behind his back first.",
"A clever trick with the fingers!",
"Both hands come out at the same time!",
"The bowler studies the batter's fingers carefully.",
"A calm moment before the next hand reveal.",
"The players prepare their fingers for the next move."
]

out_commentary = [
"Same fingers! OUT!",
"Oh no! The numbers matched perfectly!",
"The bowler guessed it right — OUT!",
"The batter shows the same number — that's OUT!",
"What a prediction by the bowler!",
"The fingers match! The batter is gone!",
"The bowler reads the batter's mind!",
"Both hands show the same number — OUT!",
"The trick failed! The batter is dismissed!",
"Perfect guess by the bowler! OUT!"
]

four_commentary = [
"A perfect FOUR with the fingers!",
"Four fingers up! That's a boundary!",
"The batter flashes FOUR confidently!",
"Nice move! FOUR runs!",
"The bowler didn't expect that FOUR!",
"A quick FOUR from the batter!",
"The batter shows four fingers proudly!",
"FOUR! Smart choice!",
"A clever FOUR from the batter!",
"The fingers say FOUR!"
]

six_commentary = [
"SIX fingers up! That's a big hit!",
"Massive SIX from the batter!",
"The batter boldly shows SIX!",
"What a confident SIX!",
"The bowler is shocked — SIX!",
"A powerful SIX from the hand!",
"The batter goes big with SIX!",
"SIX! The crowd goes wild!",
"The batter flashes six fingers!",
"That's a huge SIX!"
]


exit_choice = ["stop", "exit"]
number_choice = (1, 2, 3, 4, 5, 6)
choice_toss = ("bat", "bowl")


class CancelMatch(Exception):
    pass


def get_player_choice(name,timed=True):
    while True:
        if timed:
            print("⏰ You have 3 seconds!")
            start = time.time()
        player_choice = player_choice = input(f"👉 {name}, your choice: ").lower().strip()

        if timed:
            elapsed = time.time() - start
            if elapsed > 3:
                print("⏰ Too slow! Penalty!")
                return "penalty"

        if player_choice in exit_choice:
            raise CancelMatch

        if player_choice.isdigit():
            number = int(player_choice)
            if number in number_choice:
                return number

        print("❌ Invalid input.")


def toss_logic(name):

    print("\n" + "=" * 35)
    print("🎲 TOSS TIME")
    print("=" * 35)

    while True:
        toss_choice = input(f"\n{name}, choose ODD or EVEN: ").lower().strip()

        if toss_choice in ["odd", "even"]:
            break

        print("❌ Invalid choice. Type 'odd' or 'even'.")

    player_number = get_player_choice(name,timed=False)
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


def decide_innings(match):

    toss_winner = toss_logic(match["name"])

    if toss_winner == "player":
        while True:
            toss_decision = input(
                f"\n{match['name']}, choose your decision:\n"
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

    match["toss_winner"] = toss_winner
    match["toss_decision"] = toss_decision
    match["batting"] = batting
    match["bowling"] = bowling
    match["first_batter"] = batting


def play_ball(match,score,balls):

    if match["batting"] == "player":
        batter_choice = get_player_choice(match["name"])
        if isinstance(batter_choice,int):
            match["batting_history"].append(batter_choice)

        bowler_choice=get_bowling_choice(match,score,balls)
        print(f"🎯 Ball → {match['name']}: {batter_choice} | Computer: {bowler_choice}")
        if batter_choice == "penalty":
            print("💸 Penalty! -20 runs!")
            return "batting_penalty"

    else:
        batter_choice=get_batting_choice(match,score,balls)

        bowler_choice = get_player_choice(match["name"])
        if isinstance(bowler_choice,int):
            match["bowling_history"].append(bowler_choice)

        print(f"🎯 Ball → Computer: {batter_choice} | {match['name']}: {bowler_choice}")
        if bowler_choice == "penalty":
            print("💸 Too slow! Computer scores free runs!")
            return "bowling_penalty"

    if batter_choice == bowler_choice:
        print(random.choice(out_commentary))
        print(f"💥 OUT! {match['name'] if match['batting'] == 'player' else 'Computer'} is dismissed!\n")
        return "out"
    
    
    if batter_choice==4:
        print(random.choice(four_commentary))

    elif batter_choice==6:
        print(random.choice(six_commentary))
    
    else:
        print(random.choice(random_commentary))

    return batter_choice


def play_innings(match, label, total_balls=None):

    print("\n" + "=" * 35)
    print(f"🏏 {label}")
    print("=" * 35)

    if match["batting"] == "player":
        print(f"\n🏏 {match['name']} is BATTING")
        print("🎯 Computer is BOWLING\n")
    else:
        print("\n🏏 Computer is BATTING")
        print(f"🎯 {match['name']} is BOWLING\n")

    target = match.get("target")

    if target:
        print(f"\n🎯 Target to chase: {target}\n")

    score = 0
    balls = 0

    while True:

        result = play_ball(match,score,balls)

        balls += 1

        if result == "out":
            break

        if result == "batting_penalty":
            score = max(0, score - 20)
            print(f"📊 Score after penalty: {score}\n")
            

        elif result == "bowling_penalty":
            score += 20
            print(f"📊 Computer scores 20! Score: {score}\n")
            
        else:
            score += result

        if target and score >= target:
            print("🎯 Target chased successfully!\n")
            break

        if total_balls and balls >= total_balls:
            print("\n⏱ Overs completed!")
            break

        print(f"📊 Score: {score} | Balls: {balls}\n")
        if target:
            runs_remaining=target-score
            if runs_remaining>0:
                if total_balls:
                    balls_left=total_balls-balls
                    print(f"🎯 {runs_remaining} runs needed from {balls_left} balls\n")
                else:
                    print(f"🎯 {runs_remaining} runs needed to win\n")
                

    print(f"\n✅ Innings Finished → {score} runs ({balls} balls)\n")

    return score, balls


def win_announcement(match):

    print("\n" + "=" * 40)
    print("🏏        MATCH SUMMARY        🏏")
    print("=" * 40)

    winner_name = match["name"] if match["toss_winner"] == "player" else "Computer"

    print(f"\n🎲 Toss: {winner_name} won the toss and chose to {match['toss_decision'].upper()} first\n")

    print("📊 SCOREBOARD\n")
    print(f"1️⃣  First Innings  : {match['first_score']} runs ({match['first_balls']} balls)")
    print(f"2️⃣  Second Innings : {match['second_score']} runs ({match['second_balls']} balls)\n")

    winner=None

    if match["second_score"] > match["first_score"]:
        winner = "computer" if match["first_batter"] == "player" else "player"
    elif match["second_score"] < match["first_score"]:
        winner = match["first_batter"]


    if winner == "player":
        print(f"\n🔥 {match['name']} WINS THE MATCH!\n")
        return "wins"
    elif winner == "computer":
        print("\n💻 COMPUTER WINS THE MATCH!\n")
        return "losses"


def super_over(match):
    while True:
        print("\n" + "=" * 40)
        print("🔥 SUPER OVER TIME! 🔥")
        print("=" * 40)

        score1, balls1 = play_innings(match, "SUPER OVER - INNINGS 1", total_balls=6)

        match["batting"], match["bowling"] = match["bowling"], match["batting"]
        match["target"] = score1 + 1

        score2, balls2 = play_innings(match, "SUPER OVER - INNINGS 2", total_balls=6)
        win_announcement(match)

        print("\n" + "=" * 40)
        print("🔥        SUPER OVER RESULT        🔥")
        print("=" * 40)
        print(f"\n{match['name']} : {score1} runs ({balls1} balls)")
        print(f"Computer : {score2} runs ({balls2} balls)\n")
        print("-" * 40)

        if score1 > score2:
            print(f"\n🏆 {match['name']} WINS THE MATCH AFTER SUPER OVER!\n")
            return "wins"
        elif score2 > score1:
            print("\n💻 COMPUTER WINS THE MATCH AFTER SUPER OVER!\n")
            return "losses"
        else:
            print("\n⚖️ SUPER OVER ALSO TIED! ANOTHER SUPER OVER\n")
            continue


def endless_mode(name):
    try:
        match = {"name": name,
                 "batting_history":[],
                 "bowling_history":[]
    }

        decide_innings(match)

        match["first_score"], match["first_balls"] = play_innings(match, "FIRST INNINGS")

        match["batting"], match["bowling"] = match["bowling"], match["batting"]
        match["target"] = match["first_score"] + 1
        input("press enter to continue: ")

        match["second_score"], match["second_balls"] = play_innings(match, "SECOND INNINGS")

        if match["first_score"] == match["second_score"]:
            return super_over(match)

        return win_announcement(match)

    except CancelMatch:
        return "cancel_match"


def limited_mode(name):
    try:
        while True:
            overs = input(f"\n{name}, enter number of overs (1-10): ").strip()

            if overs.isdigit():
                overs = int(overs)
                if 1 <= overs <= 10:
                    break

            print("❌ Invalid input. Choose between 1 and 10 overs.")

        total_balls = overs * 6

        match = {"name": name,
                 "batting_history":[],
                 "bowling_history":[]
    }

        decide_innings(match)

        match["first_score"], match["first_balls"] = play_innings(
            match, "FIRST INNINGS (LIMITED MODE)", total_balls=total_balls
        )

        match["batting"], match["bowling"] = match["bowling"], match["batting"]
        match["target"] = match["first_score"] + 1
        input("press enter to continue: ")

        match["second_score"], match["second_balls"] = play_innings(
            match, "SECOND INNINGS (LIMITED MODE)", total_balls=total_balls
        )

        if match["first_score"] == match["second_score"]:
            return super_over(match)

        return win_announcement(match)

    except CancelMatch:
        return "cancel_match"