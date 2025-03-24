import random

NUM_SIDES = 6

def dice_simulator():
    die1:int = random.randint(1, NUM_SIDES)
    die2:int = random.randint(1, NUM_SIDES)
    total:int = die1 + die2
    print(f"Total of two dice: {total}")

def main():
    die1: int = 30
    print(f"Die1 in main() starts as {str(die1)}")
    dice_simulator()
    dice_simulator()
    dice_simulator()
    print(f"Die1 in main() is: {str(die1)}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()