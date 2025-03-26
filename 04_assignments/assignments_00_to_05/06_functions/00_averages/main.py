def average(a:float, b:float):
    """
    Returns the number which is half way between a and b
    """
    sum = a+b
    return sum / 2


def main():
    avg1 = average(0,10)
    avg2 = average(8,10)

    final = average(avg1, avg2)
    print(f"Avg 1 = {avg1}")
    print(f"Avg 2 = {avg2}")
    print(f"Avg final = {final}")



if __name__ == '__main__':
    main()