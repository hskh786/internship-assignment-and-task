# Step 1: Ask for number of products
products = int(input("Enter the number of products: "))

# Step 2: Ask for total price
price = float(input("Enter the total price: "))
# Step 3: Apply discount conditions
if price > 1000 and products > 3:
    discount = price * 0.15   # 15% discount
elif price > 500:
    discount = price * 0.10   # 10% discount
else:
    discount = 0              # No discount
    print("Original Price:", price)
print("Discount Applied:", discount)
final_price = price - discount
print("Final Price to Pay:", final_price)

