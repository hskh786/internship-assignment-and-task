counter=0
def change_counter():
    global counter
    counter += 1
    return counter
print("Counter value:", change_counter(), counter)