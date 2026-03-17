import random
number_choice=(1,2,3,4,5,6)

motive_weights = {
    "freestyle":    [1, 2, 1, 2, 1, 1],
    "balanced":     [1, 2, 3, 3, 2, 1],
    "aggressive":   [1, 1, 2, 3, 4, 4],
    "conservative": [2, 3, 3, 2, 1, 1],
    "desperate":    [1, 1, 1, 2, 5, 5],
    "bowling_high":   [1, 1, 2, 2, 3, 3],
    "bowling_normal": [1, 1, 2, 3, 3, 2],
    "bowling_low":    [1, 1, 2, 3, 2, 2],
}

def get_motive(match,score,balls):
    total_balls=match.get("total_balls")
    target=match.get("target")

    if match["batting"]=="computer":
        if total_balls is None:
            return "balanced"

        if target:
            remaining_balls=total_balls - balls
            remaining_score=target - score
            if remaining_balls==0:
                req_runrate=remaining_score
            else:
                req_runrate=remaining_score/remaining_balls
            if req_runrate <= 2:
                motive ="freestyle"
            elif req_runrate <= 4:
                motive="balanced"
            elif req_runrate <= 6:
                motive="aggressive"
            else:
                motive="desperate"
            return motive
        else:
            if balls==0:
                return "aggressive"
            else:
                projected_runrate=score/balls
                projected_final=projected_runrate*total_balls

                if projected_runrate < 3:
                    return "aggressive"
                elif projected_runrate < 5:
                    return "balanced"
                else:
                    return "conservative"

    else:
        if not total_balls:
            return "bowling_high"
        
        if balls==0 or not target:
            return "bowling_normal"
        remaining=total_balls-balls
        if remaining==0:
            return "bowling_high"
        
        player_rate=(target-score)/remaining

        if player_rate > 5:
            return "bowling_high"
        elif player_rate>3:
            return "bowling_normal"
        else:
            return "bowling_low"

def pick_number(motive):
    weights=motive_weights.get(motive,[1,1,1,1,1,1])
    return random.choices(number_choice,weights=weights)[0]

def get_frequency_choice(history):
    if len(history)<3:
        return None
    frequency={1:0,2:0,3:0,4:0,5:0,6:0}
    for number in history:
        frequency[number] +=1
    return max(frequency,key=lambda x: frequency[x])

def get_recency_choice(history):
    if len(history)<5:
        return None
    last_5=history[-5:]
    missing=[n for n in number_choice if n not in last_5]
    if missing:
       return random.choice(missing)
    return None

def get_bowling_choice(match, score, balls):
    history = match.get("batting_history", [])
    motive = get_motive(match, score, balls)

    motive_w = list(motive_weights.get(motive, [1,1,1,1,1,1]))
    freq_w = [1,1,1,1,1,1]
    rec_w = [1,1,1,1,1,1]

    freq_choice = get_frequency_choice(history)
    if freq_choice:
        freq_w[freq_choice - 1] = 10

    if len(history) >= 5:
        for n in history[-5:]:
            rec_w[n-1] += 2

    final_weights = [motive_w[i] + freq_w[i] + rec_w[i] for i in range(6)]
    return random.choices(number_choice, weights=final_weights)[0]


def get_batting_choice(match, score, balls):
    history = match.get("bowling_history", [])
    motive = get_motive(match, score, balls)

    motive_w = list(motive_weights.get(motive, [1,1,1,1,1,1]))
    freq_w = [1,1,1,1,1,1]
    rec_w = [1,1,1,1,1,1]

    freq_choice = get_frequency_choice(history)
    if freq_choice:
        freq_w[freq_choice - 1] = max(0, freq_w[freq_choice - 1] - 8)

    if len(history) >= 5:
        for n in history[-5:]:
            rec_w[n-1] = max(0, rec_w[n-1] - 1)

    final_weights = [motive_w[i] + freq_w[i] + rec_w[i] for i in range(6)]
    final_weights = [max(0, w) for w in final_weights]
    return random.choices(number_choice, weights=final_weights)[0]