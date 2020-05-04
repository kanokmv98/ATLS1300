#=====================================================#
#PC05 - Bubble Click Game
#Kanok Vannavong, Jasmine Chittarath
#created February 21, 2020

#This script will create a bubbles that randomly bumbles about
#Users can click and drag bubbles to remove them from the display to win the game.
#=====================================================#

import pygame
from random import *
#base script from in class example script (2/18 & 2/20)
#https://cdn.inst-fs-iad-prod.inscloudgate.net/fef24c56-8b39-4fe5-bd2e-9da829c4f1f1/pygameDragIC.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9mZWYyNGM1Ni04YjM5LTRmZTUtYmQyZS05ZGE4MjljNGYxZjEvcHlnYW1lRHJhZ0lDLnB5IiwidGVuYW50IjoiY2FudmFzIiwidXNlcl9pZCI6IjEwNzcyMDAwMDAwMDI3MDg5MiIsImlhdCI6MTU4ODU1MTQwNSwiZXhwIjoxNTg4NjM3ODA1fQ.diX3B2BvJHRVSBPM-fzUUAcZjN1H9Ro5ETnQZ4WlsXkD7yBBjzmqxJxvXglbVhnZsK3fwZYhKWFbS26JwElLJg&content_type=text%2Fx-python-script
#https://cdn.inst-fs-iad-prod.inscloudgate.net/c3f42e78-5f3b-4b9d-b756-6c30c55bc5d0/pygameCirclesFunc.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9jM2Y0MmU3OC01ZjNiLTRiOWQtYjc1Ni02YzMwYzU1YmM1ZDAvcHlnYW1lQ2lyY2xlc0Z1bmMucHkiLCJ0ZW5hbnQiOiJjYW52YXMiLCJ1c2VyX2lkIjoiMTA3NzIwMDAwMDAwMjcwODkyIiwiaWF0IjoxNTg4NTY2ODUzLCJleHAiOjE1ODg2NTMyNTN9.U6xhW4zV2jwtOpUS2AbMmaFf72BKrouTwPt5q7HuN_33AwziIvzg1r_RgStl1l8xIWtuC7uV9erNvusXWmCalA&content_type=text%2Fx-python-script

pygame.init() #initialize all the pygame functions
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption('Bubble Click Game')

#--------------------defining variables----------------------------------------

Run = True
drag = False #boolean that determines if dragging happens
x = 400 #where we want to draw stuff
y = 400 
step = 5

bckground = (178,103,94)

gColor = (159,164,169)
gSize = 100
vel = 5
x1 = 0
y1 = 0
rr = 100

#--------------------define functions------------------------------------------

#function for drawing bubbles
def makeBubbles():
    r = randint(10,20)
    pygame.draw.circle(screen, (0,0,0), (rectList[i].x + speed[0], rectList[i].y+speed[1]), r) 

#function to be called during collision detection
def collision(obj):
    print("Score!")
    rectList.remove(obj)
    print("Bubbles left:") #Keeping track of how many Bubbles are left
    print(len(rectList))
    return (len(rectList))

#function to be called once the game is over
def end():
    #0.1 pts - Use an if statement that tests the score variable to see if all the bubbles have been removed.
    if len(rectList) == 0:
            print("You win!")

#------------------------------------------------------------------------------

#create goal
goal = pygame.Rect(x1, y1, rr, rr)

#create RectList for our circles to sit on
numCirc = randint(30,50)
print("Directions: Click and drag bubbles to the grey box to get rid of them. Clear the window to win!")
print("Number of bubbles to get rid of:")
print(numCirc)
rectList = [] #for storing rect objects
for i in range(numCirc):
    randx = randint(100,600)
    randy = randint(100,600)
    r = randint(10,20)
    rectList.append(pygame.Rect(randx,randy,r*2,r*2)) #we're setting a rectangle underneath our circle
    #the r is the circle  RADIUS, but we want the rect with to be equal to DIAMETER, so:
    #diameter = radius * 2


#start the game loop!
while Run: 
    
    for event in pygame.event.get(): #scan all events --things happening outside python (mouse and keyboard actions)
        if event.type == pygame.QUIT:
            pygame.quit() #add a quit function so it stops up background tasks
    
#--------------mousepress detections-------------------------------------------
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #get our x and y positions of where the click happened
            for i in range(len(rectList)):
                if rectList[i].collidepoint(pos[0],pos[1]):
                    drag = True #whenever the mouse is down, we can potentially drage our shape
                    selected = i
                    print("Selected:")
                    print(selected)
                    offsetX = rectList[i].x - pos[0] #let's calculate the difference between where the rectangle is and where the click happened
                    offsetY = rectList[i].y - pos[1]
            
        elif event.type == pygame.MOUSEMOTION:
                if drag: #remember drag is a boolean, and if statements want to know if something is true or not...so we can just pass our variable here!
                    pos = event.pos #update position as mouse moves around
                    #update the position of the shape based on where the mouse motion event is happening (where the cursor is)
                    rect.x = pos[0] + offsetX 
                    rect.y = pos[1] + offsetY
                
        elif event.type == pygame.MOUSEBUTTONUP: #ok, now we're done dragging, so we want to detect when the mouse button is released.
            drag = False #we can set our boolean to false, so we can't update our Rect position.

#----------------collision detection-------------------------------------------

        for rect in rectList:
            if goal.colliderect(rect):
                #the goal checks to see if rectList[i] is within its boundaries
                collision(rect)

#------------------------------------------------------------------------------

    speed = [randint(-step,step),randint(-step,step)] #random displacement to add fun wiggles to our circle. 
    
    screen.fill(bckground) #draw/redraw the screen to "erase" previous drawings

#---------drawing our objects--------------------------------------------------

    #drawing our objects on top of our rectangles
    pygame.draw.rect(screen,gColor,(goal.x, goal.y, gSize,gSize))
    for i in range(len(rectList)):
        makeBubbles()
    
    pygame.display.update() #update our image to our screen
    end()
    
