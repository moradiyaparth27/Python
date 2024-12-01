import random

# Generate random integer number between a and b
random_integer = random.randint(1, 10)
print(random_integer)

# Generate random floating number between 0 to 1 but not including
random_float = random.random()
print(random_float)

# Generate random floating number between a and b
random_floating_point = random.uniform(0, 10)
print(random_floating_point)