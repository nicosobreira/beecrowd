from bisect import bisect_left


def binary_search(arr, target):
    index = bisect_left(arr, target)

    if index < len(arr) and arr[index] == target:
        return index
    return -1


caso = 1

while True:
    N, Q = map(int, input().split())

    if N == Q == 0:
        break

    marmores: list[int] = []
    for _ in range(N):
        marmores.append(int(input()))

    consultas: list[int] = []
    for _ in range(Q):
        consultas.append(int(input()))

    marmores.sort()

    print(f"CASE# {caso}:")
    for consult in consultas:
        encontrado_em = binary_search(marmores, consult)

        if encontrado_em >= 0:
            print(f"{consult} found at {encontrado_em + 1}")
        else:
            print(f"{consult} not found")

    caso += 1
