# Step 1: Get input from user
value = input("Enter anything: ")

# Step 2: Check and display the type of input
print("You entered:", value)
print("The type of your input is:", type(value))

# Step 3: Get a Python command from user
code = input("Enter Python code to run (e.g. print('Hello')): ")

# Step 4: Execute the Python code
print("Running your code...")
exec(code)
