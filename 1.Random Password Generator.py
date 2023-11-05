import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: You must select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter the length of the password: "))
    use_letters = input("Use letters (Y/N): ").strip().lower() == 'y'
    use_numbers = input("Use numbers (Y/N): ").strip().lower() == 'y'
    use_symbols = input("Use symbols (Y/N): ").strip().lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print("Generated Password: ", password)

if __name__ == "__main__":
    main()