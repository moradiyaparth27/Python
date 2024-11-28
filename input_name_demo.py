a = input("What's your name? ")
print("Hello", a + " Hope your'e doing well!")
print("Hi", a + " I can confirm that your age is: " + input("What's your Age?"))


#This line will count the characters with spaces
print("The total characters in your name counting the spaces in between is: " + str( len (a) ))

#This line will count the characters without spaces in between string
print("The total characters in your name without counting the spaces in between is: " + str( len (a.replace(' ', '') ) ))