#!/bin/bash
#Written by Anthony Tesija www.AnthonyTesija.com 
#Use this script to run RasPiVideoRandomizer.sh but wrapped with a shutdown time. I use this when I want to fall asleep watching shows but don't want the pi to stay on all night.

#Make sure we have an input
if [ "$#" -ne 1 ]; then
    echo "This script requires one parameter, the number of minutes to wait before shutting down."
    echo "For example calling it like this will play videos and then shut down after an hour and 20 minutes: ./ShutdownTimerAndPlayer.sh 80"
    exit 1
fi

#Make sure the input is a positive integer
re='^[0-9]+$'
if ! [[ $1 =~ $re ]]; then
    echo "Please pass a positive integer to this script."
    echo "The number will be how many minutes to wait before shutting down while watching shows."
    exit 1
fi

#Run the video randomizer and player normally
lxterminal -e ./RasPiVideoRandomizer.sh

#Wait for the input time
WAITSECONDS=$(($1 * 60))
sleep $WAITSECONDS

#Shutdown. The reason for waiting instead of passing the wait time into the shutdown function is to be able to cancel this script before it shuts down
sudo shutdown -h now

