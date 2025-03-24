def main():
    lst = []

    val = input("Enter a value: ")
    while val:
        lst.append(val)
        val = input("Enter a value: ")

    print(f"Here is the list: {lst}")

if __name__ == '__main__':
    main()