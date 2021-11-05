import time
from graphics import *
from random import randint
import math


def main():
    win = GraphWin("Bounce", 401, 401)
    win.setCoords(-200, -200, 200, 200)
    radius = 20
    radius2 = 20
    p1 = win.getMouse()
    p2 = win.getMouse()
    # first circle
    c = Circle(p1, radius)
    c.setFill("red")
    c.draw(win)
    # 2nd circle
    c2 = Circle(p2, radius2)
    c2.setFill("red")
    c2.draw(win)
    dx = randint(-1, 1)
    dy = randint(-1, 1)
    dx2 = randint(-1, 1)
    dy2 = randint(-1, 1)

    # distance = math.sqrt((p2.getX() - p1.getX()**2 +(p2.getY()- p1.getY())**2)

    for i in range(10000):
        c.move(dx, dy)
        center = c.getCenter()
        cx, cy = center.getX(), center.getY()
        c2.move(dx2, dy2)
        center2 = c2.getCenter()
        cx2, cy2 = center2.getX(), center2.getY()
        if 200 - abs(cx) == radius:
            dx = -dx
        if 200 - abs(cy) == radius:
            dy = -dy
        if 200 - abs(cx2) == radius:
            dx2 = -dx2
        if 200 - abs(cy2) == radius:
            dy2 = -dy2
        # if distance <= circle.getradius * 2:
        #     dx = -dx
        update(80)
        if win.checkMouse() is not None:
            break
    win.close()


if __name__ == '__main__':
    main()
