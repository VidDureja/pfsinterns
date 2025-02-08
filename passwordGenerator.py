import random
import string

def generate_password(length, include_numbers, include_special):
    # Define character sets
    characters = string.ascii_lowercase  # Lowercase letters
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    # Generate the password
    pas = ''.join(random.choice(characters) for _ in range(length))
    return pas

# Get user input
print("Welcome to the Password Generator!")
password_length = int(input("Enter password length: "))
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and print the password
password = generate_password(password_length, use_numbers, use_special, )
print(f"Your generated password is: {password}")
