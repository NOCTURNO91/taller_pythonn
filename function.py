#imprimir los numeros del 10 al 1.

"""def Mostrar(num):
    print(num)
    if num > 0:
        Mostrar(num-1)
Mostrar(10)    

#factoriL de un numero 6 = 6*5*4*3*2 #factorial de 6
def factorial(valor):
    if valor > 1:
        valor = valor * factorial(valor - 1)

    return valor
print(factorial(6))"""

#Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es.
def es_primo(num):
    """
     verifica si un número es primo.
    """
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(es_primo(66))




