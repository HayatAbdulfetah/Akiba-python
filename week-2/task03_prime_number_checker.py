import math

n = int(input("Enter a number: "))

if n <= 1:
  print(n, "-> Not prime")
elif n == 2:
  print(n, "-> Prime")
elif n % 2 == 0:
  print(n, "-> Not prime")

else:
  sqrt_ = int(math.isqrt(n))
  
  for i in range(3, sqrt_ + 1, 2):
    if n % i == 0:
      print(n, "-> Not prime")
      break

  else:
    print(n, "-> Prime")