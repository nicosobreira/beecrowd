def leia_numero_entre(min: int, max: int) -> int:
    while True:
        entrada: str = input()

        numero: int = int(entrada)
        if numero >= min and numero <= max:
            return numero


N: int = leia_numero_entre(0, 10000)

total_de_pecas: int = int(((N + 1) * (N + 2)) / 2)

print(total_de_pecas)
