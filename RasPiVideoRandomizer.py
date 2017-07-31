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

    
print GetVideosFromLocation("/media/pi/WindFish/Videos/Shows")
