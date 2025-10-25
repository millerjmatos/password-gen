import random
import string


def has_seq(password):
    # Return True if there are two identical consecutive characters
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
    return False


def has_ambiguous(password):
    # Lookups in sets are faster than in strings.
    ambiguous_chars = set("0Oo1LlIi")
    return any(char in ambiguous_chars for char in password)


def generate_password(length=16, num_count=3, special_count=3, max_attempts=100):
    letters = string.ascii_letters
    digits = string.digits
    specials = "!@#$%^&*><"

    all_chars = letters
    if special_count > 0:
        all_chars += specials
    if num_count > 0:
        all_chars += digits

    if length < (num_count + special_count):
        raise ValueError(
            "Password length too small or not enough space for numbers and special characters."
        )

    for _ in range(max_attempts):
        pwd = []
        pwd += random.choices(digits, k=num_count)
        pwd += random.choices(specials, k=special_count)
        pwd += random.choices(all_chars, k=length - num_count - special_count)

        random.shuffle(pwd)
        shuffled = "".join(pwd)

        if not has_seq(shuffled) and not has_ambiguous(shuffled):
            return shuffled

    raise RuntimeError(
        "Could not generate a password after the maximum number of attempts."
    )


try:
    password = generate_password()
    print("Password:", password)
except (ValueError, RuntimeError) as e:
    print("Error:", e)
