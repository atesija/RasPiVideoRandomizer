#!/bin/sh

#Get rid of the cursor so we don't see it when videos are running
setterm -cursor off

#Set the path to the directories containing your videos
#These are full-length movies
MOVIES="/media/pi/Windfish/Videos/Movies"
#These are shows or series
SHOWS="/media/pi/Windfish/Videos/Series"
#These are intros/openings that will play once initially
INTROS="/media/pi/Windfish/Intros"
#These are bumps/promos that may play between each show
BUMPS="/media/pi/Windfish/Extras"

#Video player (You may need to change this if you don't have omxplayer installed. It is installed on Raspbian by default)
VIDEOPLAYER="omxplayer"
VIDEOPLAYERCOMMANDS="-o hdmi -b"

#Get all videos in the directories with filetype mp4, mkv, avi, ogm, and mov
find "$MOVIES" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > movies.txt
find "$SHOWS" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > shows.txt
find "$INTROS" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > intros.txt
find "$BUMPS" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > bumps.txt

#Check if the file randomizer exists, if not build it
if [ ! -f FileRandomizer ]; then
    g++ FileRandomizer.cpp -o FileRandomizer
fi

#Run custom c++ script to randomize the videos
#Outputs the file videos.txt which is read in the loop below
./FileRandomizer

#Loop through all found files
while IFS= read -r videofile
do
    echo -Playing "$videofile"

    #Play the video in another terminal to allow hotkeys to work with the player
    lxterminal -e "$VIDEOPLAYER" "$VIDEOPLAYERCOMMANDS" "$videofile"
    sleep 1;

    #Stay in this loop while VIDEOPLAYER is still running. Check every second
    while ps ax | grep -v grep | grep $VIDEOPLAYER > /dev/null
    do
        sleep 1;
    done
done < "videos.txt"
