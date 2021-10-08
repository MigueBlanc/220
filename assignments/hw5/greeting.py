"""
Michael Blanco
greeting.py


"""
import graphics
from graphics import GraphWin, Point, Polygon, Text, Rectangle
from time import sleep, time


def main():
    win = GraphWin("HELLO!", 500, 500)
    win.setBackground("blue")

    poly = Polygon(Point(250, 250), Point(240, 240), Point(220, 228), Point(210, 230), Point(205, 240),
                   Point(207, 250), Point(250, 300), Point(250, 250), Point(260, 240), Point(270, 230), Point(280, 228),
                   Point(290, 230), Point(295, 240), Point(293, 250), Point(250, 300))
    poly.setOutline("red")
    poly.setFill("red")
    poly.setWidth(3)
    poly.draw(win)

    label_cord = (Point(250, 150))
    label = Text(label_cord, "Hello, Happy valentines!!")
    label.draw(win)
    arrow_tail = Rectangle(Point(200, 264),Point(250, 266))
    arrow_tail.draw(win)
    arrow_tail.setFill("white")
    arrow_head= Polygon(Point(250,260), Point(250,270), Point(265,265))
    arrow_head.draw(win)
    arrow_head.setFill("white")

    for i in range(10):
        arrow_head.move(11, 1)
        arrow_tail.move(11, 1)
        sleep(0.1)

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
