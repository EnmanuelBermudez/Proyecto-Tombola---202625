import struct
import datetime

def Aux_Creación_Clave(Clave, Indice=0, Mayus=0, Minus=0, Num=0, Esp=0, Invalidos=0, Consec_Actual=1, Max_Consec=1):
    """
    Valida la Clave de forma recursiva según los criterios del Reto 1.
    Retorna una lista con los mensajes de Error de los criterios que no se cumplieron.
    """
    # Caso base: se recorrió toda la cadena de la Clave
    if Indice == len(Clave):
        Errores = []
        
        # 1. Longitud entre 6 y 10 caracteres
        if not (6 <= len(Clave) <= 10):
            Errores.append("[❌] Debe poseer entre 6 y 10 caracteres.")
            
        # 2. Combinación de mayúsculas, minúsculas y números
        if Mayus == 0:
            Errores.append("[❌] Debe contener al menos una letra mayúscula.")
        if Minus == 0:
            Errores.append("[❌] Debe contener al menos una letra minúscula.")
        if Num == 0:
            Errores.append("[❌] Debe contener al menos un número.")
            
        # 3. Caracteres inválidos (acentos, ñ, Ñ)
        if Invalidos > 0:
            Errores.append("[❌] No debe contener letras con acentos ni la letra Ñ o ñ.")
            
        # 4. Caracteres Especiales permitidos
        if Esp == 0:
            Errores.append("[❌] Debe contener al menos uno de los siguientes caracteres Especiales: asterisco (*), igual (=), porcentaje (%) o guión bajo (_).")
            
        # 5. Máximo de caracteres consecutivos
        if Max_Consec > 3:
            Errores.append("[❌] La Clave NO debe contener más de 3 caracteres iguales de forma consecutiva.")
            
        return Errores

    # Paso recursivo: analizar el carácter actual
    char = Clave[Indice]
    
    # Validar qué tipo de carácter es
    es_Mayus = 1 if 'A' <= char <= 'Z' else 0
    es_Minus = 1 if 'a' <= char <= 'z' else 0
    es_Num = 1 if '0' <= char <= '9' else 0
    es_Esp = 1 if char in ['*', '=', '%', '_'] else 0
    
    # Validar si es un carácter no permitido explícitamente o ajeno al abecedario inglés estándar
    es_invalido = 1 if char in 'áéíóúÁÉÍÓÚñÑäëïöüÄËÏÖÜ ' or (not any([es_Mayus, es_Minus, es_Num, es_Esp])) else 0

    # Lógica para contar caracteres consecutivos
    Nuevo_Consec = Consec_Actual
    if Indice > 0 and Clave[Indice] == Clave[Indice - 1]:
        Nuevo_Consec += 1
    else:
        Nuevo_Consec = 1
        
    Nuevo_Max_Consec = max(Max_Consec, Nuevo_Consec)

    # Llamada recursiva avanzando al siguiente índice
    return Aux_Creación_Clave(
        Clave, 
        Indice + 1, 
        Mayus + es_Mayus, 
        Minus + es_Minus, 
        Num + es_Num, 
        Esp + es_Esp, 
        Invalidos + es_invalido, 
        Nuevo_Consec, 
        Nuevo_Max_Consec
    )

