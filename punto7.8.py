#taller 8 Crear una lista vacía

departamentos_colombia = []
ultimos = []

# cantidad de departamentos a ingresar
cantidad_departamentos = int(input("Ingrese la cantidad de departamentos que desea agregar: "))

# Recorrer un ciclo for para pedir al usuario los departamentos y agregarlos a la lista.
for i in range(cantidad_departamentos):
    departamento = input(f"Ingrese el departamento #{i+1} de Colombia: ")
    departamentos_colombia.append(departamento)

ultimos = departamentos_colombia[-2:]

# pedir que ordene la lista en orden descendente.
departamentos_colombia.sort(reverse=True)

# Imprimir la lista ordenada:
print("             ")
print(f"Lista de departamentos de Colombia en orden descendente: {departamentos_colombia}")

# Imprimia los dos últimos departamentos ingresados:
print(f"Los dos últimos departamentos ingresados son:  {ultimos}")