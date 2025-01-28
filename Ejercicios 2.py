var = int(input("Deseas ver el numero multiplicado? que vas a ingresar 1 si o 2 no: "))

while var == 1:
    try:
        tabla = int(input("Que numero deseas ver su tabla de multiplicar?: "))
        for i in range (1, 11):
            
            print(i*tabla)
        var = int(input("Deseas ingresar otro número? Ingresa 1 para sí o 2 para no: "))
    except ValueError:
        print(("Ingrese un numero por favor "))
        
print("Gracias por participar")
