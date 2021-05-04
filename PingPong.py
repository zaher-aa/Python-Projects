# importing turtle module
import turtle

wind = turtle.Screen()  # initializing the game screen
wind.title("Ping Pong Game By Zaher.")  # the screen title
wind.setup(width=800, height=600)  # screen width and height
wind.bgcolor("orange")  # screen color
wind.tracer(0)  # 0 to make the creater control when the screen should update

# madrab_1
madrab_1 = turtle.Turtle()  # making a madrab object from Turtle class
madrab_1.shape("square")  # determine the shape of the madrab
madrab_1.shapesize(stretch_wid=5, stretch_len=1)  # madrab size
madrab_1.penup()  # stop the object from drawing lines
madrab_1.speed(0)  # set the speed of the animation
madrab_1.color("blue")  # madrab_1 color
madrab_1.goto(-350, 0)  # position of madrab on the screen

# madrab_2
madrab_2 = turtle.Turtle()
madrab_2.shape("square")
madrab_2.shapesize(stretch_wid=5, stretch_len=1)
madrab_2.penup()
madrab_2.speed(0)
madrab_2.color("red")
madrab_2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.penup()
ball.speed(0)
ball.color("white")
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# score
red_score = 0
blue_score = 0
score = turtle.Turtle()
score.hideturtle()  # because we want the text on the object
score.speed(0)
score.penup()
score.color("black")
score.goto(0, 260)
score.write("Blue: 0    Red: 0", align="center", font=("Arial", 17, "bold"))

# functions


def madrab_1_up():
    # get madrab_1 y position then increase it by 20
    madrab_1.sety(madrab_1.ycor() + 20)


def madrab_1_down():
    # get madrab_1 y position then decrease it by 20
    madrab_1.sety(madrab_1.ycor() - 20)


def madrab_2_up():
    # get madrab_2 y position then increase it by 20
    madrab_2.sety(madrab_2.ycor() + 20)


def madrab_2_down():
    # get madrab_2 y position then decrease it by 20
    madrab_2.sety(madrab_2.ycor() - 20)


# keyboard bindings
wind.listen()  # to make the screen redy to take an order from the keyboard
wind.onkeypress(madrab_1_up, "w")  # when press on w call the function
wind.onkeypress(madrab_1_down, "s")  # when press on s call the function
wind.onkeypress(madrab_2_up, "Up")  # when press on up arrow call the function
wind.onkeypress(madrab_2_down, "Down")  # when press down arrow call function

# main game loop


while True:
    wind.update()  # update the screen every time the loop runs

    # ball movement
    # ball start at 0 and every time loop runs ==> x axis += 0.2
    ball.setx(ball.xcor() + ball.dx)
    # ball start at 0 and every time loop runs ==> y axis += 0.2
    ball.sety(ball.ycor() + ball.dy)

    # border check , top border ==> +300, bottom border ==> -300, top right ==> +600, top left ==> -600, ball ==> 20
    if ball.ycor() > 290:  # if ball at top border
        ball.sety(290)  # set y to +290
        ball.dy *= -1  # reverse ball movement

    if ball.ycor() < -290:  # if ball at bottom border
        ball.sety(-290)  # set y to -285
        ball.dy *= -1  # reverse ball movement

    if ball.xcor() > 390:  # if ball at top right
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse ball movement
        blue_score += 1
        score.clear()  # to clear the previous score
        score.write(f"Blue: {blue_score}    Red: {red_score}",
                    align="center",
                    font=("Arial", 17, "bold"))

    if ball.xcor() < -390:  # if ball at top left
        ball.goto(0, 0)  # return ball to center
        ball.dx *= -1  # reverse ball movement
        red_score += 1
        score.clear()  # to clear the previous score
        score.write(f"Blue: {blue_score}    Red: {red_score}",
                    align="center",
                    font=("Arial", 17, "bold"))

    # ball and madrab borders check
    if ball.xcor() > 340 and (ball.ycor() < madrab_2.ycor() + 50 and ball.ycor() > madrab_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and (ball.ycor() < madrab_1.ycor() + 50 and ball.ycor() > madrab_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
