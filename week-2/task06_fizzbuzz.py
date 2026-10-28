start = int(input("Enter number for start:  "))
end = int(input(" Enter number for end: "))

for i in range(start,end):
    if i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    else:
        print(i)