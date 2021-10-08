"""
michael blanco

"""


def name_reverse():
    x = input("what is your full name?")
    x_reverse= x.split()
    print(x_reverse[1] + "," + x_reverse[0])


def company_name():
    x = input("enter a three-part internet domain: ")
    name_split = x.split(".")
    print(name_split[1])


def initials():
    n = eval(input("how many students are in the class? "))
    for i in range(n):
        first_name = input("enter the first name of student")
        last_name = input("enter" + first_name + "'s" "last name")
        print(first_name + "' s initials are:" + first_name[0] + last_name[0])


def names():
    x = input(("enter a list of names, first name ,last name : "))
    n = x.split(",")
    for nam in n:
        parts = nam.split()
        print("the initials are " + parts[0][0] + parts[1][1])

def thirds():
    sentences = eval(input("how many sentences will be input? "))
    for i in range(sentences):
        s = input("enter sentence: ")
        print(s[2::3])


def word_average():
    sentence = input("enter a sentence")
    acc = 0
    x = sentence.split()
    for word in x:
        acc += len(word)
        print(acc/len(word))


def pig_latin ():
    x = input("sentence")
    x = x.lower()
    x = x.split()
    for word in x:
        print(word[1:] + "ay", end= " ")


def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()



if __name__ == '__main__':
    main()

