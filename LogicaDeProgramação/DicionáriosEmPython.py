#1
def main():

    meu_dicionario = {}


    meu_dicionario['nome'] = 'João'
    meu_dicionario['idade'] = 25
    meu_dicionario['cidade'] = 'Exemploville'


    print("Dicionário atualizado:")
    for chave, valor in meu_dicionario.items():
        print(f'{chave}: {valor}')

if __name__ == "__main__":
    main()

#2
def main():

    produtos_precos = {}

    for _ in range(3):
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: R$ "))
        produtos_precos[nome_produto] = preco_produto


    print("\nProdutos e Preços:")
    for produto, preco in produtos_precos.items():
        print(f'{produto}: R$ {preco:.2f}')

if __name__ == "__main__":
    main()

#3
def main():

    notas = {}


    for i in range(1, 5):
        nota = float(input(f"Digite a nota {i}: "))
        notas[f'Nota {i}'] = nota


    media = sum(notas.values()) / len(notas)


    print("\nNotas inseridas:")
    for chave, valor in notas.items():
        print(f'{chave}: {valor}')

    print(f'\nMédia das notas: {media:.2f}')

if __name__ == "__main__":
    main()

#4
def main():

    caixa_misteriosa = {}


    for i in range(1, 5):
        item = input(f"Insira o item {i} na Caixa Misteriosa: ")
        caixa_misteriosa[i] = item

    numero_usuario = int(input("Digite um número de 1 a 4: "))


    if 1 <= numero_usuario <= 4:

        item_selecionado = caixa_misteriosa[numero_usuario]
        print(f"\nNa posição {numero_usuario} da Caixa Misteriosa temos: {item_selecionado}")
    else:
        print("Número inválido. Por favor, digite um número de 1 a 4.")

if __name__ == "__main__":
    main()

#5
def main():

    funcionarios = {}


    for i in range(1, 4):
        nome_funcionario = input(f"Digite o nome do funcionário {i}: ")
        funcionarios[i] = nome_funcionario

    print("\nFuncionários cadastrados:")
    for chave, valor in funcionarios.items():
        print(f'{chave}: {valor}')

    numero_demitir = int(input("\nDigite o número do funcionário que deseja demitir (1 a 3): "))

    if 1 <= numero_demitir <= 3:
        del funcionarios[numero_demitir]

        print("\nFuncionários restantes:")
        for chave, valor in funcionarios.items():
            print(f'{chave}: {valor}')
    else:
        print("Número inválido. Por favor, digite um número de 1 a 3.")

if __name__ == "__main__":
    main()
