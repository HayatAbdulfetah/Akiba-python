nums = list(map(int, input("Please enter ten numbers: ").split()))

n = len(nums)
largest = max(nums)
smallest = min(nums)
sum_ = sum(nums)
average = sum_ / n
evens = 0
odds = 0

for i in range(n):
  if nums[i] % 2 == 0:
    evens += 1
  else:
    odds += 1

print("The largest number is:", largest)
print("The smallest number is:", smallest)
print("The total sum of the numbers is:", sum_)
print("The average of the numbers is:", average)
print("The number of even numbers is:", evens)
print("The number of odd numbers is:", odds)