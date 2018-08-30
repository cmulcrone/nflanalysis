#Original source: http://wseaton.com/pulling-data-with-nflgame.html

import nflgame
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#%matplotlib inline

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

games = nflgame.games(2015)
players = nflgame.combine_game_stats(games)

runs = pd.Series([p.rushing_yds for p in players.rushing()])

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111)
ax.set_title('age vs. rushing yds', fontsize=14, color='black')
fig.subplots_adjust(top=0.85)

ax.set_ylabel('age (days)')
ax.set_xlabel('rushing_yds')

plt.style.use('ggplot')


for p in players.rushing():
    plt.scatter(p.rushing_yds, (datetime.datetime.today() - datetime.datetime.strptime(p.player.birthdate,'%m/%d/%Y')).days)
    
