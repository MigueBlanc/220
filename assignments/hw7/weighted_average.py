"""
Michael Blanco Chavez
weighted_average.py

Proof of Authenticity : I certify this is product of my own work

"""


def weighted_average(infile_name, out_file_name):
    out_file = open(out_file_name, "w+")
    class_average = 0
    with open(infile_name, "r") as in_file:
        text_info = in_file.readlines()
        for line in text_info:
            text_values = line.strip().split(":")
            grades = 0
            for i in range(2, len(text_values), 2):
                grades = grades + float(text_values[i].strip()) * float(text_values[i + 1].strip())
            grades = grades / 100
            class_average += grades
            out_file.write(text_values[0] + " " + "'s average: {:.1f}".format(grades))
        class_average = class_average / len(text_values)
        # out_file.write('class average is : {:.1f'.format(class_average))
        out_file.close()
        # (allValues[0] + " " + allValues[1] + "'s average: {0:.1f}".format(finalWeightAverage))


def main():
    weighted_average("grades.txt", "results.txt")


if __name__ == '__main__':
    main()
