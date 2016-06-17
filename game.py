#SETUP

import pygame

pygame.init()

#screen resolution and caption
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

#initialise some colours
black = (0,0,0)
white = (255,255,255)


#initialise clock
clock = pygame.time.Clock()

crashed = False

#initialise car image
carImg = pygame.image.load('racecar.png')

#display car
def car(x,y):
	gameDisplay.blit(carImg, (x,y))
	
#starting point for car
x = (display_width * 0.45)
y = (display_height * 0.8)

########################################################

#GAME LOOP

while not crashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
			
		gameDisplay.fill(white)
		car(x,y)
		
	pygame.display.update()
	clock.tick(60)
	
pygame.quit()
quit()