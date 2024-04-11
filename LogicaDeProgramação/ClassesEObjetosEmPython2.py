#1
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        return self.endereco

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco

# Exemplo de uso:
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
endereco = input("Digite o endereço da pessoa: ")

pessoa1 = Pessoa(nome, idade, endereco)

print("Endereço atual:", pessoa1.mostrar_endereco())

novo_endereco = input("Digite o novo endereço: ")
pessoa1.alterar_endereco(novo_endereco)

print("Novo endereço:", pessoa1.mostrar_endereco())


#2
class Aluno:
    def __init__(self, nome, numero_matricula, curso):
        self.nome = nome
        self.numero_matricula = numero_matricula
        self.curso = curso

    def mostrar_curso(self):
        return self.curso

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso

# Exemplo de uso:
nome = input("Digite o nome do aluno: ")
numero_matricula = input("Digite o número de matrícula do aluno: ")
curso = input("Digite o curso do aluno: ")

aluno1 = Aluno(nome, numero_matricula, curso)

print("Curso atual:", aluno1.mostrar_curso())

novo_curso = input("Digite o novo curso: ")
aluno1.alterar_curso(novo_curso)

print("Novo curso:", aluno1.mostrar_curso())


#3
class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3


def coletar_dados_alunos():
    alunos = []
    for i in range(5):
        matricula = input("Digite a matrícula do aluno {}: ".format(i+1))
        nome = input("Digite o nome do aluno {}: ".format(i+1))
        nota1 = float(input("Digite a nota da primeira prova do aluno {}: ".format(i+1)))
        nota2 = float(input("Digite a nota da segunda prova do aluno {}: ".format(i+1)))
        nota3 = float(input("Digite a nota da terceira prova do aluno {}: ".format(i+1)))
        alunos.append(Aluno(matricula, nome, nota1, nota2, nota3))
    return alunos


def encontrar_maior_media(alunos):
    maior_media = 0
    aluno_maior_media = None
    for aluno in alunos:
        media = aluno.calcular_media()
        if media > maior_media:
            maior_media = media
            aluno_maior_media = aluno
    return aluno_maior_media

def encontrar_menor_media(alunos):
    menor_media = float('inf')
    aluno_menor_media = None
    for aluno in alunos:
        media = aluno.calcular_media()
        if media < menor_media:
            menor_media = media
            aluno_menor_media = aluno
    return aluno_menor_media

def verificar_aprovacao(aluno):
    media = aluno.calcular_media()
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

alunos = coletar_dados_alunos()

aluno_maior_media = encontrar_maior_media(alunos)
print("Aluno com maior média geral:", aluno_maior_media.nome, "- Média:", aluno_maior_media.calcular_media())

aluno_menor_media = encontrar_menor_media(alunos)
print("Aluno com menor média geral:", aluno_menor_media.nome, "- Média:", aluno_menor_media.calcular_media())

print("\nSituação de cada aluno:")
for aluno in alunos:
    situacao = verificar_aprovacao(aluno)
    print(aluno.nome, "-", situacao)


#4
class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def incrementar_segundos(self, segundos):
        total_segundos = self.hora * 3600 + self.minuto * 60 + self.segundo
        total_segundos += segundos
        self.hora = total_segundos // 3600
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60

    def diferenca_horarios(self, outro_horario):
        segundos_atual = self.hora * 3600 + self.minuto * 60 + self.segundo
        segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        diferenca_segundos = abs(segundos_atual - segundos_outro)
        hora_dif = diferenca_segundos // 3600
        minuto_dif = (diferenca_segundos % 3600) // 60
        segundo_dif = diferenca_segundos % 60
        return hora_dif, minuto_dif, segundo_dif

# Exemplo de uso:
hora1 = Horario(10, 30, 45)
hora2 = Horario(12, 15, 30)

print("Horário 1:", hora1.hora, "h", hora1.minuto, "min", hora1.segundo, "s")
print("Horário 2:", hora2.hora, "h", hora2.minuto, "min", hora2.segundo, "s")

hora1.incrementar_segundos(500)
print("\nHorário 1 após incrementar 500 segundos:", hora1.hora, "h", hora1.minuto, "min", hora1.segundo, "s")

hora2.incrementar_segundos(200)
print("Horário 2 após incrementar 200 segundos:", hora2.hora, "h", hora2.minuto, "min", hora2.segundo, "s")

diferenca = hora1.diferenca_horarios(hora2)
print("\nDiferença entre os horários:", diferenca[0], "h", diferenca[1], "min", diferenca[2], "s")


#5
class Carro:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrar_preco(self):
        return self.preco

    def mostrar_dados(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, Preço: {self.preco}"

# Exemplo de uso:
carro1 = Carro("Toyota", 2020, 30000)
carro2 = Carro("Ford", 2018, 25000)

print("Preço do carro 1:", carro1.mostrar_preco())
print("Dados do carro 1:", carro1.mostrar_dados())

print("\nPreço do carro 2:", carro2.mostrar_preco())
print("Dados do carro 2:", carro2.mostrar_dados())


#6
class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_humor(self):
        humor = (self.fome + self.saude) / 2
        return humor

tamagushi = Tamagushi("Tammy", 5, 8, 2)

print("Nome:", tamagushi.retornar_nome())
print("Fome:", tamagushi.retornar_fome())
print("Saúde:", tamagushi.retornar_saude())
print("Idade:", tamagushi.retornar_idade())
print("Humor:", tamagushi.retornar_humor())

tamagushi.alterar_fome(3)
tamagushi.alterar_saude(6)

print("\nApós alterar fome para 3 e saúde para 6:")
print("Fome:", tamagushi.retornar_fome())
print("Saúde:", tamagushi.retornar_saude())
print("Novo humor:", tamagushi.retornar_humor())


#7
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        if self.bucho:
            print(f"Conteúdo do bucho de {self.nome}: {', '.join(self.bucho)}")
        else:
            print(f"{self.nome} está com o bucho vazio.")

    def digerir(self):
        self.bucho = []

macaco1 = Macaco("Macaco 1")
macaco2 = Macaco("Macaco 2")

macaco1.comer("Banana")
macaco2.comer("Maçã")
macaco1.comer("Pêssego")
macaco2.comer("Pão")

macaco1.ver_bucho()
macaco2.ver_bucho()

macaco1.digerir()
macaco2.digerir()
macaco1.ver_bucho()
macaco2.ver_bucho()
macaco1.comer("Macaco 2")

macaco1.ver_bucho()
macaco1.digerir()
macaco1.ver_bucho()





