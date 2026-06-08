N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    pontuacoes = {
        "Rafael": (3 * x) ** 2 + y**2,
        "Beto": 2 * x**2 + (5 * y) ** 2,
        "Carlos": -100 * x + y**3,
    }

    vencedor = max(pontuacoes, key=lambda x: pontuacoes[x])

    print(f"{vencedor} ganhou")
