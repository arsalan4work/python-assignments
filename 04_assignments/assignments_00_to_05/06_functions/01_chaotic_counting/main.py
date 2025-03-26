import random

DONE_LIKELIHOOD = 0.2  # 20% chance to stop counting

def done():
    """Returns True with probability DONE_LIKELIHOOD, otherwise False"""
    return random.random() < DONE_LIKELIHOOD  # Generates a number between 0 and 1

def chaotic_counting():
    """Counts from 1 to 10 but may stop randomly based on done()"""
    for i in range(1, 11):  # Loop from 1 to 10
        if done():  # Check if we should stop
            return  # Exit the function immediately
        print(i, end=" ")  # Print the current number on the same line

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Start the chaotic counting
    print("\nI'm done.")  # Print "I'm done." once counting stops

if __name__ == '__main__':
    main()
