import pygame, sys
from pygame.locals import *

width = 1280
height = 960

menuinput = 0

pygame.init()
Display = pygame.display.set_mode((width,height))
TestTitle = pygame.image.load('TestTitle.png')
pygame.display.set_caption('Pygame Main Menu Test')

while True:
	for Event in  pygame.event.get():
		if Event.type == QUIT:
			pygame.quit()
			sys.exit()

	Key = pygame.key.get_pressed()

	if Key[pygame.constants.K_UP]:
		menuinput -= 1
		menuinput = menuinput % 3
	elif Key[pygame.constants.K_DOWN]:
		menuinput += 1
		menuinput = menuinput % 3

	Display.fill(0x000000)
	Display.blit(TestTitle, (0,0))
	pygame.draw.rect(Display, 0xff0000, (480,640+(80*menuinput),320,80), 4)
	## Rect Tuple -> (start x, start y, width, height)
	pygame.display.update()
