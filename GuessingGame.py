#Author: Alyssa Evans


import random

secret = int(random.randint(1,10))

guess = int(input("Guess a number between 1 and 10: "))

if secret == guess:
	print("You win!")
while (secret != guess):
    if (guess > secret):
        print("Too high.")
    else:
        print("Too low.")
    guess = int(input("Guess a number between 1 and 10: "))
