senha = []
login = []
count = 0

print("===================\n")
print("         Seja bem-vindo         ")
for i in range (2):
    login.append( input("Digite o login: "))

    senha.append(input("Digite a senha: "))

loginDeUsuario = input("Digite o nome de usuário: ")
senhaDeUsuario = input("Digite a senha de usuário :")

for x in range(2):

    if loginDeUsuario == login[x] and senhaDeUsuario[x] == senha:
        print("Login efetuado")
        break
    elif loginDeUsuario != login[x] or senhaDeUsuario != senha[x]:
        print("Login ou senha diferentes")
        break
    else:
        count += 1
