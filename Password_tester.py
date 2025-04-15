import re

def password_strength(password):
    # Check password length
    length_score = len(password)
    if length_score < 8:
        print("Password is too short. Aim for at least 8 characters.")
        return "Weak"

    # Check for variety of characters
    variety_score = 0
    if any(char.islower() for char in password):
        variety_score += 1
    if any(char.isupper() for char in password):
        variety_score += 1
    if any(char.isdigit() for char in password):
        variety_score += 1
    if any(char in "!@#$%^&*()-_+=<>?/|~`" for char in password):
        variety_score += 1

    # Check for common weaknesses
    common_patterns = ["123", "password", "qwerty", "abc", "111"]
    if any(pattern in password.lower() for pattern in common_patterns):
        print("Password contains common patterns. Avoid using easily guessed words or sequences.")
        return "Weak"

    # Assign overall strength
    if length_score >= 12 and variety_score == 4:
        return "Strong"
    elif variety_score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Main program
def main():
    print("Welcome to the Password Strength Tester!")
    while True:
        password = input("Enter a password to test its strength (or type 'exit' to quit): ").strip()
        if password.lower() == 'exit':
            print("Thanks for using the Password Strength Tester. Goodbye!")
            break
        strength = password_strength(password)
        print(f"Your password strength is: {strength}\n")

if __name__ == "__main__":
    main()
