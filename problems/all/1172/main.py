X = [1] * 10
for i in range(0, 10):
    x = int(input())

    if x > 0:
        X[i] = x

for i, x in enumerate(X):
    print(f"X[{i}] = {x}")
