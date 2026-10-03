tentativa = 3

while tentativa != 0:
    senha = input("Digite sua senha: ")
    if senha == "123456":
        print("Bem-Vindo, acesso liberado")
        break
    else:
        print("Tente novamente")
    tentativa -= 1