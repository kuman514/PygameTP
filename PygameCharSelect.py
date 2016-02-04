#imported by PygameMainMenuTest.py
import pygame, sys
from time import sleep
from pygame.locals import *

def CharSelect(Display):
	CharCur = 0;
	TestCharSel = pygame.image.load('TestCharSel.png')
	while True:
		for Event in pygame.event.get():
			if Event.type == QUIT:
				pygame.quit()
				sys.exit()

		Display.fill(0x000000)
		Display.blit(TestCharSel, (0,0))
		pygame.draw.rect(Display, 0x0000ff, (80+(400*CharCur),180,320,600), 4)
		
		sleep(0.13)
		k = pygame.key.get_pressed()
		if k[pygame.constants.K_LEFT]:
			CharCur -= 1
			CharCur %= 3
			# left
		elif k[pygame.constants.K_RIGHT]:
			CharCur += 1
			CharCur %= 3
			# right
		elif k[pygame.constants.K_RETURN]:
			if CharCur == 0:
				print 'Guy 1'
			elif CharCur == 1:
				print 'Guy 2'
			elif CharCur == 2:
				print 'Guy 3'
			return CharCur

		pygame.display.update()
