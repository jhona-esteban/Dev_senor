import hashlib

# 1. Función para crear un hash usando SHA-256
def crear_hash(texto):
    hash_obj = hashlib.sha256(texto.encode())  # Convertir texto a hash
    return hash_obj.hexdigest()  # Devolver el hash en formato hexadecimal

# 2. Función para simular descifrar un hash con un diccionario
def descifrar_hash(hash_dado, diccionario):
    for palabra in diccionario:
        if crear_hash(palabra) == hash_dado:
            return f"¡Coincidencia encontrada! La palabra es: {palabra}"
    return "No se encontró ninguna coincidencia en el diccionario."

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un hash de ejemplo
    texto = "Jhonatan Esteban"
    hash_generado = crear_hash(texto)
    print(f"Hash generado: {hash_generado}")

    # Simular un ataque de diccionario
    diccionario_palabras = ["admin", "Jhonatan", "Esteban", "clave123", "password"]
    resultado = descifrar_hash(hash_generado, diccionario_palabras)
    print(resultado)
