# Taking input list from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Dictionary comprehension to keep only odd numbers and store their cubes
odd_cube_dict = {n: n**3 for n in numbers if n % 2 != 0}

# Display output
print("Dictionary with odd numbers and their cubes:")
print(odd_cube_dict)
