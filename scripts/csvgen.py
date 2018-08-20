import nflgame
import csv
import os
#Define a list for every week in the NFL regular season
weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
#For every week in the weeks list, grab the player game logs and create a csv file for each week
for week in weeks:
    nflgame.combine_play_stats(nflgame.games(2016, week=week)).csv(str(week)+'.csv')

#The previous function created an empty row between each row of data. The function below brings back in every csv, removes the empty rows, and creates new csv files
for week in weeks:
    input = open(str(week)+'.csv', 'rb')
    output = open('Week'+str(week)+'.csv', 'wb')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row:
            writer.writerow(row)
            input.close()
            output.close()
            
#Delete unused csv files
for week in weeks:
    os.remove(str(week)+'.csv')

