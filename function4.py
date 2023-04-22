temperaturas = [(20, "Celsius", "Fahrenheit"), 
                (68, "Fahrenheit", "Celsius"), 
                (293.15, "Kelvin", "Celsius")]

for temp in temperaturas:
    valor, origen, destino = temp
    temperatura_convertida = convertidor_temperatura(valor, origen, destino)
    print(f"{valor} {origen} = {temperatura_convertida} {destino}")  