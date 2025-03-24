PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def voting_age():
    age:int = int(input("Please Enter your age: "))

    if age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {str(PETURKSBOUIPO_AGE)}")
    else:
        print(f"You can't vote in Peturksbouipo where the voting age is {str(PETURKSBOUIPO_AGE)}")

    if age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {str(STANLAU_AGE)}")
    else: 
        print(f"You can't vote in Stanlau where the voting age is {str(STANLAU_AGE)}")
    
    if age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {str(MAYENGUA_AGE)}")
    else:
        print(f"You can't vote in Mayengua where the voting age is {str(MAYENGUA_AGE)}")
    
if __name__ == "__main__":
    voting_age()