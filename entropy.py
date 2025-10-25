import math
import string


class PasswordEntropyCalculator:
    def __init__(self):
        self.lowercase = set(string.ascii_lowercase)  # a-z
        self.uppercase = set(string.ascii_uppercase)  # A-Z
        self.numbers = set(string.digits)  # 0-9
        self.special = set("!@#$%^&*()_+-=[]{}|;:,.<>?")

    def get_charset_size(self, password: str) -> int:
        """Calculate the size of the character set used by the password."""
        charset_size = 0
        password_set = set(password)  # convert password to a set for efficiency

        # Check each character type presence
        if self.lowercase & password_set:
            charset_size += len(self.lowercase)  # 26 characters
        if self.uppercase & password_set:
            charset_size += len(self.uppercase)  # 26 characters
        if self.numbers & password_set:
            charset_size += len(self.numbers)    # 10 characters
        if self.special & password_set:
            charset_size += len(self.special)    # special characters

        return charset_size

    def calculate_entropy(self, password: str) -> float:
        """
        Calculate the password entropy in bits.
        Entropy = length * log2(size_of_character_set)
        """
        if not password:
            return 0.0

        charset_size = self.get_charset_size(password)
        if charset_size == 0:
            return 0.0

        entropy = len(password) * math.log2(charset_size)
        return entropy

    def evaluate_strength(self, entropy: float) -> str:
        """Evaluate password strength based on entropy."""
        if entropy < 28:
            return "Very weak"
        elif entropy < 36:
            return "Weak"
        elif entropy < 60:
            return "Reasonable"
        elif entropy < 128:
            return "Strong"
        else:
            return "Very strong"

    def has_lowercase(self, password: str) -> bool:
        return any(c in self.lowercase for c in password)

    def has_uppercase(self, password: str) -> bool:
        return any(c in self.uppercase for c in password)

    def has_numbers(self, password: str) -> bool:
        return any(c in self.numbers for c in password)

    def has_special(self, password: str) -> bool:
        return any(c in self.special for c in password)

    def count_special_characters(self, password: str) -> int:
        """Count how many special characters are in the password."""
        return sum(1 for c in password if c in self.special)

    def count_numbers(self, password: str) -> int:
        """Count how many digits are in the password."""
        return sum(1 for c in password if c in self.numbers)


def main():
    calculator = PasswordEntropyCalculator()

    print("\n=== Password Entropy Calculator ===")
    print("Entropy is a measure of password strength.")
    print("Higher entropy means a stronger password.")

    while True:
        password = input("\nEnter the password to analyze (or 'exit' to quit): ")

        if password.lower() == 'exit':
            break

        entropy = calculator.calculate_entropy(password)
        strength = calculator.evaluate_strength(entropy)
        charset_size = calculator.get_charset_size(password)
        num_special = calculator.count_special_characters(password)
        num_numbers = calculator.count_numbers(password)

        print(f"\nPassword analysis:")
        print(f"- Length: {len(password)} characters")
        print(f"- Character set size: {charset_size}")
        print(f"- Entropy: {entropy:.1f} bits")
        print(f"- Strength: {strength}")
        print(f"\nCharacteristics:")
        print(f"- Contains lowercase letters: {'✓' if calculator.has_lowercase(password) else '✗'}")
        print(f"- Contains uppercase letters: {'✓' if calculator.has_uppercase(password) else '✗'}")
        print(f"- Contains numbers: {'✓' if calculator.has_numbers(password) else '✗'}")
        print(f"- Number of digits: {num_numbers}")
        print(f"- Contains special characters: {'✓' if calculator.has_special(password) else '✗'}")
        print(f"- Number of special characters: {num_special}")


if __name__ == "__main__":
    main()
