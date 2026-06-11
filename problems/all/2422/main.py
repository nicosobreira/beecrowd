# NOTE: Foi usada a **estratégia do ponteiro duplo**

N = int(input())

# Daria para tirar proveito do fato da lista estar em ordem crescente? Se sim, como?
C = []  # Em ordem **crescente**

for _ in range(N):
    C.append(int(input()))

K = int(input())

esquerda = 0
direita = N - 1

while esquerda < direita:
    if C[esquerda] + C[direita] > K:
        direita -= 1
    elif C[esquerda] + C[direita] < K:
        esquerda += 1
    else:
        print(f"{C[esquerda]} {C[direita]}")
        break
