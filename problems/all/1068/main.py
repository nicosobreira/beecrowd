import sys

for linha in sys.stdin:
    expressao = linha.replace("\n", "").replace("\r", "")

    parenteses = [p for p in expressao if p in "()"]

    if len(parenteses) % 2 != 0:
        print("incorrect")
        continue

    print(*parenteses)
