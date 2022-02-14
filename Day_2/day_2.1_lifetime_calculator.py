# Get user age
age = int(input("What is your age: "))

# Assuming that users live for 90 years in total
years = 90

# Compute what is left in days, weeks, months
days_left = (years * 365) - (age * 365)
weeks_left = (years * 52) - (age * 52)
months_left = (years * 12) - (age* 12)

message = f"You have have {days_left} days, {weeks_left} weeks, and {months_left} months left"
print(message)
