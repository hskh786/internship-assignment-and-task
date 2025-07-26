# Step 1: Get marks from user for 5 subjects
subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))
subject4 = int(input("Enter marks for Subject 4: "))
subject5 = int(input("Enter marks for Subject 5: "))

# Step 2: Calculate total and percentage
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100  # assuming each subject is out of 100

# Step 3: Determine grade
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
else:
    grade = "Fail"

# Step 4: Display results
print("\n📊 Result Summary")
print("=========================")
print(f"Total Marks: {total_marks} / 500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
