"""
Estratégia: Como as strings são **imutáveis**, trate elas como **listas** e ao final faça um `join`
"""

N = int(input())

for _ in range(N):
    texto = input()

    #                       Primeira Regra                    Segunda regra
    #                             v                                 v
    lista = [chr(ord(c) + 3) if c.isalpha() else c for c in texto][::-1]

    # Terceira Regra

    metade = len(lista) // 2
    for i in range(metade, len(lista)):
        lista[i] = chr(ord(lista[i]) - 1)

    print("".join(lista))

"""
N = int(input())

for _ in range(0, N):
    texto = input()

    primeira = ""
    for c in texto:
        if c.isalpha():
            primeira += chr(ord(c) + 3)
        else:
            primeira += c

    segunda = primeira[::-1]

    metade = len(segunda) // 2
    terceira = segunda[0:metade]

    for c in segunda[metade:]:
        terceira += chr(ord(c) - 1)

    print(terceira)
"""
