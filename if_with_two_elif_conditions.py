print("Welcome to the roller coster ride:")
height = int(input("Enter your height in cm:"))
age = int(input("Enter your age:"))
bill = 0

# checks if the height is enoght to ride, then which ticket to buy: child, adult or senior.
if height >= 170 and age >= 45 and age <= 55:
    print("You are free to go.")
elif height >= 170 and age < 12:
    print("Please buy child ticket for $5.")
    bill = 5
elif height >= 170 and age >= 12 and age <= 18:
    print("Please buy adult ticket for $7.")
    bill = 7
elif height >= 170 and age > 18:
    print("Please buy senior ticket for $12.")
    bill = 12
else : 
    print("You're not tall enough so you can't purchase any ticket.")

# Added as an extra if user wants to take a photo or not?
photo = input("Do you want to take photo? It will cost you $3. Press y for 'YES' or n for 'NO'.")
if photo == "y":
        bill += 3

print(f"Please pay: ${bill}.")