def Registro_Jugadores(Cedula, Nombre, Sexo, Fecha, InicialEstado, Clave):
    Formato_Registro = '8s30s1s10s3s20s30s'
    Tamaño_Registro = struct.calcsize(Formato_Registro)
    FR_Estados = '20s3s'
    TR_Estados = struct.calcsize(FR_Estados)

    AF_JUGADORES = "JUGADORES.bin"
    JUGADORES = open(AF_JUGADORES, 'ab')
    AF_ESTADOS = "ESTADOS.bin"
    ESTADOS = open(AF_ESTADOS, 'rb')

    NombreEstado = ""

    EOF = False
        
    while (len(Fecha) != 10) or (Fecha[2] != '-' and Fecha[2] != '/') or (Fecha[5] != '-' and Fecha[5] != '/'):
        Fecha = str(input("[ERROR:] La fecha de nacimiento ha sido colocada erroneamente. Intente nuevamente: "))
    
    EstEncontrado = False

    while (EstEncontrado == False):
        ESTADOS.seek(0)
        EOF = False
        while (EOF == False) and (EstEncontrado == False):
            BytesEstados = ESTADOS.read(TR_Estados)
            if (BytesEstados):
                NombreEstCodificado, InicialEstCodificado = struct.unpack(FR_Estados, BytesEstados)
                NombreEstExistente = NombreEstCodificado.decode('utf-8').strip()
                InicialEstExistente = InicialEstCodificado.decode('utf-8').strip()

                if (InicialEstado == InicialEstExistente):
                    NombreEstado = NombreEstExistente
                    EstEncontrado = True
            else:
                EOF = True

        if (EstEncontrado == False):
            InicialEstado = input("[ERROR:] La inicial de estado colocada no existe. Intente nuevamente: ")

    """
    Función principal que interactúa con el usuario para crear la Clave.
    """
        
    # Se llama a la función recursiva
    Lista_Errores = Aux_Creación_Clave(Clave)
    
    while (Lista_Errores):
        print("\n[ERROR]: La Clave no es válida. No cumple con los siguientes criterios:")
        for Error in Lista_Errores:
            print(f"   -> {Error}")
        print("\n[Por favor, intente nuevamente.]\n")
        Clave = str(input("Ingrese su Clave: "))
        Lista_Errores = Aux_Creación_Clave(Clave)

    if not (Lista_Errores):
        print("\n✅ ¡Clave creada exitosamente! Cumple con todos los parámetros de seguridad.")

    CedulaCodificada = Cedula.ljust(8).encode('utf-8')
    NombreCodificado = Nombre.ljust(30).encode('utf-8')
    SexoCodificado = Sexo.ljust(1).encode('utf-8')
    FechaCodificada = Fecha.ljust(10).encode('utf-8')
    InicialCodificada = InicialEstado.ljust(3).encode('utf-8')
    EstadoCodificado = NombreEstado.ljust(20).encode('utf-8')
    ClaveCodificada = Clave.ljust(30).encode('utf-8')

    Registro_Binario = struct.pack(Formato_Registro, CedulaCodificada, NombreCodificado, SexoCodificado, FechaCodificada, InicialCodificada, EstadoCodificado, ClaveCodificada)
    JUGADORES.write(Registro_Binario)

    print("="*5 + f"El usuario [{Nombre}] ha sido registrado exitosamente." + "="*5)
    print("\n")

    JUGADORES.close()
    ESTADOS.close()

def main():
    Respuesta = "S"
    while (Respuesta == 'S' or Respuesta == 's'):
        Cedula = str(input("Ingrese su Cedula: "))
        print("\n")

        Nombre = str(input("Ingrese su Nombre de Usuario: "))
        print("\n")
        
        Sexo = str(input("Ingrese su Sexo: "))
        print("\n")
        
        Fecha = str(input("Ingrese su Fecha y Año de Nacimiento [dd-mm-aaaa]: "))
        print("\n")
        
        InicialEstado = str(input("Ingrese las inicialiales de su estado de nacimiento: "))
        print("\n")
        
        print("\n")
        print("=== CRITERIOS PARA LA CREACIÓN DE LA CLAVE ===")
        print("- Debe poseer entre 6 y 10 caracteres.")
        print("- Ser una combinación de letras en mayúscula y minúscula (sin acento y sin la letra Ñ o ñ), números y caracteres Especiales.")
        print("- Debe contener al menos uno de los siguientes caracteres Especiales: el asterisco (*), el igual (=), el porcentaje (%) o el guión bajo (_).")
        print("- La Clave NO debe contener más de 3 caracteres iguales de forma consecutiva.")
        print("="*5)
        print("\n")

        Clave = str(input("Ingrese su Clave: "))
        print("\n")

        Registro_Jugadores(Cedula, Nombre, Sexo, Fecha, InicialEstado, Clave)

        Respuesta = input("¿Desea registrar otro usuario? [S/N]: ")
        print("\n")

if __name__ == "__main__":
    main()
