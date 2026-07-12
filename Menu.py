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

VOLVER_AL_REGISTRO_img = Boton("Assets/Boton-Volver-al-Menu.png", (143,149), (20, 20), "Assets/Sonido-Boton-Click.mp3")

ACEPTAR_img = Boton("Assets/Boton-Registro-de-Usuarios.png", (143, 149), (1111, 20), "Assets/Sonido-Boton-Click.mp3")

Fuente = pygame.font.Font("Assets/ElmsSans-Medium.ttf", 30)
Fuente_Negrita = pygame.font.Font("Assets/ElmsSans-ExtraBold.ttf", 30)

Cedula_Input = Dato_Jugador("Cédula:", (311, 80), (360, 120), Fuente)

Escena_Menu = "Menu"
Escena_Inicio = "Inicio"
Escena_Registro = "Registro"
Escena_Registro_Usuarios = "Registro_Usuarios"
Escena_Actual = Escena_Menu

Registrados = True
Posicion_Y = 25
Jugador_Elegido = []

FR_Jugadores = '8s30s1s10s3s30s'
TR_JUGADORES = struct.calcsize(FR_Jugadores)
Archivo_Fisico = "JUGADORES.bin"
Lista_Jugadores = []

if os.path.isfile(Archivo_Fisico):
    JUGADORES = open(Archivo_Fisico, 'rb')

    JUGADORES.seek(0)
    EOF = False
    while (EOF == False):
        Jugadores_Bytes = JUGADORES.read(TR_JUGADORES)

        if (Jugadores_Bytes):
            CedulaCodificada, NombreCodificado, SexoCodificado, FechaCodificada, InicialCodificada, EstadoCodificado,ClaveCodificada = struct.calcsize(Jugadores_Bytes)
            Cedula = CedulaCodificada.decode('utf-8').strip()
            Nombre = NombreCodificado.decode('utf-8').strip()
            Sexo = SexoCodificado.decode('utf-8').strip()
            FechaNacimiento = FechaCodificada.decode('utf-8').strip
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
        Texto_Registrados_2 = Fuente.render(f"Sexo: {Jugador['Sexo']} | {Jugador['Inicial']}", True, "Black")
        Posicion_RegJG_1 = Texto_Registrados_1.get_rect(center = (0, Posicion_Y))
        Posicion_RegJG_2 = Texto_Registrados_2.get_rect(center = (0, Posicion_Y - 35))

        Jugador_Elegido.append({
            "Texto 1": Texto_Registrados_1,
            "Texto 2": Texto_Registrados_2,
            "Posicion 1": Posicion_RegJG_1,
            "Posicion 2": Posicion_RegJG_2,
            "Elegido": Jugador
        })

        Posicion_Y = Posicion_Y - 60
else:
    Registrados = False
    Texto_ERROR_1 = Fuente_Negrita.render("[No hay usuarios registrados]", True, "Black")
    Texto_ERROR_2 = Fuente.render("¡Registrate!", True, "Black")
    Posicion_ERROR_1 = Texto_ERROR_1.get_rect(center = (640, 360))
    Posicion_ERROR_2 = Texto_ERROR_2.get_rect(center = (640, 395))

Jugadores_Cas = []
Jugador_Seleccionado = None
Scroll_Y = 0
Velocidad_Scrolling = 30

if len(Jugador_Elegido) > 0:
    Altura_Lista = len(Jugador_Elegido) * (pygame.Surface.get_height(Texto_Registrados_1) + pygame.Surface.get_height(Texto_Registrados_2))
else:
    Altura_Lista = 0

limite_Pantalla = 720

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
                    Desplazamiento = event.y * Velocidad_Scrolling
                    Scroll_Y = Scroll_Y + Desplazamiento
                
                    if (Scroll_Y < 0):
                        Scroll_Y = 0
                    
                    Limite = Altura_Lista - limite_Pantalla

                    if (Limite < 0):
                        Limite = 0

                    if (Scroll_Y < Limite):
                        Scroll_Y = Limite

                if (event.type == pygame.MOUSEBUTTONDOWN):
                    if (event.button == 1):
                        for Seleccion in Jugador_Elegido:
                            Seleccion["Posicion 1"].y = Seleccion["Posicion 1"] + Desplazamiento
                            if (Seleccion["Posicion 1"].collidepoint(event.pos)) or (Seleccion["Posicion 2"].collidepoint(event.pos)):
                                Jugador_Seleccionado = Seleccion["Elegido"]
        
        elif (Escena_Actual == Escena_Registro_Usuarios):
                    
            if (ACEPTAR_img.Es_Presionado()):
                Cedula = Cedula_Input.Escritura(event, Fuente)

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
                if ((pygame.Surface.get_height(Texto_Registrados_1) + pygame.Surface.get_height(Texto_Registrados_2)) < Seleccion["Posicion 1"] < 720):
                    Ventana.blit = Seleccion["Texto 1"]
                    Ventana.blit = Seleccion["Texto 2"]
                    Ventana.blit = Seleccion["Posicion 1"]
                    Ventana.blit = Seleccion["Posicion 2"]
        else:
            Ventana.blit(Texto_ERROR_1, Posicion_ERROR_1)
            Ventana.blit(Texto_ERROR_2, Posicion_ERROR_2)
    
    elif (Escena_Actual == Escena_Registro_Usuarios):
        Ventana.blit(Fondo_Menu_Registro_img, (0, 0))
        VOLVER_AL_REGISTRO_img.Dibujo(Ventana)
        ACEPTAR_img.Dibujo(Ventana)
        Cedula_Input.Dibujo(Ventana)

    elif (Escena_Actual == Escena_Registro):
        Ventana.blit(Fondo_Menu_Inicio_img, (0, 0))
        VOLVER_AL_MENU_img.Dibujo(Ventana)

    pygame.display.flip()

pygame.quit()
sys.exit()