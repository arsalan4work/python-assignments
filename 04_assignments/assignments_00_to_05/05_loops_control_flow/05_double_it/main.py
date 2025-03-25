def main():

    curr_value = int(input("Enters the number 2 you would then print: "))
    while curr_value < 100:
        curr_value = curr_value * 2
        print(f"Double is: {curr_value}")



if __name__ == '__main__':
    main()