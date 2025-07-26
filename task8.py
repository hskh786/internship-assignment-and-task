# Celsius to Fahrenheit Conversion
try:
    celsius = float(input("🌡️ Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"✅ {celsius}°C is equal to {fahrenheit:.2f}°F")
except ValueError:
    print("❌ Invalid input! Please enter a number for Celsius.")

# Fahrenheit to Celsius Conversion
try:
    fahrenheit_input = float(input("\n🌡️ Enter temperature in Fahrenheit: "))
    celsius_converted = (fahrenheit_input - 32) * 5/9
    print(f"✅ {fahrenheit_input}°F is equal to {celsius_converted:.2f}°C")
except ValueError:
    print("❌ Invalid input! Please enter a number for Fahrenheit.")
