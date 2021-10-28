"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
import math
from graphics import *

def add_tens(nums):#function a
    for i in range(len(nums)):
        nums[i] = nums[i] + 10

def square_each(nums):#function b
    for i in range(len(nums)):
        nums[i] = nums[i] ** nums[i]

def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc += acc + nums[i]


def toNumbers(string_List):#function
    results = []
    for i in range(len(string_List)):
        results.append(int(string_List[i]))
    print(results)


def sum_of_squares():
    file = input("what's the name of the file?")
    in_file = open(file, "r")
    outfile = open("output.txt", "w+")
    for line in in_file:
        line = line.split()
        toNumbers(line)
        square_each(line)
        line = sum_list(line)
        outfile.write("sum of squares= " + str(line))




def starter():
    weight = eval(input("what's the weight: "))
    wins = eval(input("how many wins"))
    if 150 < weight < 160 and wins >= 5:
        print("x player is starter")
    elif weight > 199 or wins > 20:
        print("yeaahh")
    else:
    print ("not starter")


def leap_year(year):
    if year % 4 == 0 and year%100 != 0 or year % 400 ==0:
        print(("year is leap"))
    else:
        print("year is not leap" + year)


def circleOverLeap():
    win = GraphWin("circleShit", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius1 = math.sqrt((p2.getX()- p1.getX()) ** 2 + (p2.getY() - p1.getY() ** 2))
    circle = Circle(p1, radius1)
    circle.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p4.getX() - p3.getX()) ** 2 + (p4.getY() - p3.getY() ** 2))
    circle = Circle(p1, radius2)
    circle.draw(win)

    distance = math.sqrt((p3.getX() - p1.getX())**2 + (p3.getY()- p1.getY()) ** 2)

    if distance <= radius1 + radius2:
        print("overlaps")
    else:
        print("does not overlaps")

def main():
    # add other function calls here
    add_tens()
    square_each()
    sum_list()
    toNumbers()
    sum_of_squares()
    starter()
    leap_year()
    circleOverLeap()

    pass


main()
