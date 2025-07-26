# Step 1: Declare variables with different data types
full_name = "25"              # string that looks like a number
age = 18                      # integer
height = 5.9                  # float
is_student = True             # boolean
complex_number = 3 + 4j       # complex number

# Step 2: Print original values and types
print("Original Values and Types:")
print(f"full_name: {full_name}, type: {type(full_name)}")
print(f"age: {age}, type: {type(age)}")
print(f"height: {height}, type: {type(height)}")
print(f"is_student: {is_student}, type: {type(is_student)}")
print(f"complex_number: {complex_number}, type: {type(complex_number)}")

print("\nConverted Values and Types:")

# Step 3: Convert and print new types

# String to int
try:
    full_name_int = int(full_name)
    print(f"full_name converted to int: {full_name_int}, type: {type(full_name_int)}")
except ValueError:
    print("Cannot convert 'full_name' to int")

# Integer to float
age_float = float(age)
print(f"age converted to float: {age_float}, type: {type(age_float)}")

# Float to string
height_str = str(height)
print(f"height converted to string: {height_str}, type: {type(height_str)}")

# Boolean to int
is_student_int = int(is_student)
print(f"is_student converted to int: {is_student_int}, type: {type(is_student_int)}")

# Complex to string
complex_str = str(complex_number)
print(f"complex_number converted to string: {complex_str}, type: {type(complex_str)}")

# Complex to int (not allowed)
try:
    complex_int = int(complex_number)
    print(f"complex_number converted to int: {complex_int}")
except TypeError:
    print("Cannot convert 'complex_number' to int directly (raises TypeError)")
