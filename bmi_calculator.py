height = input("Enter your height in m: ")
weight = input("Enter your weight in KG: ")

# One way is to do type conversion by declaring new variables
new_height = float(height)
new_weight = float(weight)
bmi = new_weight/(new_height * new_height)
new_bmi = int(bmi)
print(new_bmi)

# Second method is to convert datatypes directly 
bmi = float(weight)/(float(height)*float(height))
print(int(bmi))

# Third using the power function by ** method
bmi2 = float(weight)/(float(height)**2)
print(int(bmi2))

# Fourth method is to use // operator to convert float values to integer values directly
bmi3 = float(weight) // float(height) ** 2
print(int(bmi3))

# Fifth method is to use round function to decide how many digits should be there in float
print(round(bmi, 5))

# Sixth is to print str and int in a same print statement using fstring 
print(f"Your BMI is: {round(bmi, 2)}")

# Just prints how the calculation will be done using the user's input values
print(f"Your BMI is calculated by this way: {weight}/({height}*{height})")


print(f"You have entered weight as: {weight} KG and height as: {height} m.")