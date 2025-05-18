import random
import string
print("welcome to popassword generator ")
# Define character sets
letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = string.digits          # '0123456789'
symbols = "!@#$%^&*()_+{}[]:;<>,.?/"

# Combine all characters
all_chars = letters + digits + symbols

# Ask user how long the password should be
length = int(input("Enter desired password length: "))

# Generate password
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Your secure password is:", password)
