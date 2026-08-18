#Sistema para loja
print("Bem-vindo ao sistema da loja!")
print("Aqui você pode calcular a quantidade vezes o valor do produto.")
nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preço = int(input("Digite o preço do produto: "))
total =  quantidade * preço
print("Produto: " + nome_produto)
print("Preço: " + str(preço))
print("Quantidade: " + str(quantidade))
print("Total: " + str(total))
