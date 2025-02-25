import random


def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?"

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)
    return ''.join(password)


password_length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(password_length))