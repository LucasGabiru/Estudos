#Calculadora
numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))
if operacao == "+": 
    resultado = numero1 + numero2
    print("O resultado da soma é:", resultado)
elif operacao == "-":
    resultado = numero1 - numero2
    print("O resultado da subtração é:", resultado)
elif operacao == "*":
    resultado = numero1 * numero2
    print("O resultado da multiplicação é:", resultado)
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("O resultado da divisão é:", resultado)
    else:
        print("Erro")