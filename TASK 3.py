import random
import string

def generating_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")

    # Get user input for password length
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number for the length.")
        return

    # Check if the length is non-negative
    if length <= 0:
        print("Please enter a positive number for the length.")
        return

    # Generate and display the password
    password = generating_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
