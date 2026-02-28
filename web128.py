import random
import string


def generate_password(length=128, num_digits=16, num_special=16, max_attempts=100):
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
            "Password length too small or there is not enough space for digits and special characters."
        )

    for _ in range(max_attempts):
        password = []
        password += random.choices(digits, k=num_digits)
        password += random.choices(specials, k=num_special)
        password += random.choices(all_chars, k=length - num_digits - num_special)

        random.shuffle(password)
        shuffled_password = "".join(password)

        return shuffled_password

    raise RuntimeError(
        "Could not generate a password after the maximum number of attempts."
    )


try:
    password = generate_password()
    print("Password:", password)
except (ValueError, RuntimeError) as e:
    print("Error:", e)
