'''

'''

import time
import turtle
from turtle import *

class World:
    #World-Object
    def __init__(self, width, height, color):#Sels is used to represent the instance of the class.
        # Initializes width, height and colors with values that are passed in as parameters.
        self.width = width
        self.height = height
        self.color =  color

    #World-Function[drawWorld]
    def drawWorld(self):
        #Draws the world on screen using setup and bgcolor functions [from_pygame's library]
        setup(self.width, self.height)
        bgcolor(self.color)


class Track:
    def __init__(self, length, width,color):
        #Define the length, width and color of the track
        self.width = width /2 #/2 => Divide the whole width of  canvas in n. Represents the length of the track [meters]
        self.length = length -100 #-100, margins from left to right of canvas. Represents the width of the track [meters]
        self.color = color# Track color( what color should be drawn on top of each square that makes up a track segment)

    def drawTrack(self):
        #Draw the track on screen
        penup()# Pull the pen up- no drawing when moving
        goto(-self.length/2, self.width/2)# Goto center of screen with x,y
        pendown()# Pull oen down- drawing when moving
        turtle.color(self.color)
        begin_fill()
        for i in range(2):# Repeat it 2 times
            forward(self.length)
            right(90)
            forward(self.width)
            turtle.right(90)
        end_fill()

    def drawFinishLine(self):
        # Draws finish Line
        #Use the penup() function to draw a shape of a square, and then use the tileSpace variable to calculate how many tiles are in each row and colum.
        penup()# Pull the pen up- no drawing when moving
        shape("square")
        tileSpace = self.width /20
        tileSize = tileSpace /20
        m =turtlesize(stretch_wid = tileSize)#Calculate the size of each tile using the turtleSize funciton with strech_wid as it's parameter
        lengthMod = self.length / 3

        for i in range(20):
            for j in range(2):
                # goto(lengthMod ,(self.width /2 - (i * tileSize * 2)))
                # stamp()
                color("yellow")
                #1.Goto the specified location in lenthMod and then draw a sqaure at that location using tileSpace as its width.
                #2.Go 2 steps back two steps and draw another square at that location using tileSpace as its width minus 1 from what was drawn before it.
                #3. Continues until there are 20 squares drawn on screen.
                #Draw a 20x20 square
                #5.
                goto(lengthMod + (tileSpace * (j -1)), ((self.width/2 - tileSpace /2)- (i * tileSpace)))
                stamp()#copy of the turtle shape onto the canvas at the current tutle's possition.

class Car:
    #Object of Car
    def __init__(self, carNumber, accelerate, decelerate, maxSpeed, color, trackLength):
        #Deefine the attributes of the car; speed accelerate, decelerate....
        self.carNumber = carNumber
        self.speedUp = accelerate
        self.speedDown = decelerate
        self.maxSpeed = maxSpeed
        self.color = color
        self.trackLength = trackLength
        self.speed = 0
        self.position = self.speed * 0
        self.horizontalPosition = (-trackLength/2) + 150
        self.verticalPosition= 100 * pow(-1, carNumber)

    #Car-Function[drawCar]
    def drawCar(self, deltaTime):
        #start by drawing a car shape
        self.position += self.speed * deltaTime
        penup()
        shape("carOutline")
        goto(self.horizontalPosition + (self.trackLength * self.position) /100, self.verticalPosition)
        stamp()
    #Car-Function [accelerate]
    def accelerate(self):
        print("forward")
        if self.speed < self.maxSpeed:#Increase speed until it reaches Max speed
            self.speed += int(self.speedUp * deltaTime)#Inscreases speed
            if self.speed > self.maxSpeed:#Speed has reached max speed
                self.speed = self.maxSpeed

    # Car-Function [decelerate]
    def decelerate(self):
        print("backward")
        if self.speed > 0:#Speed is Bigger than 0
            self.speed -= int(self.speedDown * deltaTime)#Decrease speed
            if self.speed < 0:#Speed is smaller than 0
                self.speed = 0

    # Car-Function [finishCheck]
    def finishCheck(self):
        print(f"Track Length: {self.trackLength}")
        print(f"Speed: {self.speed}")
        #Check if the car's horizontal position is greater than or equal to 3 and less than 2
        #Check if speed has reached 0, if not set speed to 0 and return False
        #Otherwise, retunr True, because they have finished playing successfully.
        if (self.trackLength * self.position)/100 + self.horizontalPosition > self.trackLength/3 and (self.trackLength * self.position)/100 + self.horizontalPosition < self.trackLength/2 :
            print("finish")
            goto(-100, 205)
            color("white")
            write("FINISH", font = ("century gothic", 100, "bold"))
            self.speed = 0
            return False
        return True


#Create "compound"shape
square1 = ((-10, -20),(10, -20),(10, 20),(-10,20))#Coordinantes for compound shape
square2 = ((-5, -10),(5, -10),(5, 10),(-5,10))
s = Shape("compound")
s.addcomponent(square1, "white", "black")
s.addcomponent(square2, "white", "black")
register_shape("carOutline", s)#Register "carOutline"with compound shape

#Create a turtle object
screen = turtle.Screen()
screen.listen()

finalCheck = time.time()

speed(0)#Cars at rest before race begins
raceLocation = World(1200, 720, "green")#Set to match those of te screeen's dimensions
raceTrack = Track(raceLocation.width, raceLocation.height,"black")
car1 = Car(1, 55, 100, 10, "white", raceTrack.length)
car2 = Car(2, 55, 40, 10, "red", raceTrack.length)#
raceLocation.drawWorld()#Draws  objects onto screen using drawWorld()
raceTrack.drawTrack()#Draws objects onto screen using drawTrack()
raceTrack.drawFinishLine()#Draws  objects onto screen using drawFinishLine()

#Variable of Car1
screen.onkey(car1.accelerate, 'z')#Declares a funciton that takes one argument: the keycode
screen.onkey(car1.decelerate, 'a')#Declares a funciton that takes one argument: the keycode
#Variable of Car2
screen.onkey(car2.accelerate, 'k')#Declares a funciton that takes one argument: the keycode
screen.onkey(car2.decelerate, 'm')#Declares a funciton that takes one argument: the keycode

#
currentTime = time.time()
deltaTime = currentTime - finalCheck #The difference between current and last
finalCheck = currentTime#FinalCheck will be currentTime which is equivalent to now

car1.drawCar(deltaTime)#Draw car 1 at deltaTime[Movement]
car2.drawCar(deltaTime)#Draw car 1 at deltaTime[Movement]

state = True #Set state to true
# state = finishLineCheck

while state:
    #While-loop will keep running until return False/ state = False
    currentTime = time.time()#Set's up a new time for when the program will start checking again after finish drawing cars
    deltaTime = currentTime - finalCheck#Represents how much time has passed since the last check was done
    finalCheck = currentTime#Index into list of car, to know which are finished checkin first

    #- starts by checking if the state variable is True or False.
    #- If it is True then it will check if the time has changed since last time.
    #- If it has changed then it will update the deltaTime variable with a new value of currentTime minus lastCheck.
    #- It will also set FinalCheck equal to currentTime so that we can compare them later on when we are done drawing the cars.
    car1.drawCar(deltaTime)
    car2.drawCar(deltaTime)
    state = car1.finishCheck()
    state = car2.finishCheck()

done()


# for i in range(20):
#             for j in range(2):
#                 if (i % 2) == 0 and (j % 2) == 0:
#                     color("yellow")
#                     goto(length_mod + (tile_space * (j-1)), ((self.width/2 - tile_space/2) - (i * tile_space)))
#                     stamp()
#                 if (i % 2) == 0 and (j % 2) == 1:
#                     color("black")
#                     goto(length_mod + (tile_space * (j-1)), ((self.width/2 - tile_space/2) - (i * tile_space)))
#                     stamp()
#                 if (i % 2) == 1 and (j % 2) == 0:
#                     color("black")
#                     goto(length_mod + (tile_space * (j-1)), ((self.width/2 - tile_space/2) - (i * tile_space)))
#                     stamp()
#                 if (i % 2) == 1 and (j % 2) == 1:
#                     color("yellow")
#                     goto(length_mod + (tile_space * (j-1)), ((self.width/2 - tile_space/2) - (i * tile_space)))
#                     stamp()