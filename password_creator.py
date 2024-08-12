import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '£']

print("Welcome to my password generator")
nr_letters = int(input("How many letters?\n"))
nr_numbers = int(input("how many numbers?\n"))
nr_symbols = int(input("how many symbols?\n"))

password = []

for letter in range(0, nr_letters):
    password += random.choice(letters)
    print(password)

for number in range(0, nr_numbers):
    password += random.choice(numbers)
    print(password)
for symbol in range(0, nr_symbols):
    password += random.choice(symbols)
    print(password)

random.shuffle(password)
new_password = "".join(password)
print(f"Your new password is: {new_password}")
