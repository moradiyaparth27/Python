cities_in_gujarat = ["Surat", "Ahmedabad", "Kachh", "Bhavanagar", "Navsari", "Bardoli"]
print(cities_in_gujarat)

# Get output from a list based on their position 
print(cities_in_gujarat[0])
print(cities_in_gujarat[1])

# Get output from a list based on their position where -1 is the last position
print(cities_in_gujarat[-1])
print(cities_in_gujarat[-2])

# Append the list with adding one single item at the last in the list
cities_in_gujarat.append("Vapi")
print(cities_in_gujarat[-1])

# Extend the items in the list
cities_in_gujarat.extend(["Parth", "Happy"]) 
print(cities_in_gujarat)

# Append the list with given item on specific position
cities_in_gujarat.insert(0, "Parth0")
print(cities_in_gujarat)

# Removes the item form the list
cities_in_gujarat.remove("Bardoli")
print(cities_in_gujarat)

# Remove the item from the list from a specific Position 
cities_in_gujarat.pop(2)
print(cities_in_gujarat)