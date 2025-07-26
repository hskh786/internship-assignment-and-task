user_input = input("Enter any value: ")
print("Python thinks this is of type:", type(user_input))
try:
    int_value = int(user_input)
    print("You entered an integer!")
except ValueError:
    print("You did not enter an integer.")
    try:
        float_value = float(user_input)
        print("You entered a float!")
    except ValueError:
        print("You entered a string!")
# Step 1: Declare variables
a = "123"          # String
b = 123            # Integer
c = 123.45         # Float      
