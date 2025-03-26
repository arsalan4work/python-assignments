def main():
    fruits:str = input("Enter a fruit: ")
    stock = num_in_stock(fruits)
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print(f"This fruit is in stock! Here is how many: {stock}")


def num_in_stock(fruits:str):
    if fruits == "apple":
        return 20 
    elif fruits == "orange":
        return 10
    elif fruits == "mango":
        return 500
    else:
        return 0 
    
if __name__ == '__main__':
    main()