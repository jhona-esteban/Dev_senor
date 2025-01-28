Edades = [5,12,17,18,24,32] #Lista#

def MayorEdad(x):
    if x<18:
        return False
    else:
        return True

adulto = filter (MayorEdad,Edades)

for x in adulto:
    print(x)

print(adulto)

print("Te pase xd")


