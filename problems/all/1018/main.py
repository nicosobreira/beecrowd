"""
N = int(input())

valores = [100, 50, 20, 10, 5, 2, 1]
cedulas = [0, 0, 0, 0, 0, 0, 0]

for i, nota in enumerate(valores):
    while N >= nota:
        cedulas[i] += 1
        N -= nota
    print(f"{cedulas[i]} notas(s) de R$ {nota:.2f}")
"""

N = int(input())

valores = [100, 50, 20, 10, 5, 2, 1]

print(N)

for nota in valores:
    qtd = N // nota  # Divisão inteira

    N %= nota  # Módulo

    print(f"{qtd} nota(s) de R$ {nota},00")
