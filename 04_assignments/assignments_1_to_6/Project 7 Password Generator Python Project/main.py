import random

print("Welcome to Password Generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?/:;[]0123456789'

number = input("Enter the amount of password to generate: ")
number = int(number)

length = input("Enter the length of your password: ")
length = int(length)

print(f"\nhere are your passwords: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)