def main():
    for i in range(20):
        if is_odd(i):
            print(f"{i} is Odd!")
        else:
            print(f"{i} is Even!")

def is_odd(value: int):
    remainder = value % 2
    return remainder == 1

if __name__ == '__main__':
    main()