name = input("Enter your name: ")
salary = float(input("Enter your salary: "))
transport_allowance = float(input("Enter the transport allowance: "))
food_allowance = float(input("Enter the food allowance: "))

gross_salary = salary + transport_allowance + food_allowance

print("================================")
print("EMPLOYEE PAYSLIP")
print("================================")
print("Name: ", name)
print("Salary: ", salary)
print("Transport Allowance: ", transport_allowance) 
print("Food Allowance: ", food_allowance)
print("--------------------------------")
print("Gross Salary: ", gross_salary)
print("================================")