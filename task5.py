# Step 1: Ask user questions
name = input("What is your name? ")
food = input("What is your favorite food? ")
birth_year = input("What is your birth year? ")
fav_number = input("What is your favorite number? ")
language = input("What is your favorite programming language? ")

# Step 2: Display summary using f-strings
print("\n📄 Survey Summary")
print("=" * 30)
print(f"👤 Name: {name}")
print(f"🍔 Favorite Food: {food}")
print(f"🎂 Birth Year: {birth_year}")
print(f"🔢 Favorite Number: {fav_number}")
print(f"💻 Favorite Language: {language}")
print("=" * 30)
print(f"\nThank you, {name}! Your responses have been recorded.")
