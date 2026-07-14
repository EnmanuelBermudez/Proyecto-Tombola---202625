import pygame, struct, sys, os, Registro_Jugadores, reto2, reto3
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
Fondo_Menu_Inicio_img = pygame.transform.scale(Fondo_Menu_Inicio_img, (1280,720))

REGISTRO_DE_USUARIOS_img = Boton("Assets/Boton-Registro-de-Usuarios.png", (143, 149), (1111, 20), "Assets/Sonido-Boton-Click.mp3")

VOLVER_AL_MENU_img = Boton("Assets/Boton-Volver-al-Menu.png", (143,149), (20, 20), "Assets/Sonido-Boton-Click.mp3")

Fondo_Menu_Registro_img = pygame.image.load("Assets/Fondo-Menu-Registro.png").convert()
Fondo_Menu_Registro_img = pygame.transform.scale(Fondo_Menu_Registro_img, (1280, 720))

VOLVER_AL_INICIO_img = Boton("Assets/Boton-Volver-al-INICIO.png", (143,149), (20, 20), "Assets/Sonido-Boton-Click.mp3")

ACEPTAR_img = Boton("Assets/Boton-Aceptar.png", (143, 149), (1111, 20), "Assets/Sonido-Boton-Click.mp3")

Fuente = pygame.font.Font("Assets/ElmsSans-Medium.ttf", 30)
Fuente_Negrita = pygame.font.Font("Assets/ElmsSans-ExtraBold.ttf", 30)

Cedula_Input = Dato_Jugador("Cédula:", (311, 80), (310, 120), Fuente, Fuente_Negrita)
Nombre_Input = Dato_Jugador("Nombre:", (311, 80), (310, 300), Fuente, Fuente_Negrita)
Sexo_Input = Dato_Jugador("Sexo:", (311, 80), (310, 480), Fuente, Fuente_Negrita)
Fecha_Input = Dato_Jugador("Fecha de Nacimiento:", (311, 80), (650,120), Fuente, Fuente_Negrita)
Inicial_Input = Dato_Jugador("Inicial de Estado:", (311, 80), (650, 300), Fuente, Fuente_Negrita)
Clave_Input = Dato_Jugador("Clave:", (311, 80), (650, 480), Fuente, Fuente_Negrita)

Escena_Menu = "Menu"
Escena_Inicio = "Inicio"
Escena_Registro = "Registro"
Escena_Registro_Usuarios = "Registro_Usuarios"
Escena_Seleccion_Tarjetas = "Seleccion_Tarjetas"
Escena_Tombola = "Tombola"
Escena_Actual = Escena_Menu

Registrados = True
Posicion_Y = 55
Jugador_Elegido = []

FR_Jugadores = '8s30s1s10s3s20s30s'
TR_JUGADORES = struct.calcsize(FR_Jugadores)
Archivo_Fisico = "JUGADORES.bin"
Lista_Jugadores = []

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

            Lista_Jugadores.append({
                "Cedula": Cedula,
                "Nombre": Nombre,
                "Sexo": Sexo,
                "Fecha de Nacimiento": FechaNacimiento,
                "Inicial de Estado": Inicial,
                "Estado": Estado,
                "Clave": Clave,
            })        
        else:
            EOF = True

    for Jugador in Lista_Jugadores:
        Texto_Registrados_1 = Fuente_Negrita.render(f"{Jugador['Cedula']} | {Jugador['Nombre']}", True, "Black")
        Texto_Registrados_2 = Fuente.render(f"Sexo: {Jugador['Sexo']} | Est. {Jugador['Estado']} [{Jugador['Inicial de Estado']}]", True, "Black")
        Posicion_RegJG_1 = Texto_Registrados_1.get_rect(center = (640, Posicion_Y))
        Posicion_RegJG_2 = Texto_Registrados_2.get_rect(center = (640, Posicion_Y + 35))

        Jugador_Elegido.append({
            "Texto 1": Texto_Registrados_1,
            "Texto 2": Texto_Registrados_2,
            "Posicion 1": Posicion_RegJG_1,
            "Posicion 2": Posicion_RegJG_2,
            "Elegido": Jugador
        })

        Posicion_Y = Posicion_Y + 60
