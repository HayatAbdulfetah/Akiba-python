number = 7
count = 0
num = 0

while num != number:
    num = int(input("Guess the number:"))
    count += 1
    if count == 5:
    	break
    	
if num == number:
	print("Congratulations!")
	print("You guessed the number in",count,"attempts.")
else:
	print("Game over!")