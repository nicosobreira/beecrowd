N = int(input())

pares = []
impares = []

for _ in range(N):
    numero = int(input())

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

pares.sort()
impares.sort(reverse=True)

print("\n".join(map(str, pares)))
print("\n".join(map(str, impares)))
