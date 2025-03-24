def get_first_element(lst):

    print(lst[0])

def get_lst():

    lst = []

    elem:str =  input("Please enter a element or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main() 