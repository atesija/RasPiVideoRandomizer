#!/bin/bash
#Written by Anthony Tesija www.AnthonyTesija.com 

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

#These are songs that can play if you have the bump generator turned on
MUSIC="/media/pi/Windfish/Music"
find "$MUSIC" -name '*.mp3' > "BumpGenerator/music.txt"

#Video player (You may need to change this if you don't have omxplayer installed. It is installed on Raspbian by default)
VIDEOPLAYER="omxplayer"

#Configuration file with all options for these scripts
CONFIGURATION="Configuration.config"

#Keeps track of the last played file so you can continue where you left off
POSITIONTRACKERFILENAME="PlaybackPosition.info"

#Figure out if we're continuing from the last played file
CONTINUE="false"
if [[ "$1" == "--continue" ]] || [[ "$1" == "-c" ]]; then
    CONTINUE="true"
fi

if [ "$CONTINUE" = "false"  ]; then
    #Get all videos in the directories with filetype mp4, mkv, avi, ogm, and mov
    find "$MOVIES" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > "movies.txt"
    find "$SHOWS" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > "shows.txt"
    find "$INTROS" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > "intros.txt"
    find "$BUMPS" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > "bumps.txt"

    #Check if the file randomizer exists, if not build it
    if [ ! -f "FileRandomizer/FileRandomizer" ]; then
        g++ FileRandomizer/FileRandomizer.cpp FileRandomizer/RandomizerConfiguration.cpp -o FileRandomizer/FileRandomizer
    fi

    #Run custom c++ script to randomize the videos
    #Outputs the file videos.txt which is read in the loop below
    ./FileRandomizer/FileRandomizer "$(realpath $CONFIGURATION)"
    
    #Clear out the last played file
    echo 0 > "$POSITIONTRACKERFILENAME"
fi

#Read videos to play in from the randomized video file
VIDEOSTOPLAY=$(<"videos.txt")

#If we're continuing from the last played video we need to figure out where to continue from
CURRENTPOSITION=0
if [ -f "$POSITIONTRACKERFILENAME" ] && [ "$CONTINUE" = "true"  ]; then
    read CURRENTPOSITION < "$POSITIONTRACKERFILENAME"
    VIDEOSTOPLAY=$(sed "1,${CURRENTPOSITION}d" "videos.txt")
fi

#Loop through all found files
echo "$VIDEOSTOPLAY" | while IFS= read -r videofile
do
    echo -Playing "$videofile"

    if [ ! -f "$videofile" ]; then
        #If the video file doesn't exist or we find "[GENERATEBUMP]" then we will generate a bump
        cd BumpGenerator
        python2.7 BumpGenerator.py
        cd ../
    else
        #Play the video in another terminal to allow hotkeys to work with the player
        lxterminal -e "$VIDEOPLAYER" -o hdmi -b "$videofile"
        sleep 1;
    fi
    
    #Stay in this loop while VIDEOPLAYER is still running. Check every second
    while ps ax | grep -v grep | grep $VIDEOPLAYER > /dev/null
    do
        sleep 1;
    done
    
    #Keep track of how many files have been played from this videos.txt and store it
    CURRENTPOSITION=$((CURRENTPOSITION + 1))
    echo $CURRENTPOSITION > "$POSITIONTRACKERFILENAME"
done
