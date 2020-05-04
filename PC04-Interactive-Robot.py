#=====================================================#
#PC04 - Interactive Robot
#Kanok Vannavong, Jasmine Chittarath
#created February 14, 2020

#this code creates two robots with pygame that with key presses,
#can move, change size, and change color
#=====================================================#

import pygame
from random import *
import time
#entire script modified from class example script:
#https://cdn.inst-fs-iad-prod.inscloudgate.net/c49397e8-d940-418c-b465-55634e4b09af/Robot.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9jNDkzOTdlOC1kOTQwLTQxOGMtYjQ2NS01NTYzNGU0YjA5YWYvUm9ib3QucHkiLCJ0ZW5hbnQiOiJjYW52YXMiLCJ1c2VyX2lkIjoiMTA3NzIwMDAwMDAwMjcwODkyIiwiaWF0IjoxNTg4NTY3ODgxLCJleHAiOjE1ODg2NTQyODF9.FmHCylnkKWz2omiw4L8SnUxjhl5QHBHu9Yzalzu4r3cdRgEMOYtTnySQYSvKJOUKlCD6dbv-y2OtZgQAmCWMJQ&content_type=text%2Fx-python-script

#set up colors
BLACK = (0,0,0)
RED = (255,0,0)
PINK = (170,0,50)
GREEN = (0,255,0)
BLUE = (0,0,255)
LT_BLUE = (0, 100, 255)
WHITE = (255,255,255)
GRAY = (127,127,127)
DK_GRAY = (100,100,100)
#adding more colors of choice
MANGO = (233,180,76)
ROSE = (139,87,92)

#create screen and game variables
size = 500
screen = pygame.display.set_mode((size,size)) #create 500 x500 pixel screen

run = True
x = size/2 #center position for all robot parts or first robot
y = size/2
#variable positions for my second robot parts
w = size/2
z = size/2

#variables to be used for key-press interactions
speed = 2
eye_r = 2
rSize = 50
wSize = 20
pSize = 3
rColor = GRAY

#Robo features
blink = [GREEN, BLUE, RED, LT_BLUE]
color = choice(blink) #assign a value to color
colorL = choice(blink) #assign a value to color
colorR = choice(blink) #assign a value to color

#Game loop
while run:
    #control the speed of movement for the robot
    time.sleep(.01)
    # create exit-on click detection:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            
    #Drawing goes from bottom to top. We'll make our screen white first, then
    #add the robo-parts.    
    screen.fill(WHITE)
    
#---creating keypress commands-------------------------------------------------
    
    #from pc04 video tutorial
    keys = pygame.key.get_pressed() #checks for any keys being pressed
    #movements for first robot using arrow keys
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed  
    #movements for second robot using AWDS keys
    if keys[pygame.K_d]:
        w += speed
    if keys[pygame.K_a]:
        w -= speed
    if keys[pygame.K_w]:
        z -= speed
    if keys[pygame.K_s]:
        z += speed  
    
    #changing parts of the robots to get bigger by clicking the spacebar
    #sizes will toggle between larger and normal size with each key press
    #modified from PC04 video tutorial
    if keys[pygame.K_SPACE]:
        if rSize <=50:
            rSize += 10
        elif rSize > 50:
            rSize -= 10
        if wSize <= 20:
            wSize += 10
        elif wSize > 20:
            wSize -= 10
        if eye_r <= 2:
            eye_r += 4
        elif eye_r > 2:
            eye_r -= 4
        if pSize <= 3:
            pSize += 3
        elif pSize > 3:
            pSize -= 3
    
    #toggles robot colors between 4 colors when Enter is pressed
    #pygame color docs: https://www.pygame.org/docs/ref/color.html
    if keys[pygame.K_RETURN]:
        if rColor == GRAY:
            rColor = PINK
        elif rColor == PINK:
            rColor = ROSE
        elif rColor == ROSE:
            rColor = MANGO
        elif rColor == MANGO:
            rColor = GRAY

#---drawing my robots----------------------------------------------------------

    #Pygame draw docs: https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    #first robot
    Head = pygame.draw.rect(screen,rColor,(x-25,y-90,rSize,rSize)) 
    Body = pygame.draw.polygon(screen, rColor, [(x+35, y-35),(x+45,y+35), (x-45,y+35),(x-35, y-35)])
    L_eye = pygame.draw.circle(screen, GREEN, (int(x-10), int(y-70)),eye_r)
    R_eye = pygame.draw.circle(screen, GREEN, (int(x+10), int(y-70)),eye_r)
    panelLights1 = pygame.draw.circle(screen, colorR, (int(x+20), int(y-5)),pSize)
    panelLights2 = pygame.draw.circle(screen, color, (int(x), int(y-5)),pSize)
    panelLights3 = pygame.draw.circle(screen, colorL, (int(x-20), int(y-5)),pSize)

    L_wheel = pygame.draw.circle(screen, BLACK, (int(x-40), int(y+63)),wSize)
    R_wheel = pygame.draw.circle(screen, BLACK, (int(x+40), int(y+63)),wSize)
    L_hub = pygame.draw.circle(screen, DK_GRAY, (int(x-40), int(y+63)),10)
    R_hub = pygame.draw.circle(screen, DK_GRAY, (int(x+40), int(y+63)),10)
    Track = pygame.draw.ellipse(screen, DK_GRAY, (int(x-65), int(y+33),130,60),2)
    
    #second robot
    Head2 = pygame.draw.rect(screen,rColor,(w-25,z-90,rSize,rSize)) 
    Body2 = pygame.draw.polygon(screen, rColor, [(w+35, z-35),(w+45,z+35), (w-45,z+35),(w-35, z-35)])
    L_eye2 = pygame.draw.circle(screen, GREEN, (int(w-10), int(z-70)),eye_r)
    R_eye2 = pygame.draw.circle(screen, GREEN, (int(w+10), int(z-70)),eye_r)
    panelLights12 = pygame.draw.circle(screen, colorR, (int(w+20), int(z-5)),pSize)
    panelLights22 = pygame.draw.circle(screen, color, (int(w), int(z-5)),pSize)
    panelLights32 = pygame.draw.circle(screen, colorL, (int(w-20), int(z-5)),pSize)

    L_wheel2 = pygame.draw.circle(screen, BLACK, (int(w-40), int(z+63)),wSize)
    R_wheel2 = pygame.draw.circle(screen, BLACK, (int(w+40), int(z+63)),wSize)
    L_hub2 = pygame.draw.circle(screen, DK_GRAY, (int(w-40), int(z+63)),10)
    R_hub2 = pygame.draw.circle(screen, DK_GRAY, (int(w+40), int(z+63)),10)
    Track2 = pygame.draw.ellipse(screen, DK_GRAY, (int(w-65), int(z+33),130,60),2)

    pygame.display.update() #update all changes to screen
