def access_elements(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."
    
def modify_elements(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_lists(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid Indices."
    
def index_game():
    lst = [1,2,3,4,5,6,7,8,9]
    print(f"Current List: \n{lst}")
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_elements(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_elements(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_lists(lst, start, end))
    else:
        print("Invalid Operation!")

if __name__ == "__main__":
    index_game()