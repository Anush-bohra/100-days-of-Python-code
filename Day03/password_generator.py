# Day03/password_generator.py
import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    n = input("Password length (default 12): ").strip()
    length = int(n) if n.isdigit() and int(n) > 0 else 12
    print("Generated password:", generate_password(length))
