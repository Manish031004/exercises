#!/local/bin/python3

import random

def main():
with open("woorden.txt") as inputfile:
woordenlijst = inputfile.readlines()
print(f"woordenlijst is {woordenlijst}")
main()
def readfile(input):
    with open(input) as inputfile:
        result = [word.strip().upper() for word in inputfile.readlines()]

        print(f"woordenlijst is {woordenlijst}")
        return result

def check_and_print_word(word, list_of_letters):



read_file("woorden.txt")

def print_word(word, list_of_letters):
    output = ""
    for w in word:
        if w in list_of_letters:
            output += w
        else:
            output += ""

    print(f"gekozen ")

def main():
    lives = 7
    word_list = read_file("woorden.txt")
    input_list = []
    won=False


    word_of_the_game = random.choice(word_list)
    print(f"woord dat we zoeken is {word_of_the_game}")

    while not won and lives > 0:
        choice = input("kies een letter: ")
        print(f"gekozen letter is {choice}")

        if choice.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Dit is geen letter!")
        else:
            if choice.upper()in word_of_the_game.upper():
                input_list.append(choice)
                print("goeien kueze, we gaan straks hiermee verder")
            else:
                #leven afnemen
                lives -= 1
                print(f"Deze letter komt niet voor in het woord. nog {lives} levens over")


main()