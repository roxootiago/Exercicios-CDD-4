def test_primo(n):
    if (n==1):
        return n ,"não é primo"
    elif (n==2):
        return n,"É primo"
    else:
        for i in range(2,n):
            if(n%i == 0):
                return n,"Não é primo"
        return n,"É primo"