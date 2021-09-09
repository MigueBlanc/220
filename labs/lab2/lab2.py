"""
Name: Michael Blanco
lab2.py

"""
import math

def sum_of_threes():
    global i
    upper = eval(input("enter the upper bound"))
    acc = 0
    for i in range (0,upper+1,+3):
        acc =  i + acc
    print(acc)

def multiplication_table():

    for H in range (1,11):
        for L in range(1,11):
            print(H * L, end='_')
            print()





def triangle_area():

    a = eval(input("enter side a"))
    b = eval(input("enter side b"))
    c = eval(input("enter side c"))
    s = (a + b + c)/ 2
    A = ((s * (s-a))*(s-b)*(s-c))
    math.sqrt(A)
    print(math.sqrt(A))


def sum_of_squares():
    lower = eval(input("enter lower "))
    upper = eval(input("enter upper"))
    acc = 1
    for i in range(lower,upper + 1):
         acc= i * i
         print(acc)

         #ways to square root 1) (x**2), (x*x)


def power():
    base =  eval(input("enter base"))
    exponent= eval(input("enter exponent"))
    acc = 1
    for p in range (exponent):
        acc = acc * base
        print(acc)

