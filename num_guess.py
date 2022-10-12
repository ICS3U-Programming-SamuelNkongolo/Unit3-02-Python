#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: Oct. 5, 2022
# This program asks the user to guess a number between 0 and 9
from asyncio import constants
import random


def main():
    # ask for number
    guess = int(input("Guess a number between 0 an 9:"))

    #
    if guess == 7:
        print("you guessed correct")
    if guess != 7:
        print("you guessed wrong")


if __name__ == "__main__":
    main()
