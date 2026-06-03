"""
def maior(a, b):
    return int((a + b + abs(a - b)) / 2)


a, b, c = map(int, input().split())

ab = maior(a, b)
final = maior(ab, c)

print(f"{final} eh o maior")
"""

maior = lambda x, y: int((x + y + abs(x - y)) / 2)

a, b, c = map(int, input().split())

print(f"{maior(maior(a, b), c)} eh o maior")
