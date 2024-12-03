import random

max_letters = int(input("How many letters would you like in your password?"))
max_symbols = int(input("How many symbols would you like?"))
max_numbers = int(input("How many numbers would you like?"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list2 = []
for i in range(max_letters):
    password_list2.append(random.choice(letters))

for i in range(max_numbers):
    password_list2.append(random.choice(numbers))

for i in range(max_symbols):
    password_list2.append(random.choice(symbols))

random.shuffle(password_list2)
password = ''.join(password_list2)
print(password)