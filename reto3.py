import os
import struct
import random
import time
import datetime
import reto2

#  CONFIGURACIÓN DE ARCHIVOS 
FORMATO_JUGADOR = '8s30s1s10s3s20s30s'
TAMANO_JUGADOR = struct.calcsize(FORMATO_JUGADOR)

def guardar_juego_binario(cedula, fecha_hora, secuencia_carton, bolillos_sorteados):
    """
    Guarda el juego en JUEGOS.bin usando struct.
    Como las secuencias varían de tamaño, guardamos primero la cantidad de números.
    """
    archivo = "JUEGOS.bin"
    # Formato cabecera: Cedula(8), Fecha(20), Cantidad de num cartón, Cantidad bolillos
    formato_header = '8s20sII'
    
    cedula_bytes = cedula.ljust(8).encode('utf-8')
    fecha_bytes = fecha_hora.ljust(20).encode('utf-8')
    cant_carton = len(secuencia_carton)
    cant_bolillos = len(bolillos_sorteados)
    
    with open(archivo, "ab") as f:
        # Escribir cabecera
        header = struct.pack(formato_header, cedula_bytes, fecha_bytes, cant_carton, cant_bolillos)
        f.write(header)
        
        # Escribir los números del cartón uno por uno como enteros 
        for num in secuencia_carton:
            f.write(struct.pack('I', num))
            
        # Escribir los bolillos sorteados uno por uno como enteros 
        for bol in bolillos_sorteados:
            f.write(struct.pack('I', bol))

def Llenado_Tarjetas(mat_base, n):
    # 3. LLENADO DE TARJETA
    celdas_figura = 0
    for i in range(n):
        for j in range(n):
            if mat_base[i, j] > 0:
                celdas_figura += 1

    # Generar números aleatorios únicos para el cartón
    carton_numeros = []
    while len(carton_numeros) < celdas_figura:
        nuevo_num = random.randint(1, n*n)
        repetido = False
        for x in carton_numeros:
            if x == nuevo_num:
                repetido = True
        
        if not repetido:
            carton_numeros.append(nuevo_num)

    # Asignar los números al cartón según el orden 
    carton_final = reto2.crear_matriz(n)
    idx = 0
    for i in range(n):
        for j in range(n):
            if mat_base[i, j] > 0:
                carton_final[i, j] = carton_numeros[idx]
                idx = idx + 1

    return carton_final, carton_numeros

