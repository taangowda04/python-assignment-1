import pandas as pd
import pandas as pd

# Empty lists to store data
names = []
basic_salaries = []
total_salaries = []

while True:
    name = input("Enter employee name (type 'stop' to finish): ")

    if name.lower() == "stop":
        break

    salary_input = input("Enter basic salary (or type 'stop' to finish): ")
    if salary_input.lower() == "stop":
        break

    basic_salary = float(salary_input)

    # Salary calculations
    hra = 0.20 * basic_salary
    da = 0.10 * basic_salary
    total_salary = basic_salary + hra + da

    # Store data in lists
    names.append(name)
    basic_salaries.append(basic_salary)
    total_salaries.append(total_salary)

# Create DataFrame
df = pd.DataFrame({
    "Employee Name": names,
    "Basic Salary": basic_salaries,
    "Total Salary": total_salaries
})

# Display the Table
print("\n--- Employee Salary Report (Using Pandas) ---")
print(df)
