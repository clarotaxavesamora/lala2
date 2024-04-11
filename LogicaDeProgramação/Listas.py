#1
idades = []
alturas = []

for i in range(5):
    idades.append(int(input(f"Digite a idade da pessoa {i + 1}: ")))
    alturas.append(float(input(f"Digite a altura da pessoa {i + 1} (em metros): ")))

print("\nIdades e alturas na ordem inversa:")
for idade, altura in zip(reversed(idades), reversed(alturas)):
    print(f"Idade: {idade}, Altura: {altura:.2f} metros")


#2
vetor = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

soma_quadrados = sum(x**2 for x in vetor)

print(f"\nA soma dos quadrados dos elementos do vetor é: {soma_quadrados}")

#3
vetor_A = []
vetor_B = []

print("Digite os elementos para o vetor A:")
for _ in range(10):
    elemento_A = input("Digite um elemento: ")
    vetor_A.append(elemento_A)


print("\nDigite os elementos para o vetor B:")
for _ in range(10):
    elemento_B = input("Digite um elemento: ")
    vetor_B.append(elemento_B)

vetor_intercalado = [a for pair in zip(vetor_A, vetor_B) for a in pair]

print("\nTerceiro vetor intercalado:")
print(vetor_intercalado)

#4
vetor_A = []
vetor_B = []
vetor_C = []


print("Digite os elementos para o vetor A:")
for _ in range(10):
    elemento_A = input("Digite um elemento: ")
    vetor_A.append(elemento_A)

print("\nDigite os elementos para o vetor B:")
for _ in range(10):
    elemento_B = input("Digite um elemento: ")
    vetor_B.append(elemento_B)


print("\nDigite os elementos para o vetor C:")
for _ in range(10):
    elemento_C = input("Digite um elemento: ")
    vetor_C.append(elemento_C)

vetor_intercalado = [a for triple in zip(vetor_A, vetor_B, vetor_C) for a in triple]

print("\nQuarto vetor intercalado:")
print(vetor_intercalado)

#5
idades = []
alturas = []

for i in range(10):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    altura = float(input(f"Digite a altura do aluno {i + 1} (em metros): "))

    idades.append(idade)
    alturas.append(altura)


media_alturas = sum(alturas) / len(alturas)


alunos_count = sum(1 for i in range(10) if idades[i] > 13 and alturas[i] < media_alturas)


print(f"\nQuantidade de alunos com mais de 13 anos e altura inferior à média: {alunos_count}")
