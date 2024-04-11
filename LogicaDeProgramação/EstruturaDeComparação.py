# 1
valor1 = float (input("digite um numero "))
if valor1 > 0:
    print("O valor é positivo.")
elif valor1 < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")


#2
sexo = str (input("digite se voce feminino ou masculino "))
if sexo == "m":
   print("voce é do sexo masculino! ")
elif sexo == "f":
    print("voce é do sexo feminino! ")
else:
    print("voce é sexo invalido! ")


#3
letra = str (input("digite uma letra "))
if letra  in 'aeiou':
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")

#4
nota1 = float(input('digite a primeira nota '))
nota2 = float(input('digite a segunda nota '))
media = float

media= (nota1 + nota2) /2

if media == 10:
  print("voce foi aprovado com distinção! ")
elif media < 7:
  print("voce foi reprovada! ")
elif media > 7:
  print("voce foi aprovado! ")


#5
num1 = int(input("digite o primeiro numero "))
num2 = int(input("digite o segundo numero "))
num3 = int(input("digite o terceiro numero "))

if (num1 > num2) and (num1 > num3):
  print("o numero 1 é maior")
elif(num2>num1) and (num2>num3):
  print("o numero 2 é maior")
else:
  print("o numero 3 é maior ")

#6
num1 = int(input("digite o primeiro numero "))
num2 = int(input("digite o segundo numero "))
num3 = int(input("digite o terceiro numero "))

if (num1<num2) and (num1 < num3):
  print("o numero 1 é menor ")
elif(num2<num1) and (num2<num3):
  print("o numero 2 é menor ")
else:
  print("o numero 3 é menor ")

#7
preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))

if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
    produto_mais_barato = "Produto 1"
elif preco_produto2 < preco_produto1 and preco_produto2 < preco_produto3:
    produto_mais_barato = "Produto 2"
else:
    produto_mais_barato = "Produto 3"
print(f"Você deve comprar o {produto_mais_barato}, pois é o mais barato.")


8#
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))


numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)

print("Os números em ordem decrescente são:", numeros)
