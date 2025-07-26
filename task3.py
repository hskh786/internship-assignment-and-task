# Step 1: Declare variables
a = "123"          # String
b = 10             # Integer
c = 3.14           # Float
d = True           # Boolean
e = 2 + 3j         # Complex number
# Step 2: Print original values and types
print("a:", a, "| type:", type(a))
print("b:", b, "| type:", type(b))
print("c:", c, "| type:", type(c))
print("d:", d, "| type:", type(d))
print("e:", e, "| type:", type(e))
# Step 3: Convert variables and print new types

# Convert string to integer
a_converted = int(a)      # works because "123" is numeric
print("a converted:", a_converted, "| type:", type(a_converted))

# Convert integer to float
b_converted = float(b)
print("b converted:", b_converted, "| type:", type(b_converted))

# Convert float to string
c_converted = str(c)
print("c converted:", c_converted, "| type:", type(c_converted))

# Convert boolean to integer
d_converted = int(d)
print("d converted:", d_converted, "| type:", type(d_converted))

# Convert complex to string
e_converted = str(e)
print("e converted:", e_converted, "| type:", type(e_converted))

# Note: You cannot convert a complex number directly to int or float
# int(e) or float(e) → ❌ Error
    