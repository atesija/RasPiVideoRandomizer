import glob
import os
import re
import random
import json
from subprocess import Popen, PIPE
from time import sleep

#TODO: read these in from central location like json
order_keys = ["show", "bump", "commercial", "movie", "lineup", "intro"]
special_keys = ["repeat", "chance"]

def video_contains_string(video_filename, strings):
    return any(string in video_filename for string in strings)
    
def whitelist_videos(video_list, whitelist_strings):
    return [video for video in video_list if video_contains_string(video, whitelist_strings)]
    
def blacklist_videos(video_list, blacklist_strings):
    return [video for video in video_list if not video_contains_string(video, blacklist_strings)]

def file_is_video(filename):
    video_file_endings = [".mp4", ".avi", ".mkv", ".mov", ".ogm"]
    return any(video_file in filename for video_file in video_file_endings)

def get_videos_from_location(folder_path):
    videos = []
    for root, dirs, files in os.walk(folder_path):
        videos.extend([os.path.join(root, f) for f in files if file_is_video(f)])
    return videos

def get_all_videos_from_folders(folders):
    return [get_videos_from_location(folder) for folder in folders]

def randomize_videos(video_list):
    random.shuffle(video_list)
    return video_list

def is_video_order_template_key(order_key):
    if order_key in order_keys:
        return True

    for special_key in special_keys:
        if special_key in order_key:
            return True

    return False

def build_video_order(order_template):
    video_order = []
    for option in order_template:
        if not is_video_order_template_key(option):
            print option + " is not a key for the video order template"
            print "Options are: " + ', '.join(order_keys)
            print "Special options that follow normal options are: " + ', '.join(special_keys)
            continue

        if "repeat" in option:
            repeat_amount = [int(s) for s in option.split() if s.isdigit()]
            if len(repeat_amount) is 1:
                for _ in range(repeat_amount[0] - 1):
                    video_order.append(video_order[-1])
            elif len(repeat_amount) is 2:
                for _ in range(random.randint(repeat_amount[0], repeat_amount[1]) - 1):
                    video_order.append(video_order[-1])
            else:
                print option + " is not a well formed repeat option"
                print "If one int follows it the previous option will be repeated that many times"
                print "If two ints follow it the previous option will be repeated randomly between those two amounts of times inclusivly"

        elif "chance" in option:
            chance_to_stay = [int(s) for s in option.split() if s.isdigit()]
            if random.randint(0, 100) >= chance_to_stay[0]:
                del video_order[-1]

        else:
            video_order.append(option)

    return video_order
    
def play_video(video_file):
    print "Playing: " + video_file
    player = Popen(["lxterminal", "-e", "omxplayer",  video_file, "-b", "-o", "hdmi"], stdout = PIPE, stderr = PIPE, stdin = PIPE)
    player.communicate()
    print "After: " + video_file
    print player.pid

def is_video_playing():
    for process in Popen(["ps", "ax"], stdout = PIPE).stdout:
        if "omxplayer" in process:
                return True
    return False


if __name__ == "__main__":
    first_run = True;
    configuration_json = json.load(open("Configuration.json"))
    print configuration_json