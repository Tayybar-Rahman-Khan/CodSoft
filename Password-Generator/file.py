import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be a positive integer. Please try again.")
            else:
                password = generate_password(length)
                print("Generated Password: ", password)
                break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the length.")

if __name__ == "__main__":
    main()
