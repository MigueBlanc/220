"""
Name: <Michael Blanco>
<hangman>.py
"""
import random


def read_words(file_name):
    file = open(file_name, "r")
    content_list = file.read()
    content_list = content_list.split()
    return content_list


def get_word():
    word = random.choice(read_words("word.txt"))
    return word


def play_game():
    file = open("word.txt", "r")
    content_list = file.read()
    content_list = content_list.split()
    word = random.choice(content_list)
    tries = 7
    guesses = ""
    guessess = ''
    tries = 7
    while tries > 0:
        fail = 0
        for i in word:
            if i in guessess:
                print(i, end=' ')
            else:
                print('-', end=' ')
                fail += 1
        if fail == 0:
            print('\nYou Won!')
            break
        guess = input('\nEnter Your Guess: ')
        guess = guess.upper()
        guessess += guess
        if guess not in word:
            tries -= 1
            if tries == 0:
                print('You Lost,Word: {}'.format(word))
            else:
                print('Wrong Guess,{} round left!'.format(tries))


def main():
    # read_words()
    # get_word()
    play_game()
    pass


main()
