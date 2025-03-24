def main():
    year = int(input("Enter the year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % year == 400:
                print("That's a leap year!")
            else:
                print("That's not a leap year!")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year!")

if __name__ == '__main__':
    main()