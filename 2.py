def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        aux1 = 0
        aux2 = 1
        for i in range(2, n + 1):
            prox = aux1 + aux2
            aux1 = aux2
            aux2 = prox
        return aux2

def acharNumero (num):
    vet = []
    for i in range(num + 1):
        aux = fibo(i)
        vet.append(aux)

    if num == vet[i]:
        print(f'Tem o número: {num}, na sequência.')


numero = input("Digite um número: ")
numero = int(numero)
acharNumero(numero)
