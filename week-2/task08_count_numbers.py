n = int(input("Enter a numebr: "))

evens = 0
odds = 0
sum_ = 0

for i in range(1,n+1):
  if i % 2 == 0:
    evens+= 1
  else:
    odds += 1
  sum_ += i

print("The number of even numbers is:", evens)
print("The number of odd numbers is:",odds)
print("The sum of all the numbers is:", sum_)