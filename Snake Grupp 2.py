import turtle as tl
import time
import random

delaySeconds = 0.1 #time.sleep() funktsiooni muutuja

#mänguaken
wn = tl.Screen()
wn.title("Sneik")
wn.setup(width = 600, height = 600)
wn.bgcolor("#000000")
wn.tracer(0)
pixel = 20

#ussi pea objekt
head = tl.Turtle()
head.shape("square")
head.color("#FFFFFF")
head.penup() # ei tõmba joont turtle objektile järgi selle funktsiooniga
head.goto(0, 0)
head.direction = "stop"

#toidu objekt
food = tl.Turtle()
food.shape("square")
food.color("#FF0000")
food.penup()
food.goto(random.randrange(-280, 280, pixel), random.randrange(-280, 280, pixel))

#game loop
while True:
    wn.update()
    
    
    
    time.sleep(delaySeconds)
wn.mainloop()