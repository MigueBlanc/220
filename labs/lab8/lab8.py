"""
Name: <michael blacno>
<ProgramName>.py
"""


def number_words(in_file_name, output_file):
    in_file = open(in_file_name, "r")
    output = open(output_file, "w+")
    i = 1
    for line in  in_file:
        words = line.split()
        for words in words:
            output.write(str(i) + words + "\n")


def hourly_wages(in_hourly_file, out_hourly_file):
    in_hourly = open(in_hourly_file, "r")
    out_hourly = open(out_hourly_file, "w+")
    for line in in_hourly:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        wage_total = wage * int(parts[3])
        out_hourly.write(parts[0] + parts[1] + str(wage_total))


def calc_check_sum(isbn):
    isbn_rev = isbn[::-1]
    acc = 0
    for i in range(len(isbn)):
        numb = int(isbn_rev[i]) * (i + 1)
        acc = acc + numb
    return acc


def send_message(file,friend):
    in_file = open(file, "r")
    outfile = open(friend + ".txt", "w+")
    for line in in_file:
        outfile.write(line)


def encode_better(message, key):
    return message


def encode(message, key):
    return message


def send_safe_message(in_file_name, friend, key):
    in_file = open(in_file_name, "r")
    outfile = open(friend + ".txt", "w+")
    for line in in_file:
        outfile.write(encode(line, key))


def send_uncrackable_message(in_file_name, friend, pad):
    in_file = open(in_file_name, "r")
    outfile = open(friend + ".txt", "w+")
    pad_key = open(pad, "r")
    key = pad_key.read()
    for line in in_file:
        outfile.write(encode(line, key))

def main():
    number_words("Walrus.txt", "walrusout.txt")
    hourly_wages("hourly_wages.txt", "newwages.txt")
    calc_check_sum("0012345678")
    send_message("message.txt", "bob")
    send_safe_message("secret_message.txt", "tom", 3)
    send_uncrackable_message("safest_message.txt", "paul", "pad.txt")

    pass


main()
