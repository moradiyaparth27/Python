number = int(input("Enter a number: "))

for i in range (1, number + 1 ) :
    if i % 3 == 0:
        if i % 5 == 0:
            print(f"{i}: FizzBuzz")
        else :
            print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
    else : 
        print(f"{i} : N/A")