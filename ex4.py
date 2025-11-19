# List to store 12 speed values
speeds = []

print("Enter the average speed for each of the 12 hours:")

# Read 12 speed values using a loop
for i in range(12):
    speed = float(input(f"Hour {i+1} speed: "))
    speeds.append(speed)

# Calculate average speed
average_speed = sum(speeds) / 12

# Determine traffic flow condition
if average_speed < 40:
    status = "Slow"
elif average_speed <= 80:
    status = "Normal"
else:
    status = "Fast"

# Display result
print("\n--- Traffic Report ---")
print("Average Speed:", round(average_speed, 2))
print("Traffic Flow:", status)
