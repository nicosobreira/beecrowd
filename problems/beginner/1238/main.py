N = int(input())

for _ in range(N):
    um, dois = input().split()

    # O `zip` vai parar quando os tamanhos forem diferentes
    intercalado = "".join([a + b for a, b in zip(um, dois)])

    sobra = um[len(dois) :] + dois[len(um) :]

    print(intercalado + sobra)


"""
N = int(input())

for _ in range(N):
    um, dois = input().split()

    menor = min(len(um), len(dois))

    m = 0
    n = 1

    r = [""] * 100
    for i in range(menor):
        r[m] = um[i]
        r[n] = dois[i]

        m += 2
        n += 2

    if menor == len(um):
        for c in dois[menor : len(dois)]:
            r += c
    else:
        for c in um[menor : len(um)]:
            r += c

    print("".join(r))
"""
