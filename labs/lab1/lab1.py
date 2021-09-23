"""
Name: <Michael Blanco>
lab1.py

Problem: this function calculates the aarea of a rectangle

"""

def calc_rec_area():
    length = eval(input("enter the length"))
    width = eval(input("enter the width"))
    area = length * width
    print("area =", area)


def calc_volume():
    width = eval(input("enter the width:"))
    height = eval(input("enter the height:"))
    length = eval(input("enter the length:"))
    volume = width * height * length
    print("the volume is = ", volume)

def shooting_percentage():
    shots = eval(input("how many shots?"))
    shotsmade = eval(input("how many shots went in?"))
    shootingpercentage = shotsmade/shots * 100
    print("your shooting percentage is =" , shootingpercentage)

def cofee():
    pounds = eval(input("how many pounds?"))
    coffeecost = 10.50
    costcoffee = pounds * coffeecost
    shippingrate = 0.86
    totalcost = costcoffee + shippingrate
    print("your total cost is = $" , totalcost)
def kilometers_to_miles():
    kilometers = eval(input("how many kilometers did you travel??"))
    milescon = kilometers * .61
    print("you traveled", milescon ,  "miles")







