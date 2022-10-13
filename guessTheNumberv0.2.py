# This is a guess the number game.
# Taken directly from the solution

import random
from tkinter.tix import DisplayStyle

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is low')
    elif guess > secretNumber:
        print('Your guess is high')
    else:
        break       # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


# Future improvement on this program
# Add a scoreboard system that shows the least number of guesses and the date it was taken on.
# Maybe take data of 30
# Where this program is ran as a script evertime i enter the os