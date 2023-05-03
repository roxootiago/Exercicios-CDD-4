num = int(input("Digite o número da tabuada: "))
limite = int(input("Digite o limite da tabuda: "))

for limite in range( 0,limite+1):
    print(f"{num} x {limite} = {num*limite}")