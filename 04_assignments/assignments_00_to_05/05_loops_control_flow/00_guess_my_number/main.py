import random

def random_number_guess():

    secret_number = random.randint(1,100)

    print("I am thinking number between 1 to 100...")

    guess = int(input("Enter a guess: "))

    while guess != secret_number:
        if guess <= secret_number:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")

        print()
        guess = int(input("Enter a new guess: "))

    print(f"Correct! The number was {str(secret_number)}")

if __name__ == '__main__':
    random_number_guess()