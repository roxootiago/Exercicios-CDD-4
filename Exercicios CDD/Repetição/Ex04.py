count = 0
senha = "zorosola"


while count < 3:
    senhaSecreta = input("Digite sua senha: ")
    if senhaSecreta != senha:
        print("Senha inválida!")

    else:
        print("Senha correta!")
        break


    count = count + 1

