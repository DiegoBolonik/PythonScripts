#1. Faça um programa que tenha uma função chamada amplitude. A função deve receber uma lista e imprimir a amplitude.
#Crie também um código para testar sua função

def amplitude(vet):
    print("Amplitude:", max(vet) - min(vet))

vetor = [12,23,45,2,100]    
amplitude(vetor)

#2. Faça uma função que receba uma string e imprima esta string na forma vertical

def imprime(texto):
    for n in range(0, len(texto)):
        print(texto[n])

imprime("Cientista")

#3. Crie um programa que leia o peso de uma carga em números inteiros. 
#Se o peso for até 10 kg, informe que o valor será de R$ 50,00. 
#Entre 11 e 20 kg, informe que o valor será de R$ 80. 
# Se for maior que  20 informe que o transporte não é aceito. Teste vários pesos.

peso = 10
if peso <= 10:
	print("Valor da carga é de R$ 50,00")
 
elif peso >= 11 and peso <=20:
	print("Valor da carga é de R$ 80,00")
 
else:
	print("O transporte não é aceito")
