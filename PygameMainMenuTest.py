import pygame, sys, time
from pygame.locals import *
import PygameCharSelect

width = 1280
height = 960

menuinput = 0

pygame.init()

Display = pygame.display.set_mode((width,height))
TestTitle = pygame.image.load('TestTitle.png')
## load an image file

pygame.display.set_caption('Pygame Main Menu Test')

while True:
	for Event in pygame.event.get():
		if Event.type == QUIT:
			pygame.quit()
			sys.exit()

	Display.fill(0x000000)
	Display.blit(TestTitle, (0,0))
	pygame.draw.rect(Display, 0xff0000, (480,640+(80*menuinput),320,80), 4)
	## Rect Tuple -> (start x, start y, width, height)
	
	time.sleep(0.13)
	
	Key = pygame.key.get_pressed()
	if Key[pygame.constants.K_UP]:
		menuinput -= 1
		menuinput = menuinput % 3
	elif Key[pygame.constants.K_DOWN]:
		menuinput += 1
		menuinput = menuinput % 3
	elif Key[pygame.constants.K_RETURN]:
		if menuinput == 0:
			game = PygameCharSelect.CharSelect(Display)
			print 'game start %d' % (game + 1)
			# you can try below ones :
			# game = PygameCharSelect.CharSelect(Display)
			# Game.Play(game)
		elif menuinput == 1:
			print 'instructions'
		elif menuinput == 2:
			print 'game quit'
			pygame.quit()
			sys.exit()

	pygame.display.update()
