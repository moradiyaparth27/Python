num = int(input("Enter a number: "))
mod = int(input("Enter modulo number: "))

moduler = num % mod
if moduler == 0:
    print(f"The number {num} is divisible by {mod} because the remainder is {moduler}.")
else :
    print(f"The number {num} is not divisible by {mod} because the remainder is {moduler}.")