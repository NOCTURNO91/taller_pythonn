# Ejercicio 1
numeros = (2, 5, 7, 10, 12, 13, 16, 18, 21)

par = ()
impar = ()

for numero in numeros:

    if numero % 2 == 0:

        par += (numero,)
    else:

        impar += (numero,)

print("Tupla de números pares:", par)
print("Tupla de números impares:", impar)

# Ejercicio 2

tupla_numeros = (10, 5, 20, 15, 25)

elemento_mayor = max(tupla_numeros)
print("El elemento mayor de la tupla es:", elemento_mayor)

elemento_menor = min(tupla_numeros)
print("El elemento menor de la tupla es:", elemento_menor)