import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def random_numbers():
    for _ in range(N_NUMBERS):
        rand_num = random.randint(MIN_VALUE, MAX_VALUE)
        print(rand_num, end=" ")

if __name__ == "__main__":
    random_numbers()