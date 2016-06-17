#SETUP

import pygame
import time

pygame.init()

#screen resolution and caption
display_width = 800
display_height = 400

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Runny')

#initialise some colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#initialise clock
clock = pygame.time.Clock()

crashed = False

#guy variables
guyImg = pygame.image.load('guy.png')
guy_height = 82
guy_width = 73

dotImg = pygame.image.load('dot.png')

#poop variables
poopImg = pygame.image.load('poop.png')
poop_height = 30
poop_width = 30

#display guy
def guy(x,y):
    gameDisplay.blit(guyImg, (x,y))
    gameDisplay.blit(dotImg, (x,y))
    
def poop(x,y):
    gameDisplay.blit(poopImg, (x,y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
    
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()
    
def crash():
    message_display('You Crashed')
    
def game_loop():
    guy_x = (display_width * 0.25)
    guy_y = (display_height * 0.7)

    guy_y_change = 0
    
    poop_x = (display_width*0.8)
    poop_y = (display_height*0.85)
    
    poop_x_change = -8

    gameExit = False
    guy_standing = True
    guy_jumping = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and guy_standing == True:
                    guy_standing = False
                    guy_jumping = True
                    guy_y_change = -20

        if guy_jumping == True and guy_y == 180:
            guy_y_change = 5
        elif guy_jumping == True and guy_y > 280:
            guy_y_change = 0
            guy_y = 280
            guy_jumping = False
            guy_standing = True
        elif guy_standing == True:
            guy_y_change = 0
            
        guy_y += guy_y_change
        
        if poop_x<0:
            poop_x = 820
            
        poop_x += poop_x_change
        
        if poop_x >= guy_x+15 and poop_x <= guy_x+guy_width-15 and poop_y >= guy_y and poop_y <= guy_y + guy_height:
            crash()

        gameDisplay.fill(white)
        guy(guy_x,guy_y)
        poop(poop_x,poop_y)

        pygame.display.update()
        clock.tick(60)



game_loop()
    
pygame.quit()
quit()