import sys

for linha in sys.stdin:
    expressao = linha.replace("\n", "").replace("\r", "")

    saldo = 0
    correto = True

    for c in expressao:
        if c == "(":
            saldo += 1
        elif c == ")":
            saldo -= 1

            # NOTE: Eu não consegui enxergar a necessidade de usar uma validação aqui
            if saldo < 0:
                correto = False
                break

    correto = False if saldo != 0 else True

    if correto:
        print("correct")
    else:
        print("incorrect")
