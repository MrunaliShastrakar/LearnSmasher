import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters  # includes both uppercase and lowercase letters
    
    if include_digits:
        characters += string.digits
    
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, include_digits, include_special_chars)
    print("Generated password:", password)

if __name__ == "__main__":
    main()
