import random
import string
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(8))
print("Your random 8-character password is:", password)