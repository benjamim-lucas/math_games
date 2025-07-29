import random

guess = 0
correct_number = random.randint(1, 10)
while guess != correct_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < correct_number:
        print("Too low! Try again.")
    elif guess > correct_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number.")
