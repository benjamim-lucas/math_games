import random

def play_guessing_game():
    guess = 0
    correct_number = random.randint(1, 10)
    attempts = 0

    while guess != correct_number:
        attempts += 1
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < correct_number:
            print("Too low! Try again.")
        elif guess > correct_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You got it with {attempts} attempts!")