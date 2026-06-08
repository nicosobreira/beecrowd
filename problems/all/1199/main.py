while True:
    entrada = input()

    if entrada[0] == "-":
        break

    if entrada.startswith("0x"):
        print(int(entrada, 16))
    else:
        n = int(entrada)
        print(f"0x{n:X}")