else:
    Registrados = False
    Texto_ERROR_1 = Fuente_Negrita.render("[No hay usuarios registrados]", True, "Black")
    Texto_ERROR_2 = Fuente.render("¡Registrate!", True, "Black")
    Posicion_ERROR_1 = Texto_ERROR_1.get_rect(center = (640, 360))
    Posicion_ERROR_2 = Texto_ERROR_2.get_rect(center = (640, 395))

Jugador_Seleccionado = None
Jugador_Nuevo = []
Scroll_Y = 0
Velocidad_Scrolling = 30

if (len(Jugador_Elegido) > 0):
    Altura_Lista = len(Jugador_Elegido) * 60
else:
    Altura_Lista = 0

Limite_Ventana = 720

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

                        for Seleccion in Jugador_Elegido:
                            Seleccion["Posicion 1"].y = Seleccion["Posicion 1"].y + Desplazamiento
                            Seleccion["Posicion 2"].y = Seleccion["Posicion 2"].y + Desplazamiento

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (event.button == 1):
                        for Seleccion in Jugador_Elegido:
                            if (Seleccion["Posicion 1"].collidepoint(event.pos)) or (Seleccion["Posicion 2"].collidepoint(event.pos)):
                                Jugador_Seleccionado = Seleccion["Elegido"]
                                Escena_Actual = Escena_Seleccion_Tarjetas
        
        elif (Escena_Actual == Escena_Registro_Usuarios):
            Cedula_Input.Escritura(event, Fuente, Fuente_Negrita)
            Nombre_Input.Escritura(event, Fuente, Fuente_Negrita)
            Sexo_Input.Escritura(event, Fuente, Fuente_Negrita)
            Fecha_Input.Escritura(event, Fuente, Fuente_Negrita)
            Inicial_Input.Escritura(event, Fuente, Fuente_Negrita)
            Clave_Input.Escritura(event, Fuente, Fuente_Negrita)

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

                Texto_Registrados_1 = Fuente_Negrita.render(f"{Jugador['Cedula']} | {Jugador['Nombre']}", True, "Black")
                Texto_Registrados_2 = Fuente.render(f"Sexo: {Jugador['Sexo']} | Est. {Jugador['Estado']} [{Jugador['Inicial de Estado']}]", True, "Black")
                Posicion_RegJG_1 = Texto_Registrados_1.get_rect(center = (640, Posicion_Y))
                Posicion_RegJG_2 = Texto_Registrados_2.get_rect(center = (640, Posicion_Y + 35))

                Jugador_Nuevo = {
                    "Cedula": Cedula,
                    "Nombre": Nombre,
                    "Sexo": Sexo,
                    "Fecha de Nacimiento": FechaNacimiento,
                    "Inicial de Estado": Inicial,
                    "Estado": Estado,
                    "Clave": Clave,
                }

                Lista_Jugadores.append(Jugador_Nuevo)

                Jugador_Elegido.append({
                    "Texto 1": Texto_Registrados_1,
                    "Texto 2": Texto_Registrados_2,
                    "Posicion 1": Posicion_RegJG_1,
                    "Posicion 2": Posicion_RegJG_2,
                    "Elegido": Jugador_Nuevo
                })

                Posicion_Y = Posicion_Y + 60


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
            for Seleccion in Jugador_Elegido:
                Ventana.blit(Seleccion["Texto 1"], Seleccion["Posicion 1"])
                Ventana.blit(Seleccion["Texto 2"], Seleccion["Posicion 2"])
        else:
            Ventana.blit(Texto_ERROR_1, Posicion_ERROR_1)
            Ventana.blit(Texto_ERROR_2, Posicion_ERROR_2)
    
    elif (Escena_Actual == Escena_Registro_Usuarios):
        Ventana.blit(Fondo_Menu_Registro_img, (0, 0))
        VOLVER_AL_INICIO_img.Dibujo(Ventana)
        ACEPTAR_img.Dibujo(Ventana)
        Cedula_Input.Dibujo(Ventana)
        Nombre_Input.Dibujo(Ventana)
        Sexo_Input.Dibujo(Ventana)
        Fecha_Input.Dibujo(Ventana)
        Inicial_Input.Dibujo(Ventana)
        Clave_Input.Dibujo(Ventana)

    elif (Escena_Actual == Escena_Registro):
        Ventana.blit(Fondo_Menu_Inicio_img, (0, 0))
        VOLVER_AL_MENU_img.Dibujo(Ventana)

    pygame.display.flip()

pygame.quit()
sys.exit()