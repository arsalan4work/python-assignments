ADULT_AGE:int = 18 #U.S age

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    user_age = int(input("Enter your age: "))
    print(is_adult(user_age))


if __name__ == '__main__':
    main()