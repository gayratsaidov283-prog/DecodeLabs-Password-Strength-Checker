
from getpass import getpass

COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
    "welcome123",
}


def check_password(password):
    if not isinstance(password, str):
        raise TypeError("Password must be a string")

    if len(password) < 8:
        return "Weak"

    if password.lower() in COMMON_PASSWORDS:
        return "Weak"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    score = sum((has_upper, has_lower, has_digit, has_symbol))

    if len(password) >= 12 and score == 4:
        return "Strong"
    elif score >= 3:
        return "Medium"

    return "Weak"


def get_recommendations(password):
    recommendations = []

    if len(password) < 12:
        recommendations.append("Use at least 12 characters.")

    if not any(c.isupper() for c in password):
        recommendations.append("Add uppercase letters.")

    if not any(c.islower() for c in password):
        recommendations.append("Add lowercase letters.")

    if not any(c.isdigit() for c in password):
        recommendations.append("Add numbers.")

    if not any(not c.isalnum() for c in password):
        recommendations.append("Add special characters.")

    if password.lower() in COMMON_PASSWORDS:
        recommendations.append("Avoid common passwords.")

    return recommendations


if __name__ == "__main__":
    password = getpass("Enter your password: ")

    strength = check_password(password)
    print("\nPassword Strength:", strength)

    recommendations = get_recommendations(password)

    if recommendations:
        print("\nRecommendations:")
        for item in recommendations:
            print("-", item)
    else:
        print("All configured checks passed.")
