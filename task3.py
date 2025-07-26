# Step 1: Take income and expenses as input
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

# Step 2: Calculate savings
savings = income - expenses
print("Your savings this month are:", savings)
# Step 3: Classify the savings
if savings > 10000:
    print("Status: Saving Well 💰")
elif savings >= 5000:
    print("Status: Average 🙂")
else:
    print("Status: Try to Save 😓")