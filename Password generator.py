#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

usable_letters = []
for char in range(1, nr_letters + 1):
    usable_letters += random.choice(letters)

number_usable = []
for num in range(1, nr_numbers + 1):
    number_usable += random.choice(numbers)

usable_symbols = []
for symb in range(1, nr_symbols + 1):
    usable_symbols += random.choice(symbols)

Password_list = usable_symbols + usable_letters + number_usable
random.shuffle(Password_list)

password = ""
for pas in Password_list:
    password += pas
print(password)

