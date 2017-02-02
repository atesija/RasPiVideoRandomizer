import pygame, time, sys

pygame.init()

size = width, height = 0, 0
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

song = "/media/pi/Windfish/Music/Animal Crossing/Animal Crossing (GC Rip)/75 Rainy Day.mp3"
pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play()

timeBetweenTextChange = 2.5
exampleBump = []
exampleBump.append(("Knock knock", timeBetweenTextChange))
exampleBump.append(("...", timeBetweenTextChange))
exampleBump.append(("Orange", timeBetweenTextChange))
exampleBump.append(("...", timeBetweenTextChange))
exampleBump.append(("Orange ya glad I didn't say banana?", timeBetweenTextChange))

info = pygame.display.Info()

font = pygame.font.Font(None, info.current_h / 5)

for bumppart in exampleBump:
    screen.fill(black)
    text = font.render(bumppart[0], True, white)
    textrect = text.get_rect()
    screen.blit(text, textrect)
    pygame.display.flip()
    time.sleep(bumppart[1])

logo = pygame.image.load("Logo.png")
logorect = logo.get_rect()
screen.fill(black)
screen.blit(logo, logorect)
pygame.display.flip()

pygame.mixer.music.fadeout(2000)
time.sleep(2)
#running = True
#while(running):
#    for(event in pygame.event.get():
#        if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
#            running = False

pygame.quit()
sys.exit()
