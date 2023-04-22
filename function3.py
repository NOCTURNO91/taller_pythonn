#def fahrenheit_a_celsius(temperatura):
   
def convertidor_temperatura(valor, origen, destino):
    if origen == "Celsius":
        if destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif destino == "Kelvin":
            return valor + 273.15
        else:
            return valor
    elif origen == "Fahrenheit":
        if destino == "Celsius":
            return (valor - 32) * 5/9
        elif destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
        else:
            return valor
    elif origen == "Kelvin":
        if destino == "Celsius":
            return valor - 273.15
        elif destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32
        else:
            return valor
    else:
        return valor

print(convertidor_temperatura(25, "Celsius", "Fahrenheit"))
#-----------------------------------------------------
temperaturas = [(20, "Celsius", "Fahrenheit"), 
                (68, "Fahrenheit", "Celsius"), 
                (293.15, "Kelvin", "Celsius")]

for temp in temperaturas:
    valor, origen, destino = temp
    temperatura_convertida = convertidor_temperatura(valor, origen, destino)
    print(f"{valor} {origen} = {temperatura_convertida} {destino}")   