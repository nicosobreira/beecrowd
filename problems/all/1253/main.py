N = int(input())

for _ in range(0, N):
    palavra = input()
    key = int(input())

    # Usamos do `- key` para ir a **esquerda**, ou seja, descriptografar
    descrip = "".join(chr(ord("A") + (ord(c) - ord("A") - key) % 26) for c in palavra)

    print(descrip)
