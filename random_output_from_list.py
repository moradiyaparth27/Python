import random

friends = ["Parth", "Happy", "Fenil", "Nikhil"]

# Use a variable to save random choices from the list and then print
payer = random.choices(friends)
print(payer)

# Print random choice directly from list
print(random.choices(friends))

# Find the length of list, Use random integer function
print(len(friends))
payer = random.randint(0, 3)
print(friends[payer])