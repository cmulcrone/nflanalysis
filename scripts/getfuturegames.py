# https://github.com/BurntSushi/nflgame/issues/267
import nflgame

past_games = nflgame.games(2016, 11)
for game in past_games:
    print game

print '-'

future_games = [game for game in nflgame.live._games_in_week(2018, 1) if game['eid'] not in [g.eid for g in past_games]]
for game in future_games:
    print '{} at {} on {}/{} {}'.format(game['away'], game['home'], game['month'], game['day'], game['time'])
