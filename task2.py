# Ask the user to enter an expression
expression = input("Enter a Python expression (like 2 + 3 * 4): ")

# Store it in a result variable using exec
exec(f"result = {expression}")

# Show the result
print("Result of your expression is:", result)
