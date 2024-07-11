import turtle
import random

#main screen
gameScreen = turtle.Screen()
gameScreen.bgcolor("light blue")
gameScreen.title("Catch the Turtle")

#variables
score=0
topHeight=gameScreen.window_height()/2

#turtles
gameTurtle=turtle.Turtle()
scoreText=turtle.Turtle()
timeText=turtle.Turtle()

#main turtle
def mainTurtle():
    gameTurtle.shape("turtle")
    gameTurtle.shapesize(2,2,2)
    gameTurtle.color("green")
    gameTurtle.teleport(random.randint(-250,250),random.randint(-250,250))
    gameScreen.ontimer(mainTurtle,600)

#score text and counting scores
def scoreTitle():
    scoreText.teleport(0,topHeight*0.9)
    scoreText.hideturtle()
    scoreText.color("dark blue")
    scoreText.write(f"Score: {score}",move=False,align="center",font=("Arial",20,"normal"))

def scoreCount(x,y):
    global score
    score +=1
    scoreText.clear()
    scoreText.write(f"Score: {score}",move=False,align="center",font=("Arial",20,"normal"))

#time text and countdown
def timeTitle(time):
    timeText.teleport(0,topHeight*0.8)
    timeText.hideturtle()
    timeText.color("black")
    if time>0:
        timeText.clear()
        timeText.write(f"Time: {time}", move=False, align="center", font=("Arial", 20, "normal"))
        gameScreen.ontimer(lambda: timeTitle(time-1),1000)
    else:
        timeText.clear()
        gameTurtle.hideturtle()
        timeText.write("Game Over!", move=False, align="center", font=("Arial", 20, "normal"))

turtle.tracer(0)
timeTitle(20)
scoreTitle()
gameTurtle.onclick(scoreCount)
mainTurtle()
turtle.tracer(1)

turtle.mainloop()