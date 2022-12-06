import turtle as tl
import time
import random

delaySeconds = 0.1 #time.sleep() funktsiooni muutuja
speed_score = 10 #ekraanil scoreboardil kiirusenäitaja

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

#scoreboardi kirjutamise objekt
score = 0
high_score = 0
scoreboard = tl.Turtle()
scoreboard.shape("square")
scoreboard.color("#FFFFFF")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("SCORE: 0   HIGH SCORE: 0   SPEED: 10", align="center", font=("Consolas",20,"normal"))

#liikumise suuna määramine
def move():
    if head.direction == "up":
        head.sety(head.ycor() + pixel)

    if head.direction == "down":
        head.sety(head.ycor() - pixel)

    if head.direction == "left":
        head.setx(head.xcor() - pixel)

    if head.direction == "right":
        head.setx(head.xcor() + pixel)

#suuna muutmise funktsioonid
def move_up():
    if head.direction != "down": #ei lase liikuda vastassuunas (180 kraadi)
        head.direction = "up"
    
def move_down():
    if head.direction != "up":
        head.direction = "down"
    
def move_left():
    if head.direction != "right":
        head.direction = "left"
    
def move_right():
    if head.direction != "left":
        head.direction = "right"

#kuulab kasutaja inpute
wn.listen()
wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")

#esimene segment listis
psegment = tl.Turtle()
psegment.speed(0)
psegment.shape("square")
psegment.color("#FFFFFF")
psegment.penup()

snake_body = [psegment] #ilma placeholderita läheb esimene saba osa pea peale miski pärast, idk miks

#game loop
while True:
    wn.update()
    move()
    
    #toidu söömine
    if head.distance(food) < pixel:
        x = random.randrange(-280, 280, pixel)
        y = random.randrange(-280, 280, pixel)
        food.goto(x, y)
        
        #takistab toidu tekkimisel ussi keha sisse
        for segment in snake_body:
            if segment.distance(food) < pixel:
                x = random.randrange(-280, 280, pixel)
                y = random.randrange(-280, 280, pixel)
                food.goto(x, y)
        
        #toidu söömisel keha segmendi lisamine
        new_segment = tl.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#C0C0C0")
        new_segment.penup()
        snake_body.append(new_segment)
        
        #add score
        score = score + 1
        if score  > high_score:
            high_score = score
        
        #add speed
        
        delay_seconds -= 0.001
        speed_score += 10
        
        scoreboard.clear()
        scoreboard.write("SCORE: {}   HIGH SCORE: {}   SPEED: {}".format(score, high_score, speed_score), align="center", font=("Consolas",20,"normal"))
        
    #mänguäärte kokkupõrked
    if head.xcor() < -280 or head.xcor() > 280 or head.ycor() < -280 or head.ycor() > 280:
        head.direction = "stop"
        time.sleep(0.5)
        head.goto(0, 0)
        for segment in snake_body:
            segment.goto(3000, 3000) #keha osade objekte otseselt eemaldada ei oska, seega saadan kuskile pärapõrgusse
        snake_body = [psegment]
        
        #clear score
        score = 0
                
        #reset speed
        delay_seconds = 0.1
        speed_score = 10
        
        scoreboard.clear()
        scoreboard.write("SCORE: {}   HIGH SCORE: {}   SPEED: {}".format(score, high_score, speed_score), align="center", font=("Consolas",20,"normal"))

    #ussi pea ja keha kokkupõrkamine
    for segment in snake_body:
        if segment.distance(head) < pixel:
            head.direction = "stop"
            time.sleep(0.5)
            head.goto(0,0)
            for segment in snake_body:
                segment.goto(3000, 3000)
            snake_body = [psegment]           
            #clear score
            score = 0
                        
            #reset speed
            delay_seconds = 0.1
            speed_score = 10
            
            scoreboard.clear()
            scoreboard.write("SCORE: {}   HIGH SCORE: {}   SPEED: {}".format(score, high_score, speed_score), align="center", font=("Consolas",20,"normal"))

    #ussi keha pea jälgimine
    for i in range(len(snake_body)-1, 0 ,-1):
        x = snake_body[i-1].xcor()
        y = snake_body[i-1].ycor()
        snake_body[i].goto(x, y)
    
    if len(snake_body) > 0:
        x = head.xcor()
        y = head.ycor()
        snake_body[0].goto(x, y)

    time.sleep(delaySeconds)
wn.mainloop()