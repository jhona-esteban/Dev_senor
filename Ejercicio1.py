""""

edad = 17

if edad >=18:
    print("La persona es mayor de edad")
    
else:
    
    print("No es mayor de edad")
    
    
"""

"""
sex = "m"

if sex == "m":
    print("masculino")
elif sex == "f":
    print("Femenino")
else:
    print("Otro genero")
    
"""


edad = int (input("Ingrese su edad: "))

if edad >=0 and edad < 6:
    print("Primera infancia")
elif edad >= 6 and edad < 14:
    print("Infancia")
elif edad >=14 and edad < 18:
    print("Adolecencia")
    
elif edad >18 and edad < 120:
    print("Adulto :p") 
else:
    print("Edad incorrecta")