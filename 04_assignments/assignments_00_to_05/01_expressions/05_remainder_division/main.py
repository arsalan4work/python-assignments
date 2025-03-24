def remainder_division():
    dividend:int = int(input("Please enter an integar to be divided: "))
    divisor:int = int(input("Please enter an second integar to be divide by: "))

    quotient:int = dividend // divisor
    remainder:int = dividend % divisor

    print(f"The result of this division is {str(quotient)} with a remainder of {str(remainder)}")


if __name__ == '__main__':
    remainder_division()