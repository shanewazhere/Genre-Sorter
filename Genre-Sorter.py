import pygame, sys, time
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Genre Sorter')

mousex, mousey = 0, 0
msg = 0

while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
		elif event.type == MOUSEBUTTONUP:
			mousex, mousey = event.pos
			if event.button in (1, 2, 3):
				msg = 'left, middle, or right mouse click'
			elif event.button in (4, 5):
				msg = 'mouse scrolled up or down'
				
		elif event.type == KEYDOWN:
			if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
				msg = 'Arrow key pressed'
			if event.key == K_a:
				msg = '"A" key pressed'
			if event.key == K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
			
				
			
			
		print msg
	pygame.display.update()
	fpsClock.tick(30)

