# BeeCrowd

## Truques

### `zip`

``` python
um = "ab"
dois = "cd"

inverso = [a + b for a, b in zip(um, dois)]

print("".join(inverso))
```

> Resultado: `acbd`

### `sum`

``` python
lista = [1, 2, 3, 4]

total = sum(e for e in lista)
```

> Resultado: `10`

### print de lista em espaço

``` python
lista = [1, 2, 3, 4]

print(*lista)
```

> Resultado: `1 2 3 4`

### `max` e `min` com `key`

``` python
conta = {
    "Amanda": 12,
    "Pedro": 2,
    "Carlos": 100,
}

print(max(conta, key = lambda k: conta[k]))
```

> Resultado: `Carlos`



``` python
palavras = ["boi", "ornitorrinco", "gato"]

maior_palavra = max(palavras, key=len)

print(maior_palavra)
```

> Resultado: `ornitorrinco`

### `any` e `all`

``` python
numeros = [5, 10, 20, -3, 8, 15]

if all(n >= 0 for n in numeros):
    print("Dados válidos")

if any(n < 0 for n in numeros):
    print("Dados Inválidos")
```

> Resultado: `Dados Inválidos`

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
- [x] 1555
- [x] 1199
- [x] 2242

- [ ] 1120
- [ ] 1234
- [ ] 1028

- [ ] 1068
- [ ] 1025
- [ ] 1244
- [ ] 1259
- [ ] 1507
- [ ] 2422
- [ ] 1237

