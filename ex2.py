# Hosting charge per hour
rate_per_hour = 0.51

# Calculations
cost_per_day = rate_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30   # assuming 30 days in a month

# Amount available
balance = 918
days_operable = balance / cost_per_day

# Display results
print("Cost per day: $", round(cost_per_day, 2))
print("Cost per week: $", round(cost_per_week, 2))
print("Cost per month: $", round(cost_per_month, 2))
print("Days you can operate with $918:", round(days_operable, 2))
