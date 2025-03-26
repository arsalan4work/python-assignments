import random

def main():

    secret_number:int = random.randint(1,100)

    print("I am thinking the number between 1-100...")

    guess = int(input("Enter a number: "))

    while secret_number != guess:
        if guess < secret_number:
            print("Your guess is tooo low!")
        else:
            print("Your guess is tooo high!")
        print()
        guess:int = int(input("Enter a new guess: "))

    print("Congrats! You guess the correct number!")

if __name__ == '__main__':
    main()