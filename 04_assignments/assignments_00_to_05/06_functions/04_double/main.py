def double_num(num: int):
    return num * 2

def main():
    user_input = int(input("Enter a number: "))
    num_times_2 = double_num(user_input)
    print(f"Double is: {num_times_2}")

if __name__ == '__main__':
    main()