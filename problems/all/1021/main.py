N = int(round(float(input()) * 100))  # Converte de reais para centavos

# Tudo em centavos!
notas = [100 * 100, 50 * 100, 20 * 100, 10 * 100, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    qtd = N // nota
    N %= nota

    print(f"{qtd} nota(s) de R$ {nota / 100:.2f}")

print("MOEDAS:")
for moeda in moedas:
    qtd = N // moeda
    N %= moeda

    print(f"{qtd} moeda(s) de R$ {moeda / 100:.2f}")

"""
N = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [0.5, 0.25, 0.1, 0.05, 0.01]

N_abs = int(abs(N))

print("NOTAS:")
for nota in notas:
    qtd = N_abs // nota  # Divisão inteira

    N_abs %= nota  # Módulo

    print(f"{qtd} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")

print(f"{N_abs // 1} moeda(s) de R$ {1:.2f}")

N_moeda = int((N % 1) * 100)

for moeda in moedas:
    qtd = N_moeda // int(moeda * 100)  # Divisão inteira

    N_moeda %= int(moeda * 100)  # Módulo

    print(f"{qtd} moeda(s) de R$ {moeda:.2f}")
"""
