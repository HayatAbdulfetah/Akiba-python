amount_in_dollar = int(input("Enter the amount in American Dollar:"))
rate = 150

amount_in_birr = amount_in_dollar*rate

print("===========================")
print("CURRENCY CHANGE")
print("===========================")
print("USD Amount",amount_in_dollar)
print("Exchange Rate: 1 USD =",rate,"ETB")
print("ETB Amount:",amount_in_birr,"ETB")
print("==========================")