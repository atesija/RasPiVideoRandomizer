#!/bin/bash
#Written by Anthony Tesija www.AnthonyTesija.com 

#Get rid of the cursor so we don't see it when videos are running
setterm -cursor off

#Set the path to the directories containing your videos
VIDEOS="/media/pi/Windfish"
find "$VIDEOS" -name '*.mp4' -or -name '*.mkv' -or -name '*.avi' -or -name '*.ogm' -or -name '*.mov' > "shows.txt"


if [ ! -f "FileRandomizer/FileRandomizer" ]; then
    g++ FileRandomizer/FileRandomizer.cpp FileRandomizer/RandomizerConfiguration.cpp -o FileRandomizer/FileRandomizer
fi

echo "done"
./FileRandomizer/FileRandomizer "Basic"
echo "done"
#Video player (You may need to change this if you don't have omxplayer installed. It is installed on Raspbian by default)
VIDEOPLAYER="omxplayer"
VIDEOSTOPLAY=$(<"videos.txt")
echo "$VIDEOSTOPLAY" | while IFS= read -r videofile
do
    echo -Playing "$videofile"

    #Play the video in another terminal to allow hotkeys to work with the player
    lxterminal -e "$VIDEOPLAYER" -o hdmi -b "$videofile"
    sleep 1;
    
    #Stay in this loop while VIDEOPLAYER is still running. Check every second
    while ps ax | grep -v grep | grep $VIDEOPLAYER > /dev/null
    do
        sleep 1;
    done
done
