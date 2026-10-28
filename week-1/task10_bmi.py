name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = weight / (height * height)

print("=========================")
print("BMI REPORT")
print("=========================")
print("Name:",name)
print("Weight:",weight)
print("Height:",height)
print("BMI:",BMI)
print("=========================")