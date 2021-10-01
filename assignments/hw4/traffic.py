"""
Michael Blanco Chavez

traffic.py

Certification of Authenticity: I certified this is my work.


"""


def main():
    total_vehicles_accumulator = 0
    acc_cars = 0
    roads = int(input("how many roads were surveyed?"))
    for roads_loop in range(0, roads):
        days = eval(input("how many days was road " + str(roads_loop + 1) + " surveyed?"))
        for days_loop in range(0, days):
            cars_traveled = eval(input("how many cars traveled in day " + str(days_loop + 1) + "?"))
            acc_cars += cars_traveled
        road_avg = acc_cars / days
        print("total cars traveled is : " + str(acc_cars))
        total_vehicles_accumulator += acc_cars
        acc_cars = 0
        print("road ", roads, " average vehicles per day : ", road_avg)

    total_average = total_vehicles_accumulator / roads
    print("total number of vehicles traveled on all roads: ", total_vehicles_accumulator)
    print("average number of vehicles per road : ", total_average)


if __name__ == '__main__':
    main()
