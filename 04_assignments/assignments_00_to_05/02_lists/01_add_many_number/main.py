def add_many_numbers(numbers) -> int:
    total_so_far = 0
    for number in numbers:
        total_so_far += number

    return total_so_far


def main():
    numbers: list[int] = [1,2,3,4,5]
    sum_of_numbers:int = add_many_numbers(numbers)
    print(sum_of_numbers)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()