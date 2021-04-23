#Funções

def imprime():

    print("esta é uma função")

​

imprime()

#com parametro

def imprime(n):

    print(n)

​

imprime("Impressão deste texto")

#com retorno

def potencia(n):

    return n * n

​

x = potencia(3)

print(x)

#com valor default

def intervalo(inic=1,fim=10):

    for n in range(inic, fim+1):

        print(n)

​

x = intervalo(1,10)

y = intervalo()