def ejecutar_reto_3():
    print("\n****************************************")
    print("      SISTEMA DE TÓMBOLA ODS")
    print("****************************************")
    
    # 1. AUTENTICACIÓN 
    cedula_ingresada = input("Ingrese Cédula: ")
    clave_ingresada = input("Ingrese Clave: ")
    
    jugador_encontrado = False
    nombre_jugador = ""
    siglas_estado = ""

    if os.path.exists("JUGADORES.bin"):
        with open("JUGADORES.bin", "rb") as f:
            # Lectura inicial 
            bytes_bloque = f.read(TAMANO_JUGADOR)
            
            while bytes_bloque and not jugador_encontrado:
                datos = struct.unpack(FORMATO_JUGADOR, bytes_bloque)
                # datos[0]=cedula, [1]=nombre, [4]=siglas, [6]=clave
                c_db = datos[0].decode('utf-8').strip()
                k_db = datos[6].decode('utf-8').strip()
                
                if c_db == cedula_ingresada and k_db == clave_ingresada:
                    jugador_encontrado = True
                    nombre_jugador = datos[1].decode('utf-8').strip()
                    siglas_estado = datos[4].decode('utf-8').strip()
                else:
                    # Solo leemos el siguiente registro si no hemos encontrado al jugador
                    bytes_bloque = f.read(TAMANO_JUGADOR)

    if not jugador_encontrado:
        print("ERROR: Credenciales inválidas.")
        return

    # 2. SELECCIÓN DE ODS
    n = 0
    while n < 5 or n % 2 == 0:
        try:
            n = int(input("Ingrese dimensión N (impar >= 5): "))
        except ValueError:
            pass

    print("\nEscriba el código de la tarjeta (A1, A2, B1, B2, etc.):")
    codigo = input("> ").upper()

    mat_base = None
    if codigo == "A1": mat_base = reto2.generar_A1(n)
    elif codigo == "A2": mat_base = reto2.generar_A2(n)
    elif codigo == "B1": mat_base = reto2.generar_B1(n)
    elif codigo == "B2": mat_base = reto2.generar_B2(n)
    elif codigo == "C1": mat_base = reto2.generar_C1(n)
    elif codigo == "C2": mat_base = reto2.generar_C2(n)
    elif codigo == "D1": mat_base = reto2.generar_D1(n)
    elif codigo == "D2": mat_base = reto2.generar_D2(n)
    elif codigo == "E1": mat_base = reto2.generar_E1(n)
    elif codigo == "E2": mat_base = reto2.generar_E2(n)
    elif codigo == "F1": mat_base = reto2.generar_F1(n)
    elif codigo == "F2": mat_base = reto2.generar_F2(n)
    elif codigo == "G1": mat_base = reto2.generar_G1(n)
    elif codigo == "G2": mat_base = reto2.generar_G2(n)
    elif codigo == "H1": mat_base = reto2.generar_H1(n)
    elif codigo == "H2": mat_base = reto2.generar_H2(n)
    
    if mat_base is None:
        print("Código no válido.")
        return

    carton_final, secuencia_para_archivo = Llenado_Tarjetas(mat_base, n)

    # Mostrar inicio
    print("\nJUGADOR: {} [{}] | TARJETA: {}".format(nombre_jugador, siglas_estado, codigo))
    reto2.imprimir_tarjetas_formateadas(carton_final, mat_base, "CARTÓN GENERADO", nombre_jugador)
    input("Presione ENTER para comenzar el sorteo...")

    # 4. EL JUEGO (TOMbola)
    marcado = reto2.crear_matriz(n)
    bolillos_sorteados = []
    terminado = False
    
    while not terminado and len(bolillos_sorteados) < (n*n):
        # Generar bolillo único aleatorio
        bolillo = random.randint(1, n*n)
        ya_salio = False
        for b in bolillos_sorteados:
            if b == bolillo: 
                ya_salio = True
            # Si el número NO ha salido, se agrega a la lista de bolillos sorteados
        if not ya_salio:
            bolillos_sorteados.append(bolillo)
            print("\nTurno {}: Salió el número {}".format(len(bolillos_sorteados), bolillo))
            time.sleep(0.3)

            # Marcar en el cartón
            for i in range(n):
                for j in range(n):
                    if carton_final[i, j] == bolillo:
                        marcado[i, j] = 1
                        print("--> ¡Número encontrado en tu tarjeta!")

            # Dibujar tablero con marcas
            for i in range(n):
                fila_str = ""
                for j in range(n):
                    if mat_base[i, j] == 0:
                        fila_str += "|     "
                    elif marcado[i, j] == 1:
                        fila_str += "| [X] " 
                    else:
                        fila_str += "| {:^3} ".format(carton_final[i, j])
                print(fila_str + "|")

            # Verificar victoria
            gano = True
            for i in range(n):
                for j in range(n):
                    if mat_base[i, j] > 0 and marcado[i, j] == 0:
                        gano = False
            
            if gano:
                terminado = True
                print("\n¡¡ GANADOR !!")
                # Sumar celdas ganadoras
                suma_final = 0
                for i in range(n):
                    for j in range(n):
                        if mat_base[i, j] > 0:
                            suma_final += carton_final[i, j]
                print("Suma total de la tarjeta: {}".format(suma_final))
                
                # Guardar en archivo
                ahora = datetime.datetime.now()
                fecha_str = ahora.strftime("%d/%m/%Y %H:%M")
                guardar_juego_binario(cedula_ingresada, fecha_str, secuencia_para_archivo, bolillos_sorteados)
                print("Juego guardado en JUEGOS.bin")
                
    return gano

    opcion = input("\n¿Desea jugar otra vez? (S/N): ")
    if opcion.upper() == "S":
        ejecutar_reto_3()

if __name__ == "__main__":
    ejecutar_reto_3()