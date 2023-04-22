#Utilizando la función del punto 1, realizar otra función que reciba de
#parámetro una lista de números y devuelva sólo aquellos que son primos en
#otra lista

def es_primo(num):
    """
    Función que verifica si un número es primo.
    """
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def lista_de_primos(lista):
    primos = []
    for num in lista:
        if es_primo(num):
            primos.append(num)
    return primos
  
lista1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_de_primos(lista1))