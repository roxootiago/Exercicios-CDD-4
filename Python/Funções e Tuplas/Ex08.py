def letras(t):
    count = 0
    textoi = " "
    for x in t:
        if x not in " ":
          count += 1
    print(count)

    for y in range(len(t)-1,-1,-1):
        textoi+=t[y]
    print(textoi)


letras("o py tá on")