import os
import pickle
import numpy as np

# --- MÓDULO DE CREACIÓN Y FORMATO ---

def crear_matriz(n):
    return np.zeros((n, n), dtype=int)

def imprimir_tarjetas_formateadas(mat_p, mat_c, titulo_ods, nombre_jugador):
    n = mat_p.shape[0]
    print("\nJugador: " + nombre_jugador)
    print("=== " + titulo_ods + " ===")
    for i in range(n):
        f_p = ""; f_c = ""
        for j in range(n):
            v_p = str(mat_p[i, j]) if mat_p[i, j] != 0 else " "
            v_c = str(mat_c[i, j]) if mat_c[i, j] != 0 else " "
            f_p += f"| {v_p:^3} "; f_c += f"| {v_c:^3} "
        print(f_p + "|  " + f_c + "|")


# --- PATRONES A: Reloj de arena (Horizontal y Vertical) ---
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

# --- PATRONES B: Lazo / Corbatín (Horizontal y Vertical) ---
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

# --- PATRONES C: Rombos / Diamantes ---
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

# --- PATRONES D: Marcos perforados (Sin cruz central) ---
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

# --- PATRONES E: Espirales en tablero de ajedrez ---
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

# --- PATRONES F: Diagonales en tablero de ajedrez ---
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

# --- PATRONES G: Formas de Z y N ---
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

# --- PATRONES H: Cruz diagonal (excluyendo el centro) ---
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

# --- FLUJO PRINCIPAL ---

def ejecutar_reto_2():
    jugador_encontrado = False; nombre = ""
    cedula = input("Ingrese cédula: "); clave = input("Ingrese clave: ")
    
    if os.path.exists("JUGADORES.bin"):
        tam = os.path.getsize("JUGADORES.bin"); ar = open("JUGADORES.bin", "rb")
        while ar.tell() < tam and not jugador_encontrado:
            reg = pickle.load(ar)
            if str(reg[0]) == cedula and str(reg[5]) == clave:
                jugador_encontrado = True; nombre = reg[1]
        ar.close()

    if not jugador_encontrado: print("Acceso denegado."); return

    # Validación de N
    n = 0
    while n < 5 or n % 2 == 0:
        n = int(input("Ingrese N (impar >= 5): "))
    
    print("\nSeleccione par de ODS:")
    print("1. A1/A2: Fin Pobreza / Hambre Cero")
    print("2. B1/B2: Salud / Educación")
    print("3. C1/C2: Género / Agua Limpia")
    print("4. D1/D2: Energía / Trabajo")
    print("5. E1/E2: Industria / Desigualdades")
    print("6. F1/F2: Ciudades / Producción")
    print("7. G1/G2: Clima / Vida Submarina")
    print("8. H1/H2: Ecosistemas / Paz")
    
    op = input("> ")

    if op == "1": imprimir_tarjetas_formateadas(generar_A1(n), generar_A2(n), "A: Fin Pobreza / Hambre Cero", nombre)
    elif op == "2": imprimir_tarjetas_formateadas(generar_B1(n), generar_B2(n), "B: Salud / Educación", nombre)
    elif op == "3": imprimir_tarjetas_formateadas(generar_C1(n), generar_C2(n), "C: Género / Agua Limpia", nombre)
    elif op == "4": imprimir_tarjetas_formateadas(generar_D1(n), generar_D2(n), "D: Energía / Trabajo", nombre)
    elif op == "5": imprimir_tarjetas_formateadas(generar_E1(n), generar_E2(n), "E: Industria / Desigualdades", nombre)
    elif op == "6": imprimir_tarjetas_formateadas(generar_F1(n), generar_F2(n), "F: Ciudades / Producción", nombre)
    elif op == "7": imprimir_tarjetas_formateadas(generar_G1(n), generar_G2(n), "G: Clima / Vida Submarina", nombre)
    elif op == "8": imprimir_tarjetas_formateadas(generar_H1(n), generar_H2(n), "H: Ecosistemas / Paz", nombre)
    else: print("Opción inválida.")

if __name__ == "__main__":
    ejecutar_reto_2()