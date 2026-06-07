import math

while True:
    try:
        entrada = input()
    except EOFError:
        break

    N, M = map(int, entrada.split())

    print(math.factorial(N) + math.factorial(M))
