import math
import string


class PasswordEntropyCalculator:
    def __init__(self):
        self.lowercase = set(string.ascii_lowercase)  # a-z
        self.uppercase = set(string.ascii_uppercase)  # A-Z
        self.numbers = set(string.digits)  # 0-9
        self.special = set("!@#$%^&*()_+-=[]{}|;:,.<>?")

    def get_charset_size(self, password: str) -> int:
        """Calcula o tamanho do conjunto de caracteres usado na senha."""
        charset_size = 0
        password_set = set(password)  # Converte a senha para um conjunto para maior eficiência

        # Verifica cada tipo de caractere presente
        if self.lowercase & password_set:
            charset_size += len(self.lowercase)  # 26 caracteres
        if self.uppercase & password_set:
            charset_size += len(self.uppercase)  # 26 caracteres
        if self.numbers & password_set:
            charset_size += len(self.numbers)    # 10 caracteres
        if self.special & password_set:
            charset_size += len(self.special)    # caracteres especiais

        return charset_size

    def calculate_entropy(self, password: str) -> float:
        """
        Calcula a entropia da senha em bits.
        Entropia = comprimento * log2(tamanho_do_conjunto_de_caracteres)
        """
        if not password:
            return 0.0
            
        charset_size = self.get_charset_size(password)
        if charset_size == 0:
            return 0.0
            
        entropy = len(password) * math.log2(charset_size)
        return entropy
    
    def evaluate_strength(self, entropy: float) -> str:
        """Avalia a força da senha baseada na entropia."""
        if entropy < 28:
            return "Muito fraca"
        elif entropy < 36:
            return "Fraca"
        elif entropy < 60:
            return "Razoável"
        elif entropy < 128:
            return "Forte"
        else:
            return "Muito forte"

    def has_lowercase(self, password: str) -> bool:
        return any(c in self.lowercase for c in password)

    def has_uppercase(self, password: str) -> bool:
        return any(c in self.uppercase for c in password)

    def has_numbers(self, password: str) -> bool:
        return any(c in self.numbers for c in password)

    def has_special(self, password: str) -> bool:
        return any(c in self.special for c in password)
    
    def has_uppercase(self, password: str) -> bool:
        return any(c in self.uppercase for c in password)
    
    def count_special_characters(self, password: str) -> int:
        """Conta a quantidade de caracteres especiais na senha."""
        return sum(1 for c in password if c in self.special)

    def count_numbers(self, password: str) -> int:
        """Conta a quantidade de números na senha."""
        return sum(1 for c in password if c in self.numbers)


def main():
    calculator = PasswordEntropyCalculator()
    
    print("\n=== Calculadora de Entropia de Senha ===")
    print("A entropia é uma medida da força da senha.")
    print("Quanto maior a entropia, mais forte a senha.")
    
    while True:
        password = input("\nDigite a senha para análise (ou 'sair' para encerrar): ")
        
        if password.lower() == 'sair':
            break
            
        entropy = calculator.calculate_entropy(password)
        strength = calculator.evaluate_strength(entropy)
        charset_size = calculator.get_charset_size(password)
        num_special = calculator.count_special_characters(password)
        num_numbers = calculator.count_numbers(password)
        
        print(f"\nAnálise da senha:")
        print(f"- Comprimento: {len(password)} caracteres")
        print(f"- Tamanho do conjunto de caracteres: {charset_size}")
        print(f"- Entropia: {entropy:.1f} bits")
        print(f"- Força: {strength}")
        print(f"\nCaracterísticas:")
        print(f"- Contém letras minúsculas: {'✓' if calculator.has_lowercase(password) else '✗'}")
        print(f"- Contém letras maiúsculas: {'✓' if calculator.has_uppercase(password) else '✗'}")
        print(f"- Contém números: {'✓' if calculator.has_numbers(password) else '✗'}")
        print(f"- Quantidade de números: {num_numbers}")
        print(f"- Contém caracteres especiais: {'✓' if calculator.has_special(password) else '✗'}")
        print(f"- Quantidade de caracteres especiais: {num_special}")


if __name__ == "__main__":
    main()
