import pygame, sys
from pygame.locals import *

pygame.init()
width = 1280
height = 960
SCREEN = pygame.display.set_mode([width,height])
pygame.display.set_caption('kumankoishi.py')

pygame.mixer.music.load("AllScratchingWorld.mp3")
pygame.mixer.music.play(-1,0)

testimg = pygame.image.load("skeleton.png")

while True:
    for EVENT in pygame.event.get():
        if EVENT.type == QUIT:
            pygame.quit()
            sys.exit()
	
	k = pygame.key.get_pressed()
	if k[pygame.constants.K_r]:
		pygame.mixer.music.rewind()
	
	SCREEN.fill((0,0,0))
	SCREEN.blit(testimg, (0,0))
    pygame.draw.circle(SCREEN, 0x00ff00, (width/2,height/2), 300, 2)
    pygame.draw.rect(SCREEN, 0xff0000, (500,500,300,500), 0)
    pygame.display.update()
