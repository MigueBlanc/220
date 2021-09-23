"""
Name : Michael Blanco Chavez
mean.py

Problem : compute arithmetics to calculate the mean of a number given by the user.

Certification of Authenticity: I certify this project is all my own work.

"""

import math


def main():
    num = int(input("how many numbers?"))
    total_sum = 0  # accumulator for the rms
    acc_harmonic = 0  # accumulator for the  harmonic mean
    geo_acc = 1
    tt_acc = 0
    list1 = []
    for number_range in range(num):
        # rms
        numbers = float(input("enter value " + str(number_range + 1) + ":"))
        tt_acc += tt_acc
        square = numbers ** 2
        total_sum += square
        # harmonic mean
        divide = 1 / numbers
        acc_harmonic += divide
        # geometricMean
        list1.append(numbers)
        geo_acc = geo_acc * numbers

    avg = total_sum / num
    rms = round(math.sqrt(avg), 3)
    harmonic_mean = round(num / acc_harmonic, 3)
    geometric_mean = round(geo_acc ** (1 / num), 3)

    print( float(rms))
    print(float(harmonic_mean))
    print(float(geometric_mean))


if __name__ == '__main__':
    main()
