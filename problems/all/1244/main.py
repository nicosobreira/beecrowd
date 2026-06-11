N = int(input())

for _ in range(N):
    entrada = input().split()

    entrada.sort(key=len, reverse=True)

    print(*entrada)
