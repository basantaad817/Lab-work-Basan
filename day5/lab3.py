# Write a Python program to guess a number between 1 to 9.Note :User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random

a, guessing = random.randint(1,10),0
while a!= guessing:
    guessing = int(input("Guess a number between 1 and 10: "))
print('well guessed')