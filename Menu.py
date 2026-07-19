import pygame, struct, sys, os, Registro_Jugadores, reto2, reto3, Main
from Config_Botones import Boton
from Config_Reg_Jugadores import Dato_Jugador

pygame.init()
Ventana = pygame.display.set_mode((1280,720), pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption("Tombola")
reloj = pygame.time.Clock()

Icono = pygame.image.load("Assets/Tombola-Icono.png")
pygame.display.set_icon(Icono)

Fondo_Menu_img = pygame.image.load("Assets/Fondo-Menu.png").convert()
Fondo_Menu_img = pygame.transform.scale(Fondo_Menu_img, (1280, 720))

Logo_Tombola = pygame.image.load("Assets/Tombola-Logo.png").convert_alpha()
Logo_Tombola = pygame.transform.scale(Logo_Tombola, (576, 275))

Logo_UCAB_Blanco = pygame.image.load("Assets/Logo-UCAB-Blanco.png").convert_alpha()
Logo_UCAB_Blanco = pygame.transform.scale(Logo_UCAB_Blanco, (412, 63))

INICIO_img = Boton("Assets/Boton-Inicio.png", (319, 99), (481, 280), "Assets/Sonido-Boton-Madera.mp3")

REGISTRO_img = Boton("Assets/Boton-Registro.png", (319, 99), (481, 389), "Assets/Sonido-Boton-Madera.mp3")

SALIR_img = Boton("Assets/Boton-Salir.png", (319, 99),(481, 498), "Assets/Sonido-Boton-Madera.mp3")

Fondo_Menu_Inicio_img = pygame.image.load("Assets/Fondo-Menu-Inicio.png").convert()
Fondo_Menu_Inicio_img = pygame.transform.scale(Fondo_Menu_Inicio_img, (1280, 720))

REGISTRO_DE_USUARIOS_img = Boton("Assets/Boton-Registro-de-Usuarios.png", (143, 149), (1111, 20), "Assets/Sonido-Boton-Click.mp3")

VOLVER_AL_MENU_img = Boton("Assets/Boton-Volver-al-Menu.png", (143,149), (20, 20), "Assets/Sonido-Boton-Click.mp3")

Fondo_Menu_Registro_img = pygame.image.load("Assets/Fondo-Menu-Registro.png").convert()
Fondo_Menu_Registro_img = pygame.transform.scale(Fondo_Menu_Registro_img, (1280, 720))

VOLVER_AL_INICIO_img = Boton("Assets/Boton-Volver-al-Inicio.png", (143,149), (20, 20), "Assets/Sonido-Boton-Click.mp3")

ACEPTAR_img = Boton("Assets/Boton-Aceptar.png", (131, 149), (1111, 20), "Assets/Sonido-Boton-Click.mp3")

Seleccion_1_img = Boton("Assets/Boton-Seleccion-1.png", (446, 262), (182, 140), "Assets/Sonido-Boton-Click.mp3")
Seleccion_2_img = Boton("Assets/Boton-Seleccion-2.png", (446, 262), (650, 140), "Assets/Sonido-Boton-Click.mp3")
Seleccion_3_img = Boton("Assets/Boton-Seleccion-3.png", (446, 262), (182, 422), "Assets/Sonido-Boton-Click.mp3")
Seleccion_4_img = Boton("Assets/Boton-Seleccion-4.png", (446, 262), (650, 422), "Assets/Sonido-Boton-Click.mp3")
Seleccion_5_img = Boton("Assets/Boton-Seleccion-5.png", (446, 262), (182, 704), "Assets/Sonido-Boton-Click.mp3")
Seleccion_6_img = Boton("Assets/Boton-Seleccion-6.png", (446, 262), (650, 704), "Assets/Sonido-Boton-Click.mp3")
Seleccion_7_img = Boton("Assets/Boton-Seleccion-7.png", (446, 262), (182, 986), "Assets/Sonido-Boton-Click.mp3")
Seleccion_8_img = Boton("Assets/Boton-Seleccion-8.png", (446, 262), (650, 986), "Assets/Sonido-Boton-Click.mp3")

Opciones_Seleccion = {
    "Par de tarjetas 1": Seleccion_1_img,
    "Par de tarjetas 2": Seleccion_2_img,
    "Par de tarjetas 3": Seleccion_3_img,
    "Par de tarjetas 4": Seleccion_4_img,
    "Par de tarjetas 5": Seleccion_5_img,
    "Par de tarjetas 6": Seleccion_6_img,
    "Par de tarjetas 7": Seleccion_7_img,
    "Par de tarjetas 8": Seleccion_8_img
}

Scroll_Y_Tarjetas = 0
Altura_Opciones = 1268

Fuente = pygame.font.Font("Assets/ElmsSans-Medium.ttf", 30)
Fuente_Negrita = pygame.font.Font("Assets/ElmsSans-ExtraBold.ttf", 30)
Fuente_Negrita_Pequeña = pygame.font.Font("Assets/ElmsSans-ExtraBold.ttf", 20)

Cedula_Input = Dato_Jugador("Cédula:", (311, 80), (310, 120), "Grey50", Fuente, Fuente_Negrita)
Nombre_Input = Dato_Jugador("Nombre:", (311, 80), (310, 300), "Grey50", Fuente, Fuente_Negrita)
Sexo_Input = Dato_Jugador("Sexo:", (311, 80), (310, 480), "Grey50", Fuente, Fuente_Negrita)
Fecha_Input = Dato_Jugador("Fecha de Nacimiento:", (311, 80), (650,120), "Grey50", Fuente, Fuente_Negrita)
Inicial_Input = Dato_Jugador("Inicial de Estado:", (311, 80), (650, 300), "Grey50", Fuente, Fuente_Negrita)
Clave_Input = Dato_Jugador("Clave:", (311, 80), (650, 480), "Grey50", Fuente, Fuente_Negrita)

Tamaño_Matriz = None

Tamaño_Matriz_Input = Dato_Jugador("", (75, 75), (1150, 80), "Grey25", Fuente, Fuente_Negrita_Pequeña)
Texto_Matriz_1 = Fuente_Negrita_Pequeña.render("Tamaño de", True, "Black")
Texto_Matriz_2 = Fuente_Negrita_Pequeña.render("su Tarjeta:", True, "Black")

ERROR_Matriz_1_TXT = Fuente_Negrita_Pequeña.render("[Debe ser impar]", True, "Red")
ERROR_Matriz_2_1_TXT = Fuente_Negrita_Pequeña.render("[Debe ser", True, "Red")
ERROR_Matriz_2_2_TXT = Fuente_Negrita_Pequeña.render("mayor a 5]", True, "Red")

ERROR_Matriz_1 = False
ERROR_Matriz_2 = False

Registrados = True
Posicion_Y = 55
Jugador_Elegido = {}

FR_Jugadores = '8s30s1s10s3s20s30s'
TR_JUGADORES = struct.calcsize(FR_Jugadores)
Archivo_Fisico = "JUGADORES.bin"
Lista_Jugadores = {}

if (os.path.isfile(Archivo_Fisico)) and (os.path.getsize(Archivo_Fisico) != 0):
    JUGADORES = open(Archivo_Fisico, 'rb')

    JUGADORES.seek(0)
    EOF = False
    while (EOF == False):
        Jugadores_Bytes = JUGADORES.read(TR_JUGADORES)

        if (Jugadores_Bytes):
            CedulaCodificada, NombreCodificado, SexoCodificado, FechaCodificada, InicialCodificada, EstadoCodificado,ClaveCodificada = struct.unpack(FR_Jugadores, Jugadores_Bytes)
            Cedula = CedulaCodificada.decode('utf-8').strip()
            Nombre = NombreCodificado.decode('utf-8').strip()
            Sexo = SexoCodificado.decode('utf-8').strip()
            FechaNacimiento = FechaCodificada.decode('utf-8').strip()
            Inicial = InicialCodificada.decode('utf-8').strip()
            Estado = EstadoCodificado.decode('utf-8').strip()
            Clave = ClaveCodificada.decode('utf-8').strip()

            Lista_Jugadores[Cedula] ={
                "Cedula": Cedula,
                "Nombre": Nombre,
                "Sexo": Sexo,
                "Fecha de Nacimiento": FechaNacimiento,
                "Inicial de Estado": Inicial,
                "Estado": Estado,
                "Clave": Clave,
            }
        else:
            EOF = True

    for Jugador in Lista_Jugadores.values():
        Texto_Registrados_1 = Fuente_Negrita.render(f"{Jugador['Cedula']} | {Jugador['Nombre']}", True, "Black")
        Texto_Registrados_2 = Fuente.render(f"Sexo: {Jugador['Sexo']} | Est. {Jugador['Estado']} [{Jugador['Inicial de Estado']}]", True, "Black")
        Posicion_RegJG_1 = Texto_Registrados_1.get_rect(center = (640, Posicion_Y))
        Posicion_RegJG_2 = Texto_Registrados_2.get_rect(center = (640, Posicion_Y + 35))

        Jugador_Elegido[Jugador['Cedula']] = {
            "Texto 1": Texto_Registrados_1,
            "Texto 2": Texto_Registrados_2,
            "Posicion 1": Posicion_RegJG_1,
            "Posicion 2": Posicion_RegJG_2,
            "Elegido": Jugador
        }

        Posicion_Y = Posicion_Y + 60
else:
    Registrados = False
    Texto_ERROR_1 = Fuente_Negrita.render("[No hay usuarios registrados]", True, "Black")
    Texto_ERROR_2 = Fuente.render("¡Registrate!", True, "Black")
    Posicion_ERROR_1 = Texto_ERROR_1.get_rect(center = (640, 360))
    Posicion_ERROR_2 = Texto_ERROR_2.get_rect(center = (640, 395))

Jugador_Seleccionado = None
Jugador_Nuevo = {}
Scroll_Y = 0
Velocidad_Scrolling = 30

if (len(Jugador_Elegido) > 0):
    Altura_Lista = len(Jugador_Elegido) * 60
else:
    Altura_Lista = 0

Limite_Ventana = 720

Escena_Menu = "Menu"
Escena_Inicio = "Inicio"
Escena_Registro = "Registro"
Escena_Registro_Usuarios = "Registro_Usuarios"
Escena_Confirmacion_Datos = "Confirmación_Datos"
Escena_Seleccion_Tarjetas = "Seleccion_Tarjetas"
Escena_Actual = Escena_Menu

Corriendo = True
while Corriendo:

    dt = reloj.tick(60) / 1000
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            Corriendo = False
    
        if (Escena_Actual == Escena_Menu):
            
            if (INICIO_img.Es_Presionado(event)):
                print("INICIO")
                Escena_Actual = Escena_Inicio

            if (REGISTRO_img.Es_Presionado(event)):
                print("REGISTRO")
                Escena_Actual = Escena_Registro

            if (SALIR_img.Es_Presionado(event)):
                Corriendo = False
        
        elif (Escena_Actual == Escena_Inicio):
            if (VOLVER_AL_MENU_img.Es_Presionado(event)):
                print("VOLVER AL MENU")
                Escena_Actual = Escena_Menu
            
            elif (REGISTRO_DE_USUARIOS_img.Es_Presionado(event)):
                print("REGISTRO DE USUARIOS")
                Escena_Actual = Escena_Registro_Usuarios

            if (Registrados == True):
                if (event.type == pygame.MOUSEWHEEL): 
                    if (Altura_Lista > Limite_Ventana):
                        Desplazamiento = event.y * Velocidad_Scrolling
                        Scroll_Y = Scroll_Y + Desplazamiento
                    
                        if (Scroll_Y < 0):
                            Scroll_Y = 0
                        
                        Limite = Altura_Lista - Limite_Ventana

                        if (Limite < 0):
                            Limite = 0

                        if (Scroll_Y < Limite):
                            Scroll_Y = Limite

                        for Seleccion in Jugador_Elegido.values():
                            Seleccion["Posicion 1"].y = Seleccion["Posicion 1"].y + Desplazamiento
                            Seleccion["Posicion 2"].y = Seleccion["Posicion 2"].y + Desplazamiento

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (event.button == 1):
                        for Seleccion in Jugador_Elegido.values():
                            if (Seleccion["Posicion 1"].collidepoint(event.pos)) or (Seleccion["Posicion 2"].collidepoint(event.pos)):
                                Jugador_Seleccionado = Seleccion["Elegido"]
                                Escena_Actual = Escena_Seleccion_Tarjetas
        
        elif (Escena_Actual == Escena_Registro_Usuarios):
            Cedula_Input.Escritura(event, "Grey50", "White", Fuente, Fuente_Negrita, 14)
            Nombre_Input.Escritura(event, "Grey50", "White", Fuente, Fuente_Negrita, 14)
            Sexo_Input.Escritura(event, "Grey50", "White", Fuente, Fuente_Negrita, 14)
            Fecha_Input.Escritura(event, "Grey50", "White", Fuente, Fuente_Negrita, 14)
            Inicial_Input.Escritura(event, "Grey50", "White", Fuente, Fuente_Negrita, 14)
            Clave_Input.Escritura(event, "Grey50", "White", Fuente, Fuente_Negrita, 14)

            if (VOLVER_AL_INICIO_img.Es_Presionado(event)):
                Escena_Actual = Escena_Inicio
            
            elif (ACEPTAR_img.Es_Presionado(event)):
                Cedula = Cedula_Input.Escrito
                Nombre = Nombre_Input.Escrito
                Sexo = Sexo_Input.Escrito
                FechaNacimiento = Fecha_Input.Escrito
                Inicial = Inicial_Input.Escrito
                Clave = Clave_Input.Escrito
                Estado = ""
                Registro_Jugadores.Registro_Jugadores(Cedula, Nombre, Sexo, FechaNacimiento, Inicial, Estado, Clave)
                
                Registrados = True
                Escena_Actual = Escena_Inicio

                Jugador_Nuevo = {
                    "Cedula": Cedula,
                    "Nombre": Nombre,
                    "Sexo": Sexo,
                    "Fecha de Nacimiento": FechaNacimiento,
                    "Inicial de Estado": Inicial,
                    "Estado": Estado,
                    "Clave": Clave,
                }

                Texto_Registrados_1 = Fuente_Negrita.render(f"{Jugador['Cedula']} | {Jugador['Nombre']}", True, "Black")
                Texto_Registrados_2 = Fuente.render(f"Sexo: {Jugador['Sexo']} | Est. {Jugador['Estado']} [{Jugador['Inicial de Estado']}]", True, "Black")
                Posicion_RegJG_1 = Texto_Registrados_1.get_rect(center = (640, Posicion_Y))
                Posicion_RegJG_2 = Texto_Registrados_2.get_rect(center = (640, Posicion_Y + 35))

                Lista_Jugadores[Cedula] = Jugador_Nuevo

                Jugador_Elegido[Cedula] = {
                    "Texto 1": Texto_Registrados_1,
                    "Texto 2": Texto_Registrados_2,
                    "Posicion 1": Posicion_RegJG_1,
                    "Posicion 2": Posicion_RegJG_2,
                    "Elegido": Jugador_Nuevo
                }

                Posicion_Y = Posicion_Y + 60

        elif (Escena_Actual == Escena_Seleccion_Tarjetas):
            if (VOLVER_AL_INICIO_img.Es_Presionado(event)):
                Escena_Actual = Escena_Inicio
            
            Tamaño_Matriz_Input.Escritura(event, "Grey25", "Black", Fuente, Fuente_Negrita, 2)

            if (event.type == pygame.MOUSEWHEEL): 
                if (Altura_Opciones > Limite_Ventana):
                    Limite = Altura_Opciones - Limite_Ventana
                    Desplazamiento = event.y * Velocidad_Scrolling
                
                    if (Scroll_Y_Tarjetas - Desplazamiento < 0):
                        Desplazamiento = Scroll_Y_Tarjetas
                        Scroll_Y_Tarjetas = 0
                    
                    elif (Scroll_Y_Tarjetas - Desplazamiento > Limite):
                        Desplazamiento = Scroll_Y_Tarjetas - Limite
                        Scroll_Y_Tarjetas = Limite

                    else:
                        Scroll_Y_Tarjetas = Scroll_Y_Tarjetas - Desplazamiento
                    
                    for Opcion in Opciones_Seleccion.values():
                        Opcion.Colision.y = Opcion.Colision.y + Desplazamiento

            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (event.button == 1):

                    ERROR_Matriz_1 = False
                    ERROR_Matriz_2 = False 
                        
                    if (Tamaño_Matriz == None) and not (Tamaño_Matriz_Input.Escrito):
                        Tamaño_Matriz = 5

                    elif (Tamaño_Matriz_Input.Escrito.isdigit()):
                        
                        Tamaño_Ingresado = int(Tamaño_Matriz_Input.Escrito)

                        if (Tamaño_Ingresado >= 5) and (Tamaño_Ingresado % 2 != 0):    
                            Tamaño_Matriz = Tamaño_Ingresado

                        else:
                            Tamaño_Matriz = None
                            
                            if (Tamaño_Ingresado % 2 == 0):
                                ERROR_Matriz_1 = True

                            if (Tamaño_Ingresado < 5):
                                ERROR_Matriz_2 = True

                        if (Tamaño_Matriz != None) and (ERROR_Matriz_1 == False) and (ERROR_Matriz_2 == False):
                            Tamaño_Matriz = Tamaño_Ingresado
                            Diccionario_ODS = reto2.Seleccion_ODS_Dict(Tamaño_Matriz)

                            for Llave, Opcion in Opciones_Seleccion.items():
                                if Opcion.Es_Presionado(event):
                                    ODS_Seleccion = Llave[-1]

                                    if (ODS_Seleccion in Diccionario_ODS):
                                        Matriz_1, Matriz_2, Titulo = Diccionario_ODS[ODS_Seleccion]
                                        print(f"Seleccionado: {Titulo}")

                                        Matriz_1_Llenada, _ = reto3.Llenado_Tarjetas(Matriz_1, Tamaño_Matriz)
                                        Matriz_2_Llenada, _ = reto3.Llenado_Tarjetas(Matriz_2, Tamaño_Matriz)
                                        
                                        Nombre = Jugador_Seleccionado["Nombre"]
                                        InicialEst = Jugador_Seleccionado["Inicial de Estado"]
                                        
                                        Main.Main(Matriz_1_Llenada, Matriz_2_Llenada, Titulo, Nombre, InicialEst)

        elif (Escena_Actual == Escena_Registro):
            if (VOLVER_AL_MENU_img.Es_Presionado(event)):
                print("VOLVER AL MENU")
                Escena_Actual = Escena_Menu

    if (Escena_Actual == Escena_Menu):

        Ventana.blit(Fondo_Menu_img, (0, 0))
        Ventana.blit(Logo_Tombola, (352, 20))
        INICIO_img.Dibujo(Ventana)
        REGISTRO_img.Dibujo(Ventana)
        SALIR_img.Dibujo(Ventana)
        Ventana.blit(Logo_UCAB_Blanco, (434, 627))

    elif (Escena_Actual == Escena_Inicio):
        Ventana.blit(Fondo_Menu_Inicio_img, (0, 0))

        VOLVER_AL_MENU_img.Dibujo(Ventana)
        REGISTRO_DE_USUARIOS_img.Dibujo(Ventana)
        if (Registrados == True):
            for Seleccion in Jugador_Elegido.values():
                Ventana.blit(Seleccion["Texto 1"], Seleccion["Posicion 1"])
                Ventana.blit(Seleccion["Texto 2"], Seleccion["Posicion 2"])
        else:
            Ventana.blit(Texto_ERROR_1, Posicion_ERROR_1)
            Ventana.blit(Texto_ERROR_2, Posicion_ERROR_2)
    
    elif (Escena_Actual == Escena_Registro_Usuarios):
        Ventana.blit(Fondo_Menu_Registro_img, (0, 0))
        VOLVER_AL_INICIO_img.Dibujo(Ventana)
        ACEPTAR_img.Dibujo(Ventana)
        Cedula_Input.Dibujo(Ventana, 15, 18)
        Nombre_Input.Dibujo(Ventana, 15, 18)
        Sexo_Input.Dibujo(Ventana, 15, 18)
        Fecha_Input.Dibujo(Ventana, 15, 18)
        Inicial_Input.Dibujo(Ventana, 15, 18)
        Clave_Input.Dibujo(Ventana, 15, 18)
    
    elif (Escena_Actual == Escena_Seleccion_Tarjetas):
        Ventana.blit(Fondo_Menu_Inicio_img, (0, 0))
        VOLVER_AL_INICIO_img.Dibujo(Ventana)
        
        for Opcion in Opciones_Seleccion.values():
            Opcion.Dibujo(Ventana)
        
        Ventana.blit(Texto_Matriz_1, (1135, 30))
        Ventana.blit(Texto_Matriz_2, (1135, 50))

        if (ERROR_Matriz_1 == True) and (ERROR_Matriz_2 == True):
            Ventana.blit(ERROR_Matriz_1_TXT, (1100, 160))
            Ventana.blit(ERROR_Matriz_2_1_TXT, (1135, 180))
            Ventana.blit(ERROR_Matriz_2_2_TXT, (1135, 200))

        elif (ERROR_Matriz_1 == True) and (ERROR_Matriz_2 != True):
            Ventana.blit(ERROR_Matriz_1_TXT, (1100, 160))
        
        elif (ERROR_Matriz_1 != True) and (ERROR_Matriz_2 == True):
            Ventana.blit(ERROR_Matriz_2_1_TXT, (1135, 160))
            Ventana.blit(ERROR_Matriz_2_2_TXT, (1135, 180))

        Tamaño_Matriz_Input.Dibujo(Ventana, 25, 18)

    elif (Escena_Actual == Escena_Registro):
        Ventana.blit(Fondo_Menu_Inicio_img, (0, 0))
        VOLVER_AL_MENU_img.Dibujo(Ventana)

    pygame.display.flip()

pygame.quit()
sys.exit()