#!/bin/sh

#Get rid of the cursor so we don't see it when videos are running
setterm -cursor off

#Set the path to the directories containing your videos
MOVIES="/media/pi/Windfish/Videos/Movies"
SERIES="/media/pi/Windfish/Videos/Series"
INTROS="/media/pi/Windfish/Intros"
BETWEEN="/media/pi/Windfish/Extras"

#Video player
SERVICE="omxplayer"

#Get all videos in the directories with filetype mp4, mkv, avi, ogm, and mov
find "$MOVIES" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > movies.txt
find "$SERIES" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > series.txt
find "$INTROS" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > intros.txt
find "$BETWEEN" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > between.txt

#Run custom c++ script to randomize the videos
#Outputs the file videos.txt
./FileRandomizer
sleep 1;

#Loop through all found files
while IFS= read -r videofile
do
    echo -Playing "$videofile"

    #Play the video in another terminal to allow hotkeys to work with the player
    lxterminal -e "$SERVICE" -o hdmi -b "$videofile"
    sleep 1;

    #Stay in this loop while SERVICE is still running. Check every second
    while ps ax | grep -v grep | grep $SERVICE > /dev/null
    do
        sleep 1;
    done
done < "videos.txt"
