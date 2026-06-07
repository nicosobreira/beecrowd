valores = map(float, input().split())

A, B, C = sorted(valores, reverse=True)

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    A_2 = A**2
    BC_2 = B**2 + C**2
    if A_2 == BC_2:
        print("TRIANGULO RETANGULO")
    elif A_2 > BC_2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")

"""
a, b, c = map(float, input().split())

if a > b and a > c:
    A = a
    if b > c:
        B = b
        C = c
    else:
        B = c
        C = b
else:
    if b > a and b > c:
        A = b
        if a > c:
            B = a
            C = c
        else:
            B = c
            C = a
    else:
        A = c
        if a > b:
            B = a
            C = b
        else:
            B = b
            C = a

"""
