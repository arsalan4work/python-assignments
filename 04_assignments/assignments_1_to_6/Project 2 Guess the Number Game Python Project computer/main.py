from random import randint

def guess(x):
    random_number = randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1-{x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too Low!")
        elif guess > random_number:
            print("Sorry, guess again, Too high!")
    print("Congrats! You have guessed the correct number!")

guess(10)