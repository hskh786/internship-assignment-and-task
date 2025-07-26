import os
import re

# Step 1: List all files in current folder
files = os.listdir(".")

# Step 2: Create regex pattern: starts with 'report', ends with .txt
pattern = re.compile(r"^task.*\.py")

# Step 3: Filter files that match the pattern
matching_files = [f for f in files if pattern.match(f)]

# Step 4: Print matched files
print("Matching .txt files that start with 'report':")
for file in matching_files:
    print(file)
