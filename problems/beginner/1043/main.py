A, B, C = map(float, input().split())

X, Y, Z = sorted([A, B, C], reverse=True)

if X < Y + Z:
    print(f"Perimetro = {A + B + C}")
else:
    print(f"Area = {(A + B) * C / 2}")
