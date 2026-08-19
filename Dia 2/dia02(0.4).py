#Clasificação
nome = input("Digite seu nome: ")  
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print(nome, "é uma criança.")
elif idade >= 13 and idade <= 17:
    print(nome, "é um adolescente.")
elif idade >= 18 and idade <= 59:
    print(nome, "é um adulto.")
elif idade >= 60:
    print(nome, "é um idoso.")