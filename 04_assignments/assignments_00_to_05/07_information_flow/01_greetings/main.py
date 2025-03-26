def main():
    name = input("What is your name?: ")
    print(greeting(name))

def greeting(name):
    return f"Geetings {name}!"

if __name__ == '__main__':
    main()