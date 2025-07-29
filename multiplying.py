import random

def play_multiplying_game():
    answer = 0
    numer_a = random.randint(1, 10)
    numer_b = random.randint(1, 10)
    correct_number = numer_a * numer_b
    attempts = 0

    while answer != correct_number:
        attempts += 1
        answer = int(input(f"What is {numer_a} multiplied by {numer_b}? "))
        if answer < correct_number:
            print("Too low! Try again.")
        elif answer > correct_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You got it with {attempts} attempts!")