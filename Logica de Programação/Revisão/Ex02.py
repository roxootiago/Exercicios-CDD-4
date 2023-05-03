while True:
    num = int(input("Digite um número: "))
    if num == 0:
        print("Digite um número diferente de 0")
    elif num >0:
        print(f"{num} é positivo!")
        break
    else:
        print(f"{num} é negativo!")
        break
