N = int(input())

leds = {
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "0": 6,
}

for _ in range(0, N):
    n = input()

    ## Podemos reescrever esse loop com o `sum`
    # total = 0
    # for c in n:
    #     total += leds[c]

    total = sum(leds[c] for c in n)

    print(f"{total} leds")
