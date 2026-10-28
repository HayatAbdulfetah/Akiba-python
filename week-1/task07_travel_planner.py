destination = input("Enter your destination:")
distance = float(input("Enter the distance to your destination:"))
speed = float(input("Enter your driving speed:"))

time = distance/speed

print("Destination:",destination)
print("Distance",distance,"km")
print("Speed",speed,"km/hr")
print("Estimated time:", time,"hours")