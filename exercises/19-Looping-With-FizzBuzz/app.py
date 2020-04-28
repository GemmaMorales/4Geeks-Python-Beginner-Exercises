def fizz_buzz(range):
    # your code here
    for i in range:
        
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        else:
            print(i)


fizz_buzz(range(1,101))