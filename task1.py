import math
import statistics
numbers = [16, 25, 36, 49, 64]
for num in numbers:
    print(f"√{num} = {math.sqrt(num)}")
average = statistics.mean(numbers)
print("Average:", average)
