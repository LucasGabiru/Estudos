#Festa
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ingresso = input("Você possui ingresso? (S/N) ")
if idade >= 18 and (ingresso == "s" or ingresso == "S" or ingresso == "sim" or ingresso == "Sim" or ingresso == "Yes" or ingresso == "yes"):
    print("Você pode entrar na festa.")
elif idade < 18 and (ingresso == "s" or ingresso == "S"):
    print("Você não pode entrar na festa, pois é menor de idade.")
elif idade >= 18 and (ingresso == "n" or ingresso == "N" or ingresso == "não" or ingresso == "Não" or ingresso == "nao" or ingresso == "Nao" or ingresso == "no" or ingresso == "No"):
    print("Você não pode entrar na festa.")