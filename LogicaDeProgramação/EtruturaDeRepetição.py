#1
nota = float(input('Digite uma nota entre zero e dez: '))

if 0 <= nota <= 10:
        print('Você digitou a nota ', nota)
else:
        print('Nota inválida')


#2
usuario = str(input("digite seu nome de ususario "))
senha = str(input("digite sua senha"))
if usuario == senha:
   print("não pode o nome de usuario igual a senha " )
   usuario = str(input("digite outro nome"))
   senha = str(input("digite outra senha"))
else:
     print("usuario valido!" )


#3

print("Números de 1 a 20 abaixo um do outro:")
for numero in range(1, 21):
    print(numero)

print("\nNúmeros de 1 a 20 ao lado um do outro:")
for numero in range(1, 21):
    print(numero, end=" ")


#4

num1 = float(input('digite o primeiro numero'))
num2 = float(input('digite o primeiro numero'))
num3 = float(input('digite o primeiro numero'))
num4 = float(input('digite o primeiro numero'))
num5 = float(input('digite o primeiro numero'))

if (num1>num2) and (num1>num3) and (num1 >num3) and (num1>num4) and (num1>num5):
  print ('o primeiro numero é o maior')
elif (num2>num1) and (num2>num3) and (num2 >num4) and (num2>num5):
  print ('o segundo numero é o maior')
elif (num3>num1) and (num3>num2) and (num3>num4) and (num3>num5):
  print ('o terceiro numero é o maior')
elif (num4>num1) and (num4>num2) and (num4 >num3) and (num4>num5):
  print ('o quarto numero é o maior')
elif (num5>num1) and (num5>num2) and (num5>num3) and (num5>num4):
  print ('o quinto numero é o maior')

#5
num1 = float(input('informe o primeiro numero: '))
num2 = float(input('informe o segundo numero: '))
num3 = float(input('informe o terceiro numero: '))
num4 = float(input('informe o quarto numero: '))
num5 = float(input('informe o quinto numero: '))

soma = float
media = float
soma = num1 + num2 + num3 + num4 + num5
media =  (num1 + num2 + num3 + num4 + num5) / 2
print('a soma dos numeros é: ', soma)
print('a media dos numeros é: ', media)

#6
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
for i in range(1, 51):
    if i % 2 > 0:
        print(i)

#7
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))


if numero1 > numero2:
    numero1, numero2 = numero2, numero1

soma = 0
print(f"Números no intervalo entre {numero1} e {numero2}:")
for i in range(numero1, numero2 + 1):
    print(i, end=" ")
    soma += i

print('Soma dos números no intervalo: ', soma)

#8
numero = int(input("Digite um número inteiro entre 1 e 10: "))


if 1 <= numero <= 10:
    print(f"\nTabuada de {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
else:
    print("Número fora do intervalo permitido.")

#9
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for _ in range(expoente):
    resultado *= base

print(f"{base} elevado a {expoente} é igual a {resultado}")

#10
quantidade_pares = 0
quantidade_impares = 0

for _ in range(10):
    numero = int(input("Digite um número inteiro: "))

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1

print(f"\nQuantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
