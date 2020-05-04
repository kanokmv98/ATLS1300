#==============================================================================
#PC09 - SoundWave Part 2
#Kanok Vannavong, Jasmine Chittarath
#Created March 18, 2020
#Edited March 31, 2020

#this script will  have circles  on a black screen will grow in size based on
#   sound and move in a circle
#==============================================================================

#PSUEDOCODE:
#Using pygame, 
#the circle will change color and expand
#music will be imported

#PSEUDOCODE W/ LAYOUTS
#import pygame
#import mixer
#import a hot bopping song
#import black screen
#import circle via function
    #circle grows & expands while changing color

#------------------------------------------------------------------------------

import pygame
from random import *
import numpy as np
#modified from example
pygame.mixer.init(44100, -16,2,2048)

#--------------add music-------------------------------------------------------

music = pygame.mixer.music.load('Friends.ogg') #puts the song up on the queue
#pygame.mixer.music.play(-1) #repeats the music #moved for PC09

#--------------defining global variables----------------------------------------------

theta = np.linspace(0,6*np.pi, 200)
run = True
size = (600,600) #change this to change your screen size
screen = pygame.display.set_mode(size)
clock= pygame.time.Clock() #to set the speed of the game

x = randint(100,500)
y = randint(100,500)
r1 = 20
r2 = 20
s= 100
black = (0,0,0)
screen.fill(black)

#--------------define functions------------------------------------------------

def drawCircle(r,x,y): #draws circle 1
    for i in range(3):
        color = (randint(0,255),randint(0,255),randint(0,255))
        pygame.draw.circle(screen,color,(x,y),r)

#from Anim.py example   
def circPath(screen,x0,y0,r,theta, rr):  
    '''Create the circular path for my shape, and call the shape drawing function'''  
    x = r * np.cos(theta) + x0
    y = r * np.sin(theta) + y0  
    drawCircle(rr, x=int(x), y=int(y))  
    #return x,y

def moveIt(x0, y0, rr):
    circPath(screen, x0, y0, 30, theta[i], rr)

   
#--------------define local variables------------------------------------------
        
thres = 100 #sets the threshold for the shapes
i = 0

#game loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            
    #add animations, call functions to generate animations here
    screen.fill(black)
    moveIt(200,200, r1)
    i += 1 #move to the next angle, and calculate position again  
    if i >= len(theta):    
        i = 0
    r1 += 1
    moveIt(400,400, r1)
    i += 1 #move to the next angle, and calculate position again  
    if i >= len(theta):    
        i = 0
    r1 += 1
    
    #from PC08, music play event is moved here to be triggered by animation
    #once the circles reach a certain size, the music will play and more animations will happen
    if r1 == thres:
        pygame.mixer.music.play(-1) #repeats the music
        
    if r1 >= thres:
        moveIt(200,400, r2)
        i += 1 #move to the next angle, and calculate position again  
        if i >= len(theta):    
            i = 0
        r2 += 1
        moveIt(400,200, r2)
        i += 1 #move to the next angle, and calculate position again  
        if i >= len(theta):    
            i = 0
        r2 += 1
        
    clock.tick(15) #sets the speed of the game
      
    pygame.display.update() #updates screen
  
pygame.quit() #clean up if you exit the while loop