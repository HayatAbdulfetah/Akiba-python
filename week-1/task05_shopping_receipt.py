name = input("Enter your name: ")
product = input("Enter the product name: ")
price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity

print("================================")
print("Receipt")
print("================================")
print("Product    Price        Quantity")
print("--------------------------------")
print(f"{product:<10} {price:<10.2f} {quantity:<10}")
print("Total: ", total)
print("Thank you for shopping!")
print("================================")