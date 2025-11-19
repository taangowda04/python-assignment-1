# Ask the user for the distance
distance = float(input("How far do you want to travel (in miles)? "))

# Check the conditions
if distance < 3:
    print("You should ride a Bicycle.")
elif distance < 300:
    print("You should ride a Motor-Cycle.")
else:
    print("You should drive a Super-Car.")