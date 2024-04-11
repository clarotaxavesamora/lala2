# 1
print("hello,word!!")

# 2
num = int(input("mostra um num bb "))

#4
num1 = float(input("mostra primeira nota "))
num2 = float(input("mostra segunda nota "))
num3 = float(input("mostra terceira nota "))
num4 = float(input("mostra quarta nota "))

med = float

med = (num1 + num2 + num3 + num4)/4
print(med)

#5
metros = float(input('digite o valor em metros:'))
centimetro = float
centimetro = metros * 100
print(f'{metros:.2} metros enquivalem a {centimetro:.2f} centimetro. ')

#6
raio = float(input("Digite o raio do círculo: "))
comprimento = 2 * 3.14 * raio
area = 3.14*((raio)**2)

print ('um circulo do raio:', raio, ' unidade' )
print ('tem um comprimento de dois pontos', comprimento, 'unidade' )
print ('e area de:', area, 'unidade')

# 7
lado1 = float
lado2 = float
area = float
dobro_da_area = float

lado1= float(input("digite o primeiro lado"))
lado2= float(input("digite o segundo lado"))

area = lado1* lado2
dobro_da_area = area * 2

print ("mostrar o dobro da area," ,dobro_da_area)

#8
horas = float
num_horas = float
salario = float

horas = float (input("diga quanto voce ganha por horas"))
num_horas = float (input("digite o numero de horas trabalhadas no mes"))
salario = horas * num_horas
print("voce recebe:" ,salario)

#9
graus_f = float
graus_c = float

graus_f = float(input("peça a temperatura em graus Fahrenheit"))
graus_c = 5 * ((graus_f - 32) / 9)

print(f"A temperatura em Celsius é: {graus_c:.2f} graus Celsius")


#10
graus_f = float
graus_c = float

graus_c = float(input("peça a temperatura em graus celsius: "))
graus_f = graus_c * 1.8 + 32

print(f"A temperatura em Fahrenheit é: {graus_f:.2f} graus Fahrenheit")
