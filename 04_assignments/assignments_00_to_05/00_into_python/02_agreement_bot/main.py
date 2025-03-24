def agreement_bot():
    print("This is a simple agreement bot")

    while True:
        user_input1:str = str(input("\nWhat's your favorite animal?: "))
        print(f"My favorite animal is also {user_input1}")

        user_input2:str = str(input("\nWhat's your favorite movie?: "))
        print(f"My favorite movie is also {user_input2}")

        user_input3:str = str(input("\nWhat's your favorite place?: "))
        print(f"My favorite place is also {user_input3}")

        user_input4:str = str(input("\nWhat's your favorite food?: "))
        print(f"My favorite food is also {user_input4}")

        user_input5:str = str(input("\nWhat's your favorite hobby?: "))
        print(f"My favorite hobby is also {user_input5}")

        break


if __name__ == '__main__':
    agreement_bot()