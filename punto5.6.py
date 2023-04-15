#punto 5

agenda = {}
continuar = True

while continuar:
    nombre = input("Ingrese el nombre del contacto: ")
    if nombre in agenda:
        print("El nombre ya existe en la agenda.")
    else:
        telefono = input("Ingrese el teléfono del contacto: ")
        agenda[nombre] = telefono
        respuesta = input("¿Desea ingresar otro contacto? (s/n): ")
        if respuesta.lower() == "n":
            continuar = False

print("Agenda de contactos:")
print(agenda)

buscar_nombre = input("Ingrese el nombre del contacto para buscar su teléfono: ")
if buscar_nombre in agenda:
    print("El teléfono de", buscar_nombre, "es", agenda[buscar_nombre])
else:
    print("El nombre no se encuentra en la agenda.")


#punto 6

"""tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

indice = int(input("Ingrese un índice para mostrar el valor de la tupla: "))

if indice < 0 or indice >= len(tupla):
    print("El índice ingresado es inválido.")
else:
    print("El valor de la tupla en el índice", indice, "es", tupla[indice])"""