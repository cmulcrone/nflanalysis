#!/bin/bash

#Generate Stats
python fantasy_analysis.py

#Copy output to GCS
gsutil cp -r output/player_score gs://ff17output
dirlist=(`gsutil ls gs://ff17output/player_score`)

#Clear BQ Table
bq rm -f -t nflanalysis_data.player_scores

#Recreate BQ Table
bq mk --table cjmfftest:nflanalysis_data.player_scores WEEK:INTEGER,PLAYERID:STRING,PLAYERNAME:STRING,POSITION:STRING,SCORE:FLOAT

#Iterate over output files and load into BQ
for i in "${dirlist[@]}"
do
   :
    bq load --autodetect --noreplace --source_format='CSV' nflanalysis_data.player_scores $i WEEK:INTEGER,PLAYERID:STRING,PLAYERNAME:STRING,POSITION:STRING,SCORE:FLOAT

   echo $i
done

#bq load --autodetect --source_format='CSV' nflanalysis_data.player_scores gs://ff17output/player_score WEEK:INT, PLAYERID:STRING, PLAYERNAME:STRING, POSITION:STRING, SCORE:FLOAT



