#Source: https://github.com/BurntSushi/nflgame/issues/323

import nflgame
import csv

weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

#players = nflgame.combine_game_stats(nflgame.games(2017, 1))

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

for week in weeks:
    with open('output/player_score/Week'+str(week)+'.csv', 'w') as csvfile:
        statwriter = csv.writer(csvfile, delimiter=',', \
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        players = nflgame.combine_game_stats(nflgame.games(2017, week)) 
        for p in players:
            score = score_player(p)
            #Writes individual scores of users
            statwriter.writerow([week, p.playerid.encode(encoding='UTF-8'), \
                p.name.encode(encoding='UTF-8'), \
                p.guess_position.encode(encoding='UTF_8'), \
                round(score,2)])
            '''print (week, p.playerid.encode(encoding='UTF-8'), \
                    p.name.encode(encoding='UTF-8'), \
                    p.guess_position.encode(encoding='UTF_8'), \
                    round(score,2))

    '''
