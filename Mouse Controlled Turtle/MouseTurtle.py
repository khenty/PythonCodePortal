from turtle import Screen, Turtle

screen = Screen()
yertle = Turtle()

def k101():
    screen.onscreenclick(click_handler)

def click_handler(x, y):
    screen.onscreenclick(None)  # disable event inside event handler
    yertle.setheading(yertle.towards(x, y))
    yertle.goto(x, y)
    screen.onscreenclick(click_handler)  # reenable event on event handler exit

screen.onkey(k101, " ")  # space turns on mouse drawing

screen.listen()

screen.mainloop()
