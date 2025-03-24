INCHES_IN_FOOT:int = 12

def feet_into_inches():
    feet:float = float(input("Enter numer of feet: "))
    inches:float = feet * INCHES_IN_FOOT
    print(F"That is {inches} inches!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    feet_into_inches()