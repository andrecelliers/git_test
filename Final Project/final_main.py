#!usr/bin/python3

####################################
## Program: Spaceship Battle      ##
## Author:  Andre Celliers        ##
## Date:    Nov. 2022             ##
####################################

######################
## REQUIRED IMPORTS ##
######################
import pygame
import os
import datetime
from os import listdir
from os.path import isfile, join
pygame.init()
pygame.font.init()
pygame.mixer.init()

########################################
#####@@@@@ GLOBAL VARIABLES @@@@@#######
########################################
time = datetime.datetime.now()

###################
## GAME CONTROLS ##
###################
FPS = 60
VEL = 5
###########
## AUDIO ##
########### 
#SWORD_SWING = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
#SWORD_HIT = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))

#######################
## WINDOW PROPERTIES ##
#######################
WIDTH = 1200
HEIGHT = 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colosseum")
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'arena.png')), (WIDTH,HEIGHT))
BORDER = pygame.Rect(0,850,WIDTH, HEIGHT)

#############
## COLOURS ##
#############
GROUND = (243, 204, 161)

######################
## PLAYER CHARACTER ##
######################
GLAD_WIDTH = 55
GLAD_HEIGHT = 40
GLADIATOR = pygame.image.load(os.path.join('Assets','Gladiator','glad_test.png'))
GLADIATOR_LOCATION = pygame.Rect(700,300, GLAD_WIDTH, GLAD_HEIGHT)

###############################
#####@@@@@ FUNCTIONS @@@@@#####
###############################

####################
## WINDOW DRAWING ##
####################
def draw_window():
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN,GROUND,BORDER) # Draw border
    WIN.blit(GLADIATOR,(GLADIATOR_LOCATION.x,GLADIATOR_LOCATION.y))

    pygame.display.update()

#####################
## PLAYER MOVEMENT ##
#####################
def gladiator_movement(keys_pressed,GLADIATOR):
    """ Controls movement of yellow ship
    :return: None
    """
    if keys_pressed[pygame.K_LEFT] and GLADIATOR.x - VEL > BORDER.x +10: # MOVE RED LEFT
        GLADIATOR_LOCATION.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and GLADIATOR.x + VEL < WIDTH - GLAD_HEIGHT - 10: # MOVE RED RIGHT
        GLADIATOR_LOCATION.x += VEL
    if keys_pressed[pygame.K_UP] and GLADIATOR.y - VEL > 0: # MOVE RED UP
        GLADIATOR_LOCATION.y -= VEL
    if keys_pressed[pygame.K_DOWN] and GLADIATOR.y + VEL < HEIGHT - GLAD_WIDTH: # MOVE RED DOWN
        GLADIATOR_LOCATION.y += VEL



##############################
## BACKGROUND TILE FUNCTION ##
##############################
# def get_background(name):
#     image =  pygame.image.load(join("assets", "Background", name))
#     _, _, width, height = image.get_rect()
#     tiles = []

#     for i in range(WIDTH // width + 1):
#         for j in range(HEIGHT // height +1):
#             pos = (i * width, j * height)
#             tiles.append(pos)

#     return tiles, image
 


###################
## MAIN FUNCTION ##
###################
def main():
    clock = pygame.time.Clock()
    GLADIATOR = pygame.Rect(700, 300, GLAD_WIDTH, GLAD_HEIGHT)

    run = True

    while run:
        clock.tick(FPS) # SET MAX SPEED OF GAME THROUGH FPS VARIABLE

        # LOOK FOR EVENTS CALLED BY PGAME DURING GAMEPLAY
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


        keys_pressed = pygame.key.get_pressed() #Pygame detecting pressed keys
        gladiator_movement(keys_pressed,GLADIATOR) #check if keys controlling yellow are pressed



        # Do logical updates here.
        # ...

        #screen.fill("purple")  # Fill the display with a solid color

        # Render the graphics here.
        # ...

        #pygame.display.flip()  # Refresh on-screen display
        #clock.tick(60)         # wait until next frame (at 60 FPS)
        draw_window()

##################
## MAIN PROGRAM ##
##################
if __name__ == "__main__":
    main()


