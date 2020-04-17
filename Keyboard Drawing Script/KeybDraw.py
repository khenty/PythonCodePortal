"""
All movements and turns are by increments of 5.
Right arrow key = move forward
Left arrow key = move backward
r = turn right
l = turn left
u = pen up
d = pen down
h = go home
c = clear
"""

from tkinter import *
from turtle import *

root = Tk()
T = Text(root, root.title("Controls"),height=12, width=60)
T.pack()
T.insert(END, "\nRight arrow key = move forward\nLeft arrow key = move backward\nr = turn right\nl = turn left\nu = pen up\nd = pen down\nh = go home\nc = clear")


def main():
    width(2)
    speed(0)
    pencolor("blue")
    onkey(up, "u")
    onkey(down, "d")
    onkey(clear, "c")
    onkey(home, "h")
    onkey(lambda: forward(5), "Right")
    onkey(lambda: back(5), "Left")
    onkey(lambda: left(5), "l")
    onkey(lambda: right(5), "r")
    listen()
    return "Done!"
if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
