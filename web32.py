import random
import string


def has_consecutive_duplicates(password):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
    return False


def has_ambiguous_chars(password):
    # Membership tests in sets are faster than in strings.
    ambiguous_chars = set("0Oo1LlIi")
    return any(char in ambiguous_chars for char in password)


def generate_password(length=32, num_digits=7, num_special=7, max_attempts=1000):
    letters = string.ascii_letters
    digits = string.digits
    specials = "!@#$%^&*><"

    all_chars = letters

    if num_special > 0:
        all_chars += specials
    if num_digits > 0:
        all_chars += digits

    if length < (num_digits + num_special):
        raise ValueError(
            "Password length too small or not enough room for digits and special characters."
        )

    for _ in range(max_attempts):
        password = []
        password += random.choices(digits, k=num_digits)
        password += random.choices(specials, k=num_special)
        password += random.choices(all_chars, k=length - num_digits - num_special)

        random.shuffle(password)
        shuffled_password = "".join(password)

        if not has_consecutive_duplicates(shuffled_password) and not has_ambiguous_chars(shuffled_password):
            return shuffled_password

    raise RuntimeError(
        "Unable to generate a password after the maximum number of attempts."
    )


try:
    pwd = generate_password()
    print("Password:", pwd)
except (ValueError, RuntimeError) as e:
    print("Error:", e)
