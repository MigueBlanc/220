"""
Michael Blanco
greeting.py


"""
import graphics
from graphics import GraphWin, Point, Polygon, Text, Rectangle
from time import sleep


def main():
    width = 400
    height = 400
    win = GraphWin("Hello!!", width, height)
    a = Point(300, 250)
    b = Point(150, 175)
    c = Point(165, 150)
    d = Point(190, 150)
    e = Point(200, 160)
    f = Point(210, 150)
    g = Point(235, 150)
    h = Point(250, 150)
    shape = Polygon(a, b, c, d, e, f, g, h)
    shape.setFill("red")
    win.getMouse()

    shape.draw(win)


    greeting = Text(Point(200,300), "happy valentines day")
    win.getMouse()


if __name__ == '__main__':
    main()
