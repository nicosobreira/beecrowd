N = int(input())

for _ in range(N):
    S = input()

    Q = int(input())

    for _ in range(Q):
        R = input()

        start = -1  # Esse -1 é por causa do `start + 1`
        for r in R:
            start = S.find(r, start + 1)

            if start < 0:
                break

        if start >= 0:
            print("Yes")
        else:
            print("No")
