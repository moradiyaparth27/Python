print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

tip_amount = (float(total_bill) * float(tip)) / 100
total_amount_to_be_paid = float(total_bill) + tip_amount
payment = total_amount_to_be_paid / float(people)

print(f'Each person should pay: ' +  "{:.2f}".format(payment))
print(f'Each person should pay: ' +  "{:.4f}".format(payment))