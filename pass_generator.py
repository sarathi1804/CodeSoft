import random
import string
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
        if not characters:
        raise ValueError("At least one character set must be selected")
            password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation)
    except ValueError as e:
        print(e)
        return
    print("Generated Password:", password)
if __name__ == "__main__":
    main()