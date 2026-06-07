# BeeCrowd

## Truques

### `zip`

``` python
um = "ab"
dois = "cd"

inverso = [a + b for a, b in zip(um, dois)]

print("".join(inverso))
```

> `acbd`

### `sum`

``` python
lista = [1, 2, 3, 4]

total = sum(e for e in lista)
```

> `10`

### print de lista em espaço

``` python
lista = [1, 2, 3, 4]

print(*lista)
```

> `1 2 3 4`

### `max` e `min` com `key`

``` python
palavras = ["boi", "ornitorrinco", "gato"]

maior_palavra = max(palavras, key=len)

print(maior_palavra)
```

> `ornitorrinco`

### `any` e `all`

``` python
numeros = [5, 10, 20, -3, 8, 15]

if all(n >= 0 for n in numeros):
    print("Dados válidos")

if any(n < 0 for n in numeros):
    print("Dados Inválidos")
```

> `Dados Inválidos`

### `input` e `round`

Quando trabalhar com dinheiro ou tempo.

``` python
entrada = int(round(float(input()) * 100))
```

## Lista de Exercícios

- [x] 1173
- [x] 1174
- [x] 1168
- [x] 1253
- [x] 1220
- [x] 1161
- [x] 1024
- [x] 1238
- [ ] 1555
- [ ] 1199
- [x] 2242
