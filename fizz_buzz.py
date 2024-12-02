for number in range(1, 101):
    if number % 5 == 0:
        if number % 3 == 0:
            print("FizzBuzz")
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)