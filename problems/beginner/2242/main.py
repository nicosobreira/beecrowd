risada = input()

ri_vogais = [v for v in risada if v in "aeiou"]

if all(a == b for a, b in zip(ri_vogais, reversed(ri_vogais))):
    print("S")
else:
    print("N")
