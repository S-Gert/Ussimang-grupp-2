import turtle as tl
import time
import random

delaySeconds = 0.1 #time.sleep() funktsiooni muutuja

#mänguaken
wn = tl.Screen()
wn.title("snek")
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

#game loop
while True:
    wn.update()
    
    
    
    time.sleep(delaySeconds)
wn.mainloop()