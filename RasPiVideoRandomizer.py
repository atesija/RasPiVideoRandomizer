import glob
import os
import re
import random

def VideoContainsString(video_filename, strings):
    return any(string in video_filename for string in strings)
    
def WhitelistVideos(video_list, whitelist_strings):
    return [video for video in video_list if VideoContainsString(video, whitelist_strings)]
    
def BlacklistVideos(video_list, blacklist_strings):
    return [video for video in video_list if not VideoContainsString(video, blacklist_strings)]

def FileIsVideo(filename):
    video_file_endings = [".mp4", ".avi", ".mkv", ".mov", ".ogm"]
    return any(video_file in filename for video_file in video_file_endings)

def GetVideosFromLocation(folder_path):
    videos = []
    for root, dirs, files in os.walk(folder_path):
        videos.extend([os.path.join(root, f) for f in files if FileIsVideo(f)])
    return videos

def RandomizeVideos(video_list):
    random.shuffle(video_list)

def BuildOrderVideoOrder(order_template):
    video_order = []
    for option in order_template:
        if("repeat" in option):
            repeat_amount = [int(s) for s in option.split() if s.isdigit()]
            for _ in range(random.randint(repeat_amount[0], repeat_amount[1]) - 1):
                video_order.append(video_order[-1])
        elif("chance" in option):
            chance_to_stay = [int(s) for s in option.split() if s.isdigit()]
            if(random.randint(0, 100) >= chance_to_stay[0]):
                del video_order[-1]
        else:
            video_order.append(option)
    return video_order
    
print GetVideosFromLocation("/media/pi/WindFish/Videos/Shows")
