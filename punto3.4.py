# Ejercicio 3
"""numeros = (2, 5, 8, 2, 3, 9, 2, 1, 6, 7)

numeroUsuario = int(input("Ingrese un número: "))

cantidad = numeros.count(numeroUsuario)

if cantidad > 0:
    print(f"El número {numeroUsuario} aparece {cantidad} veces en la tupla.")
else:
    print(f"El número {numeroUsuario} no se encuentra en la tupla.")"""

# Ejercicio 4

datos = {}
while True:
    nombre = input("Ingrese el nombre del contacto (Escribe 'salir' para finalizar el proceso): ")
    if nombre == "salir":
        break
    if nombre in datos:
        print("Ese contacto ya existe. Introduce otro nombre.")
        continue
    celular = input("Introduce el número de teléfono: ")
    datos[nombre] = celular

print("Estos son tus contactos:")
print(datos)