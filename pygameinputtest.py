import pygame, sys
from pygame.locals import *

pygame.init()
width = 1280
height = 960
display = pygame.display.set_mode([width,height])
pygame.display.set_caption('Pygame Input Test')

while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
            sys.exit()
    k = pygame.key.get_pressed()
    if k[pygame.constants.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    pygame.display.update()
