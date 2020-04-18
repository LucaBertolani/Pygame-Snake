# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:33:23 2020

@author: lucab
"""

# Simple pygame program

# Import and initialize the pygame library
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
x=SCREEN_WIDTH/2
y=SCREEN_HEIGHT/2
dx=0
dy=0
initialspeed=20
#coordinates for random food popup
foodx =  round(random.randrange(0, SCREEN_WIDTH)/10)*10 #THIS WEIRD WAY OF DEFINING THE 
foody =  round(random.randrange(0,SCREEN_HEIGHT)/10)*10#POSITION IS VERY IMPORTANT FOR THE CODE
#set quantities and function for snake enlargement script
def our_snake(snake_list): 
    for k in snake_list:
        pygame.draw.rect(screen, (100,100,255), [k[0], k[1], 10, 10])
snake_List = []
Length_of_snake = 1
snake_Head = []
# Variable to keep the main loop running
running = True
clock = pygame.time.Clock()
# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            elif event.key==K_UP:
                dy=-10
                dx=0
            elif event.key==K_DOWN:
                dy=10
                dx=0
            elif event.key==K_LEFT:
                dx=-10
                dy=0
            elif event.key==K_RIGHT:
                dx=10
                dy=0
        
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
    if x==SCREEN_WIDTH: #BOUNDARY CONDITIONS
        x=0+10
    if x==0:
        x=SCREEN_WIDTH-10
    if y==SCREEN_HEIGHT:
        y=0+10
    if y==0:
        y=SCREEN_HEIGHT -10         
    
    x=x+dx #MOVEMENT
    y=y+dy 
    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,255,255),[foodx,foody,10,10])#FOOD POP-UP
    snake_Head = []
    snake_Head.append(x)
    snake_Head.append(y) #THIS THREE LINES FOLLOW THE MOVEMENT OF THE SNAKE IN A LIST
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0] #THIS KEEPS REFRESHING THE LIST SO IT ONLY HAS THE CURRENT 
                              #SNAKE POSTIONS
 
    for s in snake_List[:-1]: 
        if s == snake_Head:     #accounts for self-bite
            running = False
 
    our_snake(snake_List)  #ACTUALLY DRAWS THE additional length
 
    pygame.display.update()   

    if x == foodx and y == foody:    #food eating
        foodx =  round(random.randrange(0, SCREEN_WIDTH)/10)*10 #new food popup
        foody =  round(random.randrange(0,SCREEN_HEIGHT)/10)*10
        Length_of_snake =Length_of_snake+1 #snake enlargement
        initialspeed=initialspeed+2
    clock.tick(initialspeed) #DEFINES SPEED OF SNAKE
    
pygame.quit()
quit()    



 


    