correctPIN = 1234
n = 0
while n < 3:
  trial = int(input("Enter your four digits pin: "))
  n += 1
  
  if(trial == correctPIN):
    print("Successful")
    break
  else:
    print("Incorrect PIN.")
    print("Attempt remaining:", 3-n)