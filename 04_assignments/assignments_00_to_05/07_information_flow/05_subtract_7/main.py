def main():
    num:int = 7
    num = substract_seven(num)
    print(f"This should be zero: {num}")

def substract_seven(num):
    num = num - 7
    return num

if __name__ == '__main__':
    main()