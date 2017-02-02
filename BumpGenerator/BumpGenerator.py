import pygame
import time
import sys

pygame.init()

pygame.mouse.set_visible(False)

black = 0, 0, 0
white = 255, 255, 255

size = 0, 0
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h

song = "/media/pi/Windfish/Music/Animal Crossing/Animal Crossing (GC Rip)/75 Rainy Day.mp3"
pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play()

#debug bump
timeBetweenTextChange = 2.5
exampleBump = []
exampleBump.append(("Knock knock", timeBetweenTextChange))
exampleBump.append(("...", timeBetweenTextChange))
exampleBump.append(("Orange", timeBetweenTextChange))
exampleBump.append(("...", timeBetweenTextChange))
exampleBump.append(("Orange ya glad I didn't say banana?", timeBetweenTextChange))

font = pygame.font.Font(None, screen_height / 10)

for bumppart in exampleBump:
    screen.fill(black)
    text = font.render(bumppart[0], True, white)
    textrect = text.get_rect(center = (screen_width / 2, screen_height / 2))
    screen.blit(text, textrect)
    pygame.display.flip()
    time.sleep(bumppart[1])

logo = pygame.image.load("Logo.png")
logorect = logo.get_rect(center = (screen_width / 2, screen_height / 2))
screen.fill(black)
screen.blit(logo, logorect)
pygame.display.flip()

pygame.mixer.music.fadeout(2000)
time.sleep(2)

pygame.quit()
sys.exit()
