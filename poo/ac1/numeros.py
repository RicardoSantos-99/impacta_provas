def digits_count(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i


def sum(n):
    i = digits_count(n)
    s = 0
    while n > 0:
        digit = n % 10
        n //= 10
        s += pow(digit, i)
    return s


# OK
def eh_primo(n):
    qtd = 0
    d = 1
    while d <= n:
        if n % d == 0:
            qtd += 1
        d += 1
    if qtd == 2:
        return True
    else:
        return False
    pass


# OK
def lista_primos(n):
    lista = []
    for i in range(1, n):
        if eh_primo(i):
            lista.append(i)
    return lista


# OK
def conta_primos(list):
    cont = {}
    for i in list:
        if eh_primo(i):
            cont[i] = cont.get(i, 0) + 1
    return cont
    pass


# OK
def eh_perfeito(n):
    sum1 = 0

    for i in range(1, n):
        if (n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        return True
    else:
        return False
    pass


# OK
def lista_perfeitos(n):
    lista = []
    for i in range(1, n):
        if eh_perfeito(i):
            lista.append(i)
    return lista
    pass


# ok
def eh_armstrong(num):
    if sum(num) == num:
        return True
    else:
        return False


# OK
def lista_armstrong(n):
    lista = []
    for i in range(0, n):
        if eh_armstrong(i):
            lista.append(i)
    return lista
    pass


# ok
def eh_quase_armstrong(n):
    if eh_armstrong(n):
        return False
    else:
        return sum(n) == n - 1
    pass
