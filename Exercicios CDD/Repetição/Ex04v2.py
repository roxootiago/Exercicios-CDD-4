senhaSecreta = "123"
tentativas = 1
senha = input("Digite a senha: ")

while senha != senhaSecreta:
    tentativas += 1
    print("senha incorreta, digite novamente")
    senha = input()
    print(tentativas)

    if tentativas > 2 and senha != senhaSecreta:
        print("conta bloqueada")
        break

else:
    print("senha correta")