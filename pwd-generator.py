import random
from math import log2

def generate_password(length, charset):
    return ''.join(random.choice(charset) for _ in range(length))

def main():
    length = int(input("Enter the password length: "))

    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    specials = '!"#€%&/()=?+\''

    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").lower() == 'y'
    charset = ''
    if use_lowercase:
        charset += lowercase
    if use_uppercase:
        charset += uppercase
    if use_digits:
        charset += digits
    if use_specials:
        charset += specials
    
    charSpace = len(charset)
    password = generate_password(length, charset)
    
    print(f"Entropy is: {log2(charSpace**length)}")
    print(f"Generated password is: {password}")

if __name__ == "__main__":
    main()
