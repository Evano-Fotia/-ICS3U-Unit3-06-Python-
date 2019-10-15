#!/usr/bin/env python3

# Created by: Evano Fotia
# Created on: oct 2019
# this program guesses the number

import random


def main():

    # random number
    number = random.randint(0, 9)

    # input
    guess = input("Guess the number between 0 and 9: ")
    print("")

    # process
    try:
        guess = int(guess)
        if guess == number:
            print("Correct number")
            # process
        else:
            print("Sorry. nice try!")
            print("My number was", number)
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
