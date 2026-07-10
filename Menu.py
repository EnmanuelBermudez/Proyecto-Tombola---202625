import pygame, sys, Registro_Jugadores, reto2, reto3
from Config_Botones import Boton

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

Registro_de_Usuario_img = pygame.image.load("Assets/Boton-Registro-de-Usuarios.png").convert_alpha()
Volver_al_Menu_img = pygame.image.load("Assets/Boton-Volver-al-Menu.png")

def main_menu():
    Corriendo = True
    while Corriendo:
        dt = reloj.tick(60) / 1000
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                Corriendo = False
    
        Ventana.blit(Fondo_Menu_img, (0, 0))
        Ventana.blit(Logo_Tombola, (352, 20))
        INICIO_img.draw(Ventana)
        REGISTRO_img.draw(Ventana)
        SALIR_img.draw(Ventana)
        Ventana.blit(Logo_UCAB_Blanco, (434, 627))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if (__name__ == "__main__"):
    main_menu()