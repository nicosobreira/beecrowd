"""
def leia_peca():
    p1, p2, p3 = input().split()
    codigo = int(p1)
    numero = int(p2)
    valor = float(p3)

    return (codigo, numero, valor)


c_1, n_1, v_1 = leia_peca()
c_2, n_2, v_2 = leia_peca()

total_1: float = n_1 * v_1
total_2: float = n_2 * v_2

total: float = total_1 + total_2

print(f"VALOR A PAGAR: R$ {total:.2f}")
"""

_, n1, v1 = input().split()
_, n2, v2 = input().split()

total = int(n1) * float(v1) + int(n2) * float(v2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
