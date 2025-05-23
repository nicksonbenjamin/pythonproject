import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_position=[(0,0),(-20,0),(-40,0)]

segments = []

snake=Snake()
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    #Detect
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor() <-280:
        score.reset()


    #detect collision with tail
    for segments in snake.segments[1:]:
        if segments ==snake.head:
            pass
        elif snake.head.distance(segments) <10:
            score.reset()
            snake.reset()





screen.exitonclick()