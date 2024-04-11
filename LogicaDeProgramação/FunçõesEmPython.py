#1
def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ' '.join(str(i) for _ in range(i))
        print(linha.center(2 * n - 1))

def main():
    try:
        valor_n = int(input("Digite um valor inteiro para n: "))
        imprimir_padrao(valor_n)
    except ValueError:
        print("Por favor, insira um valor inteiro válido.")

if __name__ == "__main__":
    main()

#3
def fatorial(n):

    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def verifica_primo(num):

    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


numero_usuario = int(input("Digite um número inteiro: "))

print(f'O fatorial de {numero_usuario} é: {fatorial(numero_usuario)}')


if verifica_primo(numero_usuario):
    print(f'{numero_usuario} é um número primo.')
else:
    print(f'{numero_usuario} não é um número primo.')


#4
def inverte_string(s):

    return s[::-1]

texto_usuario = input("Digite uma string: ")
resultado = inverte_string(texto_usuario)
print(f'A string invertida é: {resultado}')


#5
def maior_valor(lista):

    if not lista:
        return None
    else:
        return max(lista)

numeros = [5, 12, 8, 24, 6, 15]
resultado = maior_valor(numeros)
print(f'O maior valor na lista é: {resultado}')

#6
def conta_vogais(s):

    vogais = "aeiouAEIOU"
    contador_vogais = sum(1 for char in s if char in vogais)
    return contador_vogais

texto_usuario = input("Digite uma string: ")
resultado = conta_vogais(texto_usuario)
print(f'O número de vogais na string é: {resultado}')

#7
def soma_quadrados(lista):

    return sum(x**2 for x in lista)

numeros = [2, 3, 4, 5]
resultado = soma_quadrados(numeros)
print(f'A soma dos quadrados dos números é: {resultado}')


#8
def imprime_tabuada(numero):

    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')


numero_usuario = int(input("Digite um número inteiro: "))
imprime_tabuada(numero_usuario)
