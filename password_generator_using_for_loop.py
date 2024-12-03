import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

max_letters = int(input("How many letters would you like in your password?"))
max_symbols = int(input("How many symbols would you like?"))
max_numbers = int(input("How many numbers would you like?"))

# *-*-*-*-* HARD LEVEL *-*-*-*-*  
# If passwrod list is written as password = [] the output will be single-single letters within single quotes (for example: ['V', 'y', 'E'])
password_list = []

for i in range( 1, max_letters + 1 ):
    password_list.append(random.choice(letters))

for i in range ( 1, max_numbers + 1 ):
    password_list.append(random.choice(numbers))

# Instead of starting the range from 1 and adding +1 at last we can start it from 0 itself.
for i in range ( 0, max_symbols ):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)
# Final step is to convert the list objects into a string
final_password = ""

for char in password_list :
    final_password += char
print(f"{final_password}")



# *-*-*-*-* EASY LEVEL *-*-*-*-* 
# If passwrod list is written as password = "" the output will be letters as a string (for example: VyE)
password = "" 

for i in range( 1, max_letters + 1 ):
    password += random.choice(letters)

for i in range ( 1, max_numbers + 1 ):
    password += random.choice(numbers)

# Instead of starting the range from 1 and adding +1 at last we can start it from 0 itself.
for i in range ( 0, max_symbols ):
    password += random.choice(symbols)

print(password)