import pygame, struct, random, sys, os, reto2, reto3, Main
from Config_Botones import Boton
import numpy as np

def Dibujar_Tarjeta (Ventana, Matriz, Matriz_Marcas, Marca_img, Fuente, Tamaño_Celda, Posicion_X, Posicion_Y):
    Filas, Columnas = Matriz.shape
    Alto_Matriz = Filas * Tamaño_Celda
    Ancho_Matriz = Columnas * Tamaño_Celda
    Colision_Marca = None

    for i in range(0, Filas):
        for j in range(0, Columnas):
            Valor = Matriz[i, j]

            Eje_X = Posicion_X + (j * Tamaño_Celda)
            Eje_Y = Posicion_Y + (i * Tamaño_Celda)

            Colision_Celda = pygame.Rect(Eje_X, Eje_Y, Tamaño_Celda, Tamaño_Celda)

            if (Valor == 0):
                pygame.draw.rect(Ventana, "White", Colision_Celda)
            else:
                pygame.draw.rect(Ventana, "Green3", Colision_Celda)
            
            pygame.draw.rect(Ventana, "Black", Colision_Celda, 2)
            
            if (Valor != 0):
                Texto = Fuente.render(str(Valor), True, "Black")
                Colision_Texto = Texto.get_rect(center = Colision_Celda.center)
                Ventana.blit(Texto, Colision_Texto)
            
            if (Matriz_Marcas[i, j] == 1):
                Colision_Marca = Marca_img.get_rect(center = Colision_Celda.center)
                Ventana.blit(Marca_img, Colision_Marca)

def Main (Matriz_1, Matriz_2):
    pygame.init()
    Ventana = pygame.display.set_mode((1280,720), pygame.RESIZABLE | pygame.SCALED)
    pygame.display.set_caption("Tombola")
    reloj = pygame.time.Clock()

    Icono = pygame.image.load("Assets/Tombola-Icono.png")
    pygame.display.set_icon(Icono)

    Fondo_Juego_img = pygame.image.load("Assets/Fondo-Menu.png").convert()
    Fondo_Juego_img = pygame.transform.scale(Fondo_Juego_img, (1280, 720))

    Seguir_img = Boton("Assets/Boton-Seguir.png", (141, 141), (570, 290), "Assets/Sonido-Boton-Madera.mp3")

    Tamaño_Celda = 70

    Marca_img = pygame.image.load("Assets/Marca-Estrella.png").convert_alpha()
    Marca_img = pygame.transform.scale(Marca_img, (Tamaño_Celda, Tamaño_Celda))

    Texto_Num_Sorteados = ""

    Fuente = pygame.font.Font("Assets/ElmsSans-Medium.ttf", 30)
    Fuente_Negrita = pygame.font.Font("Assets/ElmsSans-ExtraBold.ttf", 30)

    N = Matriz_1.shape[0]
    Marcas_1 = np.zeros((N, N), dtype = int)
    Marcas_2 = np.zeros((N, N), dtype = int)
    Bolillos_Sorteados = []
    
    Corriendo = True
    while Corriendo:

        dt = reloj.tick(60) / 1000
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                Corriendo = False

            if (Seguir_img.Es_Presionado(event)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                if (len(Bolillos_Sorteados) < (N * N)):
                    Encontrado = False
                    Bolillo = 0

                    while not Encontrado:
                        Bolillo = random.randint(1, N * N)
                        ya_salio = False
                        for B in Bolillos_Sorteados:
                            if B == Bolillo: 
                                ya_salio = True
                        if not ya_salio:
                            Encontrado = True

                    Bolillos_Sorteados.append(Bolillo)
                    print(f"Salió el número {Bolillo}")

                    for i in range(N):
                        for j in range(N):
                            if (Matriz_1[i, j] == Bolillo):
                                Marcas_1[i, j] = 1

                            if (Matriz_2[i, j] == Bolillo):
                                Marcas_2[i, j] = 1

        Texto_Num_Sorteados = ""
        
        for B in Bolillos_Sorteados:
            Texto_Num_Sorteados = Texto_Num_Sorteados + str(B) + " "
        
        Render_Num_Sorteados = Fuente_Negrita.render (Texto_Num_Sorteados, True, "White")
        Colision_Num_Sorteados = Render_Num_Sorteados.get_rect(center = (640, 20))

        Ventana.blit(Fondo_Juego_img, (0, 0))
        Seguir_img.Dibujo(Ventana)
        Dibujar_Tarjeta(Ventana, Matriz_1, Marcas_1, Marca_img, Fuente, Tamaño_Celda, 170, 190)
        Dibujar_Tarjeta(Ventana, Matriz_2, Marcas_2, Marca_img, Fuente, Tamaño_Celda, 760, 190)
        Ventana.blit(Render_Num_Sorteados, Colision_Num_Sorteados)
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    Main()