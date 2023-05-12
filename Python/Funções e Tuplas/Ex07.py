text = input("Digite um texto: ")
def texto (t):
    count = 0
    for x in t:
        if x not in " ":
            count+= 1
    print(count)
    print("-"*30)
    for i in range(-1,-(count+1),-1):
        print(t[i], end=" ")
    return

texto(text)