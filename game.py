#SETUP

import pygame

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

guyImg = pygame.image.load('guy.png')
guy_height = 82
guy_standing = True
guy_jumping = False

#display guy
def guy(x,y):
    gameDisplay.blit(guyImg, (x,y))
    
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
    x = (display_width * 0.25)
    y = (display_height * 0.7)

    y_change = 0

    gameExit = False
    guy_standing = True
    guy_jumping = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and guy_standing == True:
                    guy_standing = False
                    guy_jumping = True
                    y_change = -20

        if guy_jumping == True and y == 180:
            y_change = 5
        elif guy_jumping == True and y > 280:
            y_change = 0
            y = 280
            guy_jumping = False
            guy_standing = True
        elif guy_standing == True:
            y_change = 0
            
        y += y_change

        gameDisplay.fill(white)
        guy(x,y)

        pygame.display.update()
        clock.tick(60)



game_loop()
    
pygame.quit()
quit()