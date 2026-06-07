v = input()
c = input()
a = input()

key = f"{v} {c} {a}"

animais = {
    "vertebrado ave carnivoro": "aguia",
    "vertebrado ave onivoro": "pomba",
    #
    "vertebrado mamifero onivoro": "homem",
    "vertebrado mamifero herbivoro": "vaca",
    #
    "invertebrado inseto hematofago": "pulga",
    "invertebrado inseto herbivoro": "lagarta",
    #
    "invertebrado anelideo hematofago": "sanguessuga",
    "invertebrado anelideo onivoro": "minhoca",
}

print(animais[key])

"""
v = input()
c = input()
a = input()

animais = {
    ("vertebrado", "ave", "carnivoro"): "aguia",
    ("vertebrado", "ave", "onivoro"): "pomba",
    #
    ("vertebrado", "mamifero", "onivoro"): "homem",
    ("vertebrado", "mamifero", "herbivoro"): "vaca",
    #
    ("invertebrado", "inseto", "hematofago"): "pulga",
    ("invertebrado", "inseto", "herbivoro"): "lagarta",
    #
    ("invertebrado", "anelideo", "hematofago"): "sanguessuga",
    ("invertebrado", "anelideo", "onivoro"): "minhoca",
}

print(animais[(v, c, a)])

"""

"""
vertebrado = input()
classe = input()
alimento = input()

if vertebrado == "vertebrado":
    if classe == "ave":
        if alimento == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if alimento == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if classe == "inseto":
        if alimento == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if alimento == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
"""
