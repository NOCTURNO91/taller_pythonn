# taller 9

numeros = []


while True:
    numero = input("Ingrese un número entero (o escriba 'fin' para terminar): ")
    if numero == 'fin':
        break
    numeros.append(int(numero))


numeros_ascendente = sorted(numeros)
numeros_descendente = sorted(numeros, reverse=True)

print("Lista ordenada de forma ascendente:", numeros_ascendente)
print("Lista ordenada de forma descendente:", numeros_descendente)
