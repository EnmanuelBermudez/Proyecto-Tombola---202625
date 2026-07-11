import pygame, struct, sys, os, Registro_Jugadores, reto2, reto3
from Config_Botones import Boton

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
            Inicial = InicialCodificada.decode('utf-8').strip()
            Estado = EstadoCodificado.decode('utf-8').strip()
            Clave = ClaveCodificada.decode('utf-8').strip()

            Lista_Jugadores.append({
                "Cedula": Cedula,
                "Nombre": Nombre,
                "Sexo": Sexo,
                "Inicial de Estado": Inicial,
                "Estado": Estado,
                "Clave": Clave,
            })        
        else:
            EOF = True

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

Fuente = pygame.font.Font("Assets/ElmsSans-Medium.ttf", 16)

Escena_Menu = "Menu"
Escena_Inicio = "Inicio"
Escena_Registro = "Registro"
Escena_Registro_Usuarios = "Registro_Usuarios"
Escena_Actual = Escena_Menu

Posicion_Y = 25

Jugador_Elegido = []

for Jugador in Lista_Jugadores:
    Texto_Registrados = f"{Jugador['Cedula']} | {Jugador['Nombre']} \n Sexo: {Jugador['Sexo']} | {Jugador['Inicial']}"

    Render_Registrados = font.render(Texto_Registrados, True, "Black")

    Colision_Jug = Render_Registrados.get_rect(center = (0, Posicion_Y))

    Jugador_Elegido.append({
        "Texto" : Texto_Registrados,
        "Colision":Colision_Jug,
        "Elegido": Jugador
    })

    Posicion_Y = Posicion_Y - 60

Jugadores_Cas = []

Corriendo = True
while Corriendo:

    Jugador_Seleccionado = None
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

            if (event.type == pygame.MOUSEBUTTONDOWN):
                for Seleccion in Jugador_Elegido:
                    if Seleccion["Colision"].collidepoint(event.pos):
                        Jugador_Seleccionado = Seleccion["Elegido"]
                
            VOLVER_AL_MENU_img.Dibujo(Ventana)
            REGISTRO_DE_USUARIOS_img.Dibujo(Ventana)

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
        Ventana.blit = Seleccion["Texto"]
        Ventana.blit = Seleccion["Colision"]

    elif (Escena_Actual == Escena_Registro):
        Ventana.blit(Fondo_Menu_Inicio_img, (0, 0))
        VOLVER_AL_MENU_img.Dibujo(Ventana)


    pygame.display.flip()

pygame.quit()
sys.exit()