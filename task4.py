# Step 1: Ask for username
username = input("Enter username: ")

# Step 2: Ask for password
password = input("Enter password: ")

# Step 3: Check if both username and password are correct
if username == "admin" and password == "1234":
    print("Access Granted ")
else:
    print("Access Denied ")
