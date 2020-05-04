#============================================================================#
#PC03 - Generative Art
#Kanok Vannavong
#created February 7, 2020

#this code was originally built to generate random clouds across
#a sky, but with the randomization of the shapes, this code now pops
#random popcorn shapes into a popcorn bucket/popcorn machine backgound
#============================================================================#

#importing libraries
from turtle import * 
from random import *

window = Screen() #creating a screen
window.bgcolor('#C03221') #setting the background color
window.update() #updates to draw any changes made to the canvas

#creating turtles
corn = Turtle()
corn.shape("turtle")
corn.speed(0)

stripe = Turtle()
stripe.shape("circle")
stripe.color("#A82A1C")
stripe.speed(0)

#list of colors to refer to later
colors = ["#FEFCAD", "#EADDA6", "#FFFAE2", "#FBFFFE", "#FBFFFE"]
          
#creating the stripes on the background to complete the circus ~look~
stripe.penup()
stripe.goto(-500, 400)
for i in range(4):
    stripe.seth(0)
    stripe.forward(100)
    stripe.right(90)
    stripe.width(80)
    stripe.pendown()
    stripe.forward(800)
    stripe.seth(0)
    stripe.forward(100)
    stripe.left(90)
    stripe.forward(800)
          
#for loops that generate the popcorn
for b in range(6):
    #for loop to iterate through the list of colors
    for i in range(5):
        randx = randint(-300, 300)
        randy = randint(-300, 300)
        corn.penup()
        corn.goto(randx, randy)
        corn.pendown()
        corn.color(colors[i])
        corn.begin_fill()
        #for loop to generate the random popcorn shape
        for c in range(15):
            rrad = randint(10,40)
            rcir = randint(80, 200)
            rturn = randint(75, 120)
            corn.circle(rrad, rcir)
            corn.right(rturn)
        corn.end_fill()
        
corn.hideturtle()
#stopping the program from expecting commands
done()
 


