V = int(input())

N = [0] * 10

for i in range(0, 10):
    N[i] = V

    print(f"N[{i}] = {N[i]}")
    V *= 2
