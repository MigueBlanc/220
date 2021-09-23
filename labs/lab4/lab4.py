"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""

from graphics import *
import  math

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions.setText("click to close")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    pass
    win = GraphWin("rectangle drawer", 400, 400)

    p1 = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p1, p2)
    r.draw(win)
    length = abs(p2.getX() - p1.getY())
    width = abs(p2.getX() - p1.getY())

    area = length * width
    area_text = Text(Point(200, 20), "the area is" + str(area))
    area_text.draw(win)

    perimeter = 2 * (length + width)
    perimeter_txt = Text(Point(200, 40), "the perimeter is " + str(perimeter))
    perimeter_txt.draw(win)


def circle():
    # Open window
    win = GraphWin('Double click Circle', 600, 600)

    # Click for center
    center = win.getMouse()

    # Click for circumference
    point = win.getMouse()

    dx = point.getX() - center.getX()
    dy = point.getY() - center.getY()

    d = math.sqrt(dx ** 2 + dy ** 2)
    w = Circle(center, d)

    w.setFill('blue')
    w.draw(win)

    # pause for click in window
    win.getMouse()
    # close
    win.close()

def pi2():
    n = eval(input("enter value of n:"))
    acc = 0
    den = 1
    sign = 1
    for i in range(1,n):
        acc += (sign * (4/den))
        den += 2
        sign += -1
    print(math.pi - acc)

def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
