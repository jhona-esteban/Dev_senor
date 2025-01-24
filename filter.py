Edades = [5,12,17,18,24,32] #Lista#

def MayorEdad(x):
    if x<18:
        return False
    else:
        return True

adultos = filter (MayorEdad,Edades)

for x in adultos:
    print(x)

print(adultos)

