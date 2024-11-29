current_age = input("What is your current age? ")
years_left = 90 - int(current_age)
days_left = years_left * 365
week_left = years_left * 52
months_left = years_left * 12
print(f"You have {days_left} Days, {week_left} Weeks and {months_left} months left.")