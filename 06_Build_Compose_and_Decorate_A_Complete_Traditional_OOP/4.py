# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. 
# Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Meezan Bank" #  Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name # Updating class variable
    
    def display(self):
        return f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}"
    
# storing data to class and variable
user_1 = Bank("Ali")
user_2 = Bank("Sara")

# first display to check the given data
print(user_1.display())
print(user_2.display())

# Change the bank name using class method
Bank.change_bank_name("Bank Alfalah")

# now display the data
print(user_1.display())
print(user_2.display())

# Output: 
# Account Holder: Ali, Bank: Meezan Bank
# Account Holder: Sara, Bank: Meezan Bank
# Account Holder: Ali, Bank: Bank Alfalah
# Account Holder: Sara, Bank: Bank Alfalah