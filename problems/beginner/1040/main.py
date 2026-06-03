n1, n2, n3, n4 = map(float, input().split())

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / (2 + 3 + 4 + 1)

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
    exit()
elif media < 5.0:
    print("Aluno reprovado.")
    exit()
else:
    print("Aluno em exame.")

n_nova = float(input())
print(f"Nota do exame: {n_nova:.1f}")

media = (media + n_nova) / 2

if media >= 5:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")

print(f"Media final: {media:.1f}")
