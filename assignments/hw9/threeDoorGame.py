import random
from button import Buttons
from graphics import *
from string import *

def main():
    ##DOOR 1
    win = GraphWin("Three Door Game", 500, 500)
    win.setCoords(0, 0, 25, 25)
    p1 = Point(2, 14)
    p2 = Point(6, 6)
    door1 = Buttons(Rectangle(p1, p2), "door 1")
    door1.draw(win)
    door1.color_button("yellow")
    #DOOR 2
    p3 = Point(10, 14)
    p4 = Point(14, 6)
    # label = "DOOR 2"
    door2 = Buttons(Rectangle(p3, p4), "door 2")
    door2.draw(win)
    door2.color_button("yellow")
    #DOOR 3
    p5 = Point(18, 14)
    p6 = Point(22, 6)
    # label2 = "DOOR 3"
    door3 = Buttons(Rectangle(p5, p6), "door 3")
    door3.draw(win)
    door3.color_button("yellow")

    door_list = [door1, door2, door3]
    secret_door = random.choice(door_list)
    #GUI STRINGS
    starting_message = Text(Point(13, 20), "I HAVE A SECRET DOOR")
    starting_message.setSize(30)
    starting_message.draw(win)
        #click message
    click_message = Text(Point(12,3), "click on a door to open a door")
    click_message.draw(win)
        #won or lose messages
    won_message = Text(Point(13,20), "you won")
    won_exit = Text(Point(12,5), "click to exit")
    lost_exit = Text(Point(12,5), "you lost the secret door was {}".format(secret_door.get_label()))
    lost_message = Text(Point(12,22), "you lost")

    #game starts
    pt = win.getMouse()
    starting_message.undraw()
    click_message.undraw()
    if secret_door.is_clicked(pt):
        secret_door.color_button("green")
        secret_door.set_label("open")
        won_message.draw(win)
        won_exit.draw(win)
    elif door1.is_clicked((pt)):
        door1.color_button("red")
        door1.set_label("locked door")
        lost_message.draw(win)
        lost_exit.draw(win)
    elif door2.is_clicked((pt)):
        door2.color_button("red")
        door2.set_label("locked door")
        lost_message.draw(win)
        lost_exit.draw(win)
    elif door3.is_clicked((pt)):
        door3.color_button("red")
        door3.set_label("locked door")
        lost_message.draw(win)
        lost_exit.draw(win)

    win.getMouse()
    win.close()

    
if __name__ == '__main__':
    main()