import os
import struct
import numpy as np

# CONFIGURACIÓN BINARIA 
# Formato: Cedula(8), Nombre(30), Sexo(1), Fecha(10), Inicial(3), Estado(20), Clave(30)
FORMATO_JUGADOR = '8s30s1s10s3s20s30s'
TAMANO_REGISTRO = struct.calcsize(FORMATO_JUGADOR)

# MÓDULO DE CREACIÓN Y FORMATO 

def crear_matriz(n):
    return np.zeros((n, n), dtype=int)

def imprimir_tarjetas_formateadas(mat_p, mat_c, titulo_ods, nombre_jugador):
    n = mat_p.shape[0]
    print("\n" + "="*50)
    print(f"JUGADOR: {nombre_jugador}")
    print(f"PATRÓN ODS: {titulo_ods}")
    print("="*50)
    # Encabezado: Figura a la izquierda, Estructura a la derecha
    print(f"{'CARTÓN BINGO':<25} | {'ESTRUCTURA (RETO 2)':<25}")
    
    for i in range(n):
        f_p = ""; f_c = ""
        for j in range(n):
            v_p = str(mat_p[i, j]) if mat_p[i, j] != 0 else "·"
            v_c = str(mat_c[i, j]) if mat_c[i, j] != 0 else " "
            f_p += f"| {v_p:^3} "
            f_c += f"| {v_c:^3} "
        print(f"{f_p}|    {f_c}|")
    print("="*50)

# FUNCIONES DE PATRONES (A hasta H) 

def generar_A1(n):
    m = crear_matriz(n); c = 1
    for i in range(n-1, -1, -1):
        if i >= n // 2:
            for j in range(i, n-2-i, -1): m[i, j] = c; c += 1
        else:
            for j in range(n-1-i, i-1, -1): m[i, j] = c; c += 1
    return m

def generar_A2(n):
    m = crear_matriz(n); c = 1
    for j in range(n-1, -1, -1):
        if j >= n // 2:
            for i in range(j, n-2-j, -1): m[i, j] = c; c += 1
        else:
            for i in range(n-1-j, j-1, -1): m[i, j] = c; c += 1
    return m

def generar_B1(n):
    m = crear_matriz(n); c = 1
    for i in range(n):
        if i <= n // 2:
            for j in range(i + 1): m[i, j] = c; c += 1
            for j in range(n-1-i, n): m[i, j] = c; c += 1
        else:
            for j in range(n - i): m[i, j] = c; c += 1
            for j in range(i, n): m[i, j] = c; c += 1
    return m

def generar_B2(n):
    m = crear_matriz(n); c = 1
    for j in range(n):
        if j <= n // 2:
            for i in range(j + 1): m[i, j] = c; c += 1
            for i in range(n-1-j, n): m[i, j] = c; c += 1
        else:
            for i in range(n - j): m[i, j] = c; c += 1
            for i in range(j, n): m[i, j] = c; c += 1
    return m

def generar_C1(n):
    m = crear_matriz(n); c = 1
    for i in range(n-1, -1, -1):
        dist = abs(i - (n // 2))
        for j in range(n-1-dist, dist-1, -1): m[i, j] = c; c += 1
    return m

def generar_C2(n):
    m = crear_matriz(n); c = 1
    for j in range(n-1, -1, -1):
        dist = abs(j - (n // 2))
        for i in range(n-1-dist, dist-1, -1): m[i, j] = c; c += 1
    return m

def generar_D1(n):
    m = crear_matriz(n); c = 1
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n-1 or j == 0 or j == n-1) and (i != n//2 and j != n//2):
                m[i, j] = c; c += 1
    return m

def generar_D2(n):
    m = crear_matriz(n); c = 1
    for j in range(n):
        for i in range(n):
            if (i == 0 or i == n-1 or j == 0 or j == n-1) and (i != n//2 and j != n//2):
                m[i, j] = c; c += 1
    return m

def generar_E1(n):
    m = crear_matriz(n); c = 1
    anillos = (n // 2) + 1
    for k in range(anillos):
        for j in range(k, n-k):
            if (k % 2) == (j % 2) and m[k, j] == 0: m[k, j] = c; c += 1
        for i in range(k+1, n-k):
            if (i % 2) == ((n-1-k) % 2) and m[i, n-1-k] == 0: m[i, n-1-k] = c; c += 1
        for j in range(n-2-k, k-1, -1):
            if ((n-1-k) % 2) == (j % 2) and m[n-1-k, j] == 0: m[n-1-k, j] = c; c += 1
        for i in range(n-2-k, k, -1):
            if (i % 2) == (k % 2) and m[i, k] == 0: m[i, k] = c; c += 1
    return m

def generar_E2(n):
    m = crear_matriz(n); c = 1
    anillos = (n // 2) + 1
    for k in range(anillos):
        for i in range(k, n-k):
            if (i % 2) == (k % 2) and m[i, k] == 0: m[i, k] = c; c += 1
        for j in range(k+1, n-k):
            if ((n-1-k) % 2) == (j % 2) and m[n-1-k, j] == 0: m[n-1-k, j] = c; c += 1
        for i in range(n-2-k, k-1, -1):
            if (i % 2) == ((n-1-k) % 2) and m[i, n-1-k] == 0: m[i, n-1-k] = c; c += 1
        for j in range(n-2-k, k, -1):
            if (k % 2) == (j % 2) and m[k, j] == 0: m[k, j] = c; c += 1
    return m

def generar_F1(n):
    m = crear_matriz(n); c = 1
    for s in range(0, 2*n - 1, 2):
        for i in range(min(s, n-1), max(-1, s-n), -1):
            m[i, s-i] = c; c += 1
    return m

def generar_F2(n):
    m = crear_matriz(n); c = 1
    for d in range(n-1, -n, -2):
        for i in range(max(0, d), min(n, n+d)):
            m[i, i-d] = c; c += 1
    return m

def generar_G1(n):
    m = crear_matriz(n); c = 1
    for j in range(n-1, -1, -1): m[n-1, j] = c; c += 1
    for i in range(n-2, 0, -1): m[i, n-1-i] = c; c += 1
    for j in range(n-1, -1, -1): m[0, j] = c; c += 1
    return m

def generar_G2(n):
    m = crear_matriz(n); c = 1
    for i in range(n-1, -1, -1): m[i, n-1] = c; c += 1
    for i in range(1, n-1): m[i, n-1-i] = c; c += 1
    for i in range(n-1, -1, -1): m[i, 0] = c; c += 1
    return m

def generar_H1(n):
    m = crear_matriz(n); c = 1
    for i in range(n-1, -1, -1):
        if i != n // 2: m[i, n-1-i] = c; c += 1
    for i in range(n-1, -1, -1):
        if i != n // 2: m[i, i] = c; c += 1
    return m

def generar_H2(n):
    m = crear_matriz(n); c = 1
    for i in range(n-1, -1, -1):
        if i != n // 2: m[i, i] = c; c += 1
    for i in range(n-1, -1, -1):
        if i != n // 2: m[i, n-1-i] = c; c += 1
    return m

# FLUJO PRINCIPAL RETO 2 
def Seleccion_ODS_Dict(n):
    return {
        "1": (generar_A1(n), generar_A2(n), "A: Pobreza/Hambre"),
        "2": (generar_B1(n), generar_B2(n), "B: Salud/Educación"),
        "3": (generar_C1(n), generar_C2(n), "C: Género/Agua"),
        "4": (generar_D1(n), generar_D2(n), "D: Energía/Trabajo"),
        "5": (generar_E1(n), generar_E2(n), "E: Industria/Desigualdad"),
        "6": (generar_F1(n), generar_F2(n), "F: Ciudades/Producción"),
        "7": (generar_G1(n), generar_G2(n), "G: Clima/Vida Submarina"),
        "8": (generar_H1(n), generar_H2(n), "H: Ecosistemas/Paz")
    }

def ejecutar_reto_2():
    jugador_encontrado = False
    nombre = ""
    cedula_input = input("Ingrese cédula: ").strip()
    clave_input = input("Ingrese clave: ").strip()
    
    # Autenticación binaria estructurada 
    if os.path.exists("JUGADORES.bin"):
        with open("JUGADORES.bin", "rb") as ar:
            # Lectura inicial 
            bytes_leidos = ar.read(TAMANO_REGISTRO)
            
            # El bucle se detiene si se acaba el archivo o si encontramos al jugador
            while bytes_leidos and not jugador_encontrado:
                reg = struct.unpack(FORMATO_JUGADOR, bytes_leidos)
                c_db = reg[0].decode('utf-8').strip()
                k_db = reg[6].decode('utf-8').strip()
                
                if c_db == cedula_input and k_db == clave_input:
                    jugador_encontrado = True
                    nombre = reg[1].decode('utf-8').strip()
                else:
                    # Solo leemos el siguiente registro si no hemos encontrado al jugador
                    bytes_leidos = ar.read(TAMANO_REGISTRO)

    if not jugador_encontrado:
        print("Acceso denegado. Verifique sus datos.")
        return

    # Validación de N 
    n = 0
    entrada_valida = False
    while not entrada_valida:
        try:
            n = int(input("Ingrese N (impar >= 5): "))
            if n >= 5 and n % 2 != 0:
                entrada_valida = True
        except ValueError:
            # Si hay un error, el bucle simplemente vuelve a evaluar la condición y repite
            pass
    
    print("\nSeleccione par de ODS (1-8):")
    print("1. A1/A2 | 2. B1/B2 | 3. C1/C2 | 4. D1/D2")
    print("5. E1/E2 | 6. F1/F2 | 7. G1/G2 | 8. H1/H2")
    op = input("> ")

    ods_dict = Seleccion_ODS_Dict(n)

    if op in ods_dict:
        m1, m2, tit = ods_dict[op]
        imprimir_tarjetas_formateadas(m1, m1, tit + " (1)", nombre)
        imprimir_tarjetas_formateadas(m2, m2, tit + " (2)", nombre)
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    ejecutar_reto_2()