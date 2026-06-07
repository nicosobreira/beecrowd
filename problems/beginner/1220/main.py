while True:
    n = int(input())

    if n <= 0:
        break

    A = [0] * n
    soma = 0

    # 1. Leitura segura e conversão 100% para inteiros
    for i in range(n):
        A[i] = int(round(float(input()) * 100))
        soma += A[i]

    # 2. A média permanece float (para usarmos o truque do int)
    media_exata = soma / n

    dar = 0
    receber = 0

    # 3. Calculamos os dois lados da moeda
    for x in A:
        if x < media_exata:
            dar += int(media_exata - x)  # Automaticamente usa a média para baixo
        elif x > media_exata:
            receber += int(x - media_exata)  # Automaticamente usa a média para cima

    # 4. A resposta é o maior valor de transferência
    total = max(dar, receber)

    # 5. Voltamos para o formato de dólares para imprimir
    print(f"${total / 100:.2f}")
