"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
from random import randint
def ibb(value, list1):
    left_p = 0
    right = len(list1) - 1
    while left_p <= right:
        middle = (left_p + right) // 2
        middle_value = list1[middle]
        if middle_value == value:
            print(middle)
            break
        elif value < middle_value:
            right = middle_value

        elif value > middle_value:
            left_p = middle + 1
#
#
def ss(list1):
    for i in range(len(list1)):
        lowest = list1[i]
        pos = i
        for index in range(i, len(list1)):
            if list1[index] < list1[lowest]:
                lowest = list1[index]
                pos = index
        list1[i], list1[pos] = list1[pos], list1[i]

#
#
def get_area(rec):
    return randint(1, 100)


def rect_sort(values):
    d = {}
    areas = []
    for rectangles in values:
        d[get_area(rectangles)] = rectangles
        areas.append(get_area(rectangles))
    ss(areas)
    for i in range(len(areas)):
        values[i] = d[areas]
    return areas


def trade_alert(filename):
    file = open(filename, "r")
    data = file.read().split(" ")
    for i in range(len(data)):
        if 500 < int(data[i]) < 830:
            print(i + 1, "warning")
        elif int(data[i]) > 830:
            print(i + 1, "ALERT!!!")



if __name__ == '__main__':
    ibb(9, [1,2,3,4,5,6,7,8,9])



