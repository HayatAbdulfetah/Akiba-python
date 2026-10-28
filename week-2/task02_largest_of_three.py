a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b and b == c:
    print("All three numbers are equal.")
elif a >= b and a >= c:
    if a == b:
        print("The largest number is:", a, "and", b)
    elif a == c:
        print("The largest number is:", b, "and" , c)
    else:
        print("The largest number is:", a)
elif b >= a and b >= c:
    if b == c:
        print("The largest number is:", b, "and" , c)
    else:
        print("The largest number is:",b)
else:
    print("The largest number is:",c)