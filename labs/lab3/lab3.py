"""
Name: <Michael Blanco>
<ProgramName>.py
"""
import math

def average():
    num_of_grades = eval(input("number of grades to input? :"))
    for i in range(1, num_of_grades + 1 ):

        grade1 = eval(input(i))
        grade = eval(input(i))
        acc = 0 + grade
        average = acc / num_of_grades
        print ("your grade average is : ", average)




# def tip_jar():
    #for i in range(5 + 1):

# def newton():


def pi():
    n = input("how many number of factors are there? :")
    inc = 1
    for i in range(1, n+1):
        temp1 = float(2 * i) / (2 * i -1)
        temp2 = float(2* i) / (2 * i +1 )
        inc = inc * temp1 * temp2
        print("pi/2 using wallis formula is ", inc)