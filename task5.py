from datetime import datetime

# Step 1: Ask for birthdate
birth_input = input("Enter your birth date (YYYY-MM-DD): ")

# Step 2: Convert to datetime object
birth_date = datetime.strptime(birth_input, "%Y-%m-%d")

# Step 3: Get today's date
today = datetime.now()

# Step 4: Calculate days lived
days_lived = (today - birth_date).days

# Step 5: Calculate age in years
age_years = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age_years -= 1

# Step 6: Print result
print("You are", age_years, "years old.")
print("You've lived for", days_lived, "days.")
