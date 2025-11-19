# Get student name
name = input("Enter the student's name: ")

# Get marks for three subjects
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

# Data validation: Marks must be between 0 and 100
if (m1 < 0 or m1 > 100) or (m2 < 0 or m2 > 100) or (m3 < 0 or m3 > 100):
    print("Error: Marks must be between 0 and 100!")
else:
    # Calculate total and average
    total = m1 + m2 + m3
    average = total / 3

    # Determine grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"

    # Display results
    print("\n--- Student Report ---")
    print("Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)
