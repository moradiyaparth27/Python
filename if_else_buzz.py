user_input = int(input("Enter a number: "))

if user_input % 5 == 0 :
    if user_input % 3 == 0:
        print("BuzzBee")
    else :
        print("Buzz")
elif user_input%3 ==0 :
    print("Bee")