import pygame
import time
import sys
import random
import json
from FileFinder import get_files_of_type_from_folders

def play_lineup(channel_json, upcoming_video_list):
    pygame.init()
    random.seed()

    #We don't want to see the mouse over the bump
    pygame.mouse.set_visible(False)

    #Set up the screen
    size = 0, 0
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h

    #Open a random music file and play it
    pygame.mixer.init()
    if channel_json:
        configuration_json = json.load(open(channel_json))  
        song = random.choice(get_files_of_type_from_folders(configuration_json["folders"]["music"], ".mp3"))
        song = song.rstrip()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

    #Set up font
    white = 255, 255, 255
    font = pygame.font.Font(None, screen_height / 10)

    #Announce the lineup
    announcement_text = ["Tonight's lineup:", "Coming up:", "Here's what's next:"]
    black = 0, 0, 0
    screen.fill(black)
    text = font.render(random.choice(announcement_text), True, white)
    textrect = text.get_rect(center = (screen_width / 2, screen_height / 2))
    screen.blit(text, textrect)
    pygame.display.flip()
    time.sleep(3)
    
    #Loop through each part of the bump and display it for the proper time
    for video_file_name in upcoming_video_list:
        screen.fill(black)
        text = font.render(video_file_name, True, white)
        textrect = text.get_rect(center = (screen_width / 2, screen_height / 2))
        screen.blit(text, textrect)
        pygame.display.flip()
        time.sleep(3)

    #Display the logo at the end 
    logo = pygame.image.load("Logo.png")
    logo = pygame.transform.scale(logo, (int(screen_width / 3.5), int(screen_height / 3.5)))
    logorect = logo.get_rect(center = (screen_width / 2, screen_height / 2))
    screen.fill(black)
    screen.blit(logo, logorect)
    pygame.display.flip()

    #Fade msuic out, wait, then exit
    pygame.mixer.music.fadeout(2000)
    time.sleep(2)

    pygame.quit()
    #sys.exit()

if __name__ == '__main__':
    play_lineup(None, [])
