from datetime import date


print("Hello World:")
print("hello world")
print("\n")
print("Soma de Dois Números:")
a = int(input("Primeiro numero:"))
b = int(input("Segundo numero:"))
print(a+b)
print("\n")
print("Mensagem de Saudação:")
nome = input("Nome:")
print("Olá "+nome)
print("\n")
print("Contagem de 1 a 10:")
i = 0
while( i <= 10):
    print(i)
    i+=1
print("\n")
print("Tabuada:")
a = int(input("Numero:"))
i = 1
while( i <= 10):
    print(f' {a} x {i} = {i*a}')
    i+=1
print("\n")
print("Calculadora de Idade:")
c = int(input("Ano de Nascimento:"))
print(2023-c)
print("\n")
print("Verificador de Maioridade:")
d = int(input("Idade:"))
if(d>=18):
    print("maior")
else:
    print("menor")
print("\n")
print("Mostrar dia da semana:")
print(date.today().day)
print("\n")
print("Numero Favorito:")
e = int(input("Numero:"))
print(e)
print("\n")
print("Trocar Valores:")
f = int(input("Numero 1:"))
g = int(input("Numero 2:"))
aux = f
f = g 
g = aux
print(f'{f} {g}')
print("Calculadora de Média")
h = int(input("Numero 1:"))
i = int(input("Numero 2:"))
j = int(input("Numero 3:"))
print((h+i+j)/3)

