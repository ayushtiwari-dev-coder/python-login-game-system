import random
number_choice=(1,2,3,4,5,6)

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
    if motive == "freestyle":
        weights = [1, 2, 1, 2, 1, 1]
    elif motive == "balanced":
        weights = [1, 2, 3, 3, 2, 1]
    elif motive == "aggressive":
        weights = [1, 1, 2, 3, 4, 4]
    elif motive == "conservative":
        weights = [2, 3, 3, 2, 1, 1]
    elif motive == "desperate":
        weights = [1, 1, 1, 2, 5, 5]
    elif motive == "bowling_high":
        weights = [1, 1, 2, 3, 5, 5]
    elif motive == "bowling_normal":
        weights = [1, 1, 2, 3, 5, 4]
    elif motive == "bowling_low":
        weights = [1, 1, 2, 4, 5, 3]

    else:
        weights=[1,1,1,1,1,1]
        
    return random.choices(number_choice,weights=weights)[0]



