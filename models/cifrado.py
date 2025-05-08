class Cifrado:
    
    @staticmethod
    def cifrar_numero(numero):
        """
        Cifra un número de 6 dígitos siguiendo el algoritmo especificado
        """
        # Validar que sea un número de 6 dígitos
        if not isinstance(numero, int) or numero < 0 or len(str(numero).zfill(6)) != 6:
            raise ValueError("El número debe ser un entero de 6 dígitos")
        
        # Asegurar que el número tenga 6 dígitos (rellenar con ceros a la izquierda si es necesario)
        digitos = [int(d) for d in str(numero).zfill(6)]
        
        # Paso 1: Sumar 7 a cada dígito y obtener el residuo de la división entre 10
        for i in range(len(digitos)):
            digitos[i] = (digitos[i] + 7) % 10
        
        # Paso 2: Intercambiar posiciones
        digitos[0], digitos[2] = digitos[2], digitos[0]  # Intercambiar 1er y 3er dígito
        digitos[1], digitos[3] = digitos[3], digitos[1]  # Intercambiar 2do y 4to dígito
        digitos[4], digitos[5] = digitos[5], digitos[4]  # Intercambiar 5to y 6to dígito
        
        # Convertir la lista de dígitos de vuelta a un número
        resultado = int(''.join(map(str, digitos)))
        return resultado
    
    @staticmethod
    def descifrar_numero(numero_cifrado):
        """
        Descifra un número previamente cifrado, revirtiendo el proceso
        """
        # Validar que sea un número de 6 dígitos o menos (puede tener ceros a la izquierda)
        if not isinstance(numero_cifrado, int) or numero_cifrado < 0:
            raise ValueError("El número cifrado debe ser un entero positivo")
        
        # Asegurar que el número tenga 6 dígitos (rellenar con ceros a la izquierda si es necesario)
        digitos = [int(d) for d in str(numero_cifrado).zfill(6)]
        
        # Verificar que ahora tenemos exactamente 6 dígitos
        if len(digitos) != 6:
            raise ValueError("El número cifrado debe tener 6 dígitos")
        
        # Paso 1: Intercambiar posiciones (reverso del cifrado)
        digitos[0], digitos[2] = digitos[2], digitos[0]  # Intercambiar 1er y 3er dígito
        digitos[1], digitos[3] = digitos[3], digitos[1]  # Intercambiar 2do y 4to dígito
        digitos[4], digitos[5] = digitos[5], digitos[4]  # Intercambiar 5to y 6to dígito
        
        # Paso 2: Revertir la suma de 7 (equivalente a sumar 3)
        for i in range(len(digitos)):
            digitos[i] = (digitos[i] + 3) % 10
        
        # Convertir la lista de dígitos de vuelta a un número
        resultado = int(''.join(map(str, digitos)))
        return resultado