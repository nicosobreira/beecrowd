SIZE = 4  # O valor 4 é para teste, mude para 100 na hora

A = [0.0] * SIZE

for i in range(0, SIZE):
    a = float(input())
    A[i] = a

    if a <= 10:
        print(f"A[{i}] = {a}")
