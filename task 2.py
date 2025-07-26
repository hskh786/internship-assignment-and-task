# Step 1: Input marks for 3 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
# Step 2: Calculate total marks
total = sub1 + sub2 + sub3
print("Total Marks:", total)
# Step 3: Calculate percentage
percentage = (total / 300) * 100
print("Percentage:", percentage)
# Step 4: Assign grade
if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# Step 5: Show grade
print("Grade:", grade)