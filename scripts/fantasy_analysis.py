import pandas as pd
import nflgame

playerdf = pd.DataFrame({})

weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

players = nflgame.combine_game_stats(nflgame.games(2017, 1))

scoring = {
    # Passing
    'passing_yds' : lambda x : x*.04,
    'passing_tds' : lambda x : x*4,
    'passing_twoptm'  : lambda x : x*2,
    # Rushing
    #'rushing_yds' : lambda x : x*.1 + (2 if x >= 100 else 0),
    'rushing_yds' : lambda x : x*.1,
    'rushing_tds' : lambda x : x*6,
    'kickret_tds' : lambda x : x*6,
    'rushing_twoptm' : lambda x : x*2,
    # Receiving
    'receiving_tds' : lambda x : x*6,
    #'receiving_yds' : lambda x : x*.1 + (2 if x >= 100 else 0),
    'receiving_yds' : lambda x : x*.1,
    'receiving_rec' : lambda x : x*.5,
    'receiving_twoptm' : lambda x : x*2,
    # Various
    'fumbles_lost' : lambda x : x*-2, 
    'passing_ints' : lambda x : x*-2,
}

def score_player(player):
    score = 0
    for stat in player._stats:
        if stat in scoring:
            score += scoring[stat](getattr(player,stat))    
    return score

for p in players.limit(100):
    score = score_player(p)
    print (p.name, p.passing_yds,score)

