usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == "ADM" and senha == "54321":
    print("Bem-vindo, administrador!")
elif usuario == "USER" and senha == "12345":
    print("Bem-vindo, usuário!")
else: 
    print("Usuário não reconhecido.")