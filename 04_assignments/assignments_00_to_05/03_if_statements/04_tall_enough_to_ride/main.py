MAX_HEIGHT:int = 6

def main():
    user_height = float(input("How tall are you? (give answer in ft): "))

    if user_height == MAX_HEIGHT:
        print("You are tall enough to ride!")
    elif user_height >= MAX_HEIGHT:
        print("You are more tall than max height!")
    else:
        print("You are not tall enough to ride!")

if __name__ == "__main__":
    main()