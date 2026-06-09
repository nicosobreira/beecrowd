import sys

for linha in sys.stdin:
    sentenca = linha.replace("\n", "").replace("\r", "")

    dancing = []
    is_upper = True

    for c in sentenca:
        if c.isspace():
            dancing.append(c)
        else:
            dancing.append(c.upper() if is_upper else c.lower())
            is_upper = not is_upper

    print("".join(dancing))

"""
while True:
    # Será que não dá para substituir esse `try except`?
    try:
        sentenca = input()
    except EOFError:
        break

    dancing = [c for c in sentenca]

    is_upper = True
    for i in range(0, len(dancing)):
        if dancing[i].isspace():
            continue

        if is_upper:
            dancing[i] = dancing[i].upper()
        else:
            dancing[i] = dancing[i].lower()

        is_upper = not is_upper

    print("".join(dancing))
"""
