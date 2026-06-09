import math

N = int(input())

for _ in range(N):
    F1, F2 = map(int, input().split())

    # Preciso achar o __Máximo Multiplo Comum__ entre F1 e F2

    """
    maximo, minimo = max(F1, F2), min(F1, F2)
    while minimo != 0:
        maximo, minimo = minimo, maximo % minimo
    """

    mmc = math.gcd(F1, F2)

    print(mmc)
