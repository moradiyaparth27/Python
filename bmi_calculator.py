height = input("Enter your height in m: ")
weight = input("Enter your weight in KG: ")

# One way is to do type conversion by declaring new variables
new_height = float(height)
new_weight = float(weight)
bmi = new_weight/(new_height * new_height)
new_bmi = int(bmi)
print(new_bmi)

# Second method is to convert datatypes directly 
# Also using the power function by ** method
bmi = float(weight)/(float(height)*float(height))
bmi2 = float(weight)/(float(height)**2)
print(int(bmi))
print(int(bmi2))
print(round(bmi, 5))