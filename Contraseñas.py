import string
import random

logi = int(input("Ingrese el tamaño de la contraseña: "))

carateres = string.ascii_letters + string.digits + string.punctuation

contrasena = "".join(random.choice(carateres) for i in range (logi))

print("La contraseña generada es: " + contrasena)

