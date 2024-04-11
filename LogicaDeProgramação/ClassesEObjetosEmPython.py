#1
 class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        """Muda o valor do lado do quadrado."""
        self.lado = novo_lado

    def retornar_lado(self):
        """Retorna o valor do lado do quadrado."""
        return self.lado

    def calcular_area(self):
        """Calcula a área do quadrado."""
        area = self.lado ** 2
        return area

quadrado1 = Quadrado(5)

print("Lado do quadrado:", quadrado1.retornar_lado())

print("Área do quadrado:", quadrado1.calcular_area())

quadrado1.mudar_lado(7)
print("Novo lado do quadrado:", quadrado1.retornar_lado())

print("Nova área do quadrado:", quadrado1.calcular_area())


#2 Crie uma classe que modele um retangulo:
class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudar_lados(self, novo_lado_a, novo_lado_b):
        """Muda os valores dos lados do retângulo."""
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornar_lados(self):
        """Retorna os valores dos lados do retângulo."""
        return self.lado_a, self.lado_b

    def calcular_area(self):
        """Calcula a área do retângulo."""
        area = self.lado_a * self.lado_b
        return area

    def calcular_perimetro(self):
        """Calcula o perímetro do retângulo."""
        perimetro = 2 * (self.lado_a + self.lado_b)
        return perimetro

def main():
    lado_a = float(input("Informe a medida do lado A: "))
    lado_b = float(input("Informe a medida do lado B: "))

    local = Retangulo(lado_a, lado_b)

    area_local = local.calcular_area()
    perimetro_local = local.calcular_perimetro()

    quantidade_pisos = area_local
    quantidade_rodapes = perimetro_local

    print("\nPara o local com medidas {}x{}:".format(lado_a, lado_b))
    print("Quantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)

if __name__ == "__main__":
    main()


#3 Crie uma classe que modele uma pessoa:
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        """Envelhece a pessoa e ajusta a altura conforme a regra."""
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)

    def engordar(self, peso_ganho):
        """Aumenta o peso da pessoa."""
        self.peso += peso_ganho

    def emagrecer(self, peso_perdido):
        """Reduz o peso da pessoa."""
        self.peso -= peso_perdido

    def crescer(self, altura_ganha):
        """Aumenta a altura da pessoa."""
        self.altura += altura_ganha

    def informacoes(self):
        """Retorna informações sobre a pessoa."""
        return f"{self.nome}, {self.idade} anos, {self.peso} kg, {self.altura} cm"

pessoa1 = Pessoa(nome="clara", idade=17, peso=60, altura=170)

print("Informações iniciais:", pessoa1.informacoes())

pessoa1.envelhecer(3)

pessoa1.engordar(5)

pessoa1.emagrecer(2)

print("Informações finais:", pessoa1.informacoes())

#4 Crie uma classe para implementar uma conta corrente.
class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        """Altera o nome do correntista."""
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        """Realiza um depósito na conta."""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        """Realiza um saque na conta."""
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        elif valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def informacoes_conta(self):
        """Retorna informações sobre a conta corrente."""
        return f"Número da Conta: {self.numero_conta}\nCorrentista: {self.nome_correntista}\nSaldo: R${self.saldo:.2f}"

conta1 = ContaCorrente(numero_conta="12345", nome_correntista="xavier")

print("Informações iniciais da conta:")
print(conta1.informacoes_conta())

conta1.deposito(1000)

conta1.saque(500)

conta1.alterar_nome("angelina")

print("\nInformações finais da conta:")
print(conta1.informacoes_conta())


#5
class Televisor:
    def __init__(self):
        self.canal = 1
        self.volume = 50

    def alterar_canal(self, novo_canal):
        """Altera o número do canal."""
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
            print(f"Canal alterado para {novo_canal}.")
        else:
            print("Número do canal inválido. Mantendo o canal atual.")

    def aumentar_volume(self):
        """Aumenta o nível de volume."""
        if self.volume < 100:
            self.volume += 1
            print(f"Volume aumentado para {self.volume}.")
        else:
            print("Volume máximo atingido.")

    def diminuir_volume(self):
        """Diminui o nível de volume."""
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume diminuído para {self.volume}.")
        else:
            print("Volume mínimo atingido.")

def main():
    televisor = Televisor()

    while True:
        print("\n===== Controle Remoto =====")
        print("1. Alterar Canal")
        print("2. Aumentar Volume")
        print("3. Diminuir Volume")
        print("0. Desligar Televisor")

        escolha = input("Escolha uma opção (0-3): ")

        if escolha == "1":
            novo_canal = int(input("Digite o número do canal desejado (1-100): "))
            televisor.alterar_canal(novo_canal)
        elif escolha == "2":
            televisor.aumentar_volume()
        elif escolha == "3":
            televisor.diminuir_volume()
        elif escolha == "0":
            print("Desligando o televisor. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
