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
    video_file_endings = [".mp4", ".avi", ".mkv", ".mov"]
    return any(video_file in filename for video_file in video_file_endings)

def GetVideosFromLocation(folder_path):
    videos = []
    for root, dirs, files in os.walk(folder_path):
        videos.extend([f for f in files if FileIsVideo(f)])
    return videos

allimages = []
for root, dirs, files in os.walk("C:/Users/a.tesija/Desktop"):
    images = [f for f in files if ".mp4" in f]
    allimages.extend(images)
print allimages
random.shuffle(allimages)
print allimages
print VideoContainsString(allimages[0], "ios")
print BlacklistVideos(allimages, ["ois", 'ios'])
print FileIsVideo("hi.png")
print FileIsVideo(allimages[0])
print GetVideosFromLocation("C:/Users/a.tesija/Desktop")
