"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
import random


def find_and_remove(lst, value):
    try:
        i = lst.index(value)
        lst[i]= "michael"
    except:
        pass


def read_data(in_file):
    file = open(in_file, "r")
    data = file.read()
    data.split()
    i = 0
    while i < len(data):
        data[i] = int(data[i])
        i += 1
    return data


def search(lst, value):
    i = 0
    while i < len(lst):
        if value == lst[i]:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("enter number between 1:10:"))
    while not x < 10 and x > 0:
        x = eval(input("enter a number between 1-10:"))
    return x


def num_digits():
    num = eval(input("enter a positive interger: "))
    while num > 0:
        digits = 0
        while digits > 0:
            num//=10
            digits += 1
        print(digits)
        num = eval(input("enter a positive interger: "))


def hi_low_game():
    num = random.randint(1, 10)
    guesses = 0
    guess = eval(input("enter yo guess: "))
    while guesses != 7 and guess!= num:
        if guess > num:
            print("value is too low")
        elif guess < num:
            print("value is too low")
            guesses += 1
            guess = eval(input("enter yo guess: "))

    if guesses != 7 and guess != num:
        print("you lost the number was" + str(num))
    else:
        print("you won the number was " + str(num) + " your guesses were " + str(guesses))

def main():
    # add other function calls here
    hi_low_game()
    pass


main()
