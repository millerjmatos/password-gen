import random
import string


def tem_seq(senha):
    for i in range(len(senha) - 1):
        if senha[i] == senha[i + 1]:
            return True
    return False


def tem_ambiguos(senha):
    caracteres_ambiguos = set(
        "0Oo1LlIi"
    )  # Buscas em conjuntos são mais rápidas do que em strings.
    return any(char in caracteres_ambiguos for char in senha)


def gerar_senha(tamanho=32, qtd_numero=7, qtd_especial=7, tentativas_max=1000):
    letras = string.ascii_letters
    numeros = string.digits
    especiais = "!@#$%^&*><"

    todos_caracteres = letras

    if qtd_especial > 0:
        todos_caracteres += especiais
    if qtd_numero > 0:
        todos_caracteres += numeros

    if tamanho < (qtd_numero + qtd_especial):
        raise ValueError(
            "Tamanho da senha muito pequeno ou não há espaço suficiente para números e caracteres especiais."
        )

    for _ in range(tentativas_max):
        senha = []
        senha += random.choices(numeros, k=qtd_numero)
        senha += random.choices(especiais, k=qtd_especial)
        senha += random.choices(todos_caracteres, k=tamanho - qtd_numero - qtd_especial)

        random.shuffle(senha)
        senha_embaralhada = "".join(senha)

        if not tem_seq(senha_embaralhada) and not tem_ambiguos(senha_embaralhada):
            return senha_embaralhada

    raise RuntimeError(
        "Não foi possível gerar uma senha após o número máximo de tentativas."
    )


try:
    senha = gerar_senha()
    print("Senha:", senha)
except (ValueError, RuntimeError) as e:
    print("Erro:", e)
