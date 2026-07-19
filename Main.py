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

def Main (Matriz_1, Matriz_2, Titulo, Nombre, InicialEst):
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

    Titulo_ODS_1_img = pygame.image.load("Assets/Titulo-ODS-1.png").convert_alpha()
    Titulo_ODS_1_img = pygame.transform.scale(Titulo_ODS_1_img, (259, 59))

    Titulo_ODS_2_img = pygame.image.load("Assets/Titulo-ODS-2.png").convert_alpha()
    Titulo_ODS_2_img = pygame.transform.scale(Titulo_ODS_2_img, (259, 59))

    Titulo_ODS_3_img = pygame.image.load("Assets/Titulo-ODS-3.png").convert_alpha()
    Titulo_ODS_3_img = pygame.transform.scale(Titulo_ODS_3_img, (259, 59))
    
    Titulo_ODS_4_img = pygame.image.load("Assets/Titulo-ODS-4.png").convert_alpha()
    Titulo_ODS_4_img = pygame.transform.scale(Titulo_ODS_4_img, (259, 59))

    Titulo_ODS_5_img = pygame.image.load("Assets/Titulo-ODS-5.png").convert_alpha()
    Titulo_ODS_5_img = pygame.transform.scale(Titulo_ODS_5_img, (259, 59))
    
    Titulo_ODS_6_img = pygame.image.load("Assets/Titulo-ODS-6.png").convert_alpha()
    Titulo_ODS_6_img = pygame.transform.scale(Titulo_ODS_6_img, (259, 59))

    Titulo_ODS_7_img = pygame.image.load("Assets/Titulo-ODS-7.png").convert_alpha()
    Titulo_ODS_7_img = pygame.transform.scale(Titulo_ODS_7_img, (259, 59))

    Titulo_ODS_8_img = pygame.image.load("Assets/Titulo-ODS-8.png").convert_alpha()
    Titulo_ODS_8_img = pygame.transform.scale(Titulo_ODS_8_img, (259, 59))

    Titulo_ODS_9_img = pygame.image.load("Assets/Titulo-ODS-9.png").convert_alpha()
    Titulo_ODS_9_img = pygame.transform.scale(Titulo_ODS_9_img, (259, 59))

    Titulo_ODS_10_img = pygame.image.load("Assets/Titulo-ODS-10.png").convert_alpha()
    Titulo_ODS_10_img = pygame.transform.scale(Titulo_ODS_10_img, (259, 59))

    Titulo_ODS_11_img = pygame.image.load("Assets/Titulo-ODS-11.png").convert_alpha()
    Titulo_ODS_11_img = pygame.transform.scale(Titulo_ODS_11_img, (259, 59))

    Titulo_ODS_12_img = pygame.image.load("Assets/Titulo-ODS-12.png").convert_alpha()
    Titulo_ODS_12_img = pygame.transform.scale(Titulo_ODS_12_img, (259, 59))

    Titulo_ODS_13_img = pygame.image.load("Assets/Titulo-ODS-13.png").convert_alpha()
    Titulo_ODS_13_img = pygame.transform.scale(Titulo_ODS_13_img, (259, 59))

    Titulo_ODS_14_img = pygame.image.load("Assets/Titulo-ODS-14.png").convert_alpha()
    Titulo_ODS_14_img = pygame.transform.scale(Titulo_ODS_14_img, (259, 59))

    Titulo_ODS_15_img = pygame.image.load("Assets/Titulo-ODS-15.png").convert_alpha()
    Titulo_ODS_15_img = pygame.transform.scale(Titulo_ODS_15_img, (259, 59))

    Titulo_ODS_16_img = pygame.image.load("Assets/Titulo-ODS-16.png").convert_alpha()
    Titulo_ODS_16_img = pygame.transform.scale(Titulo_ODS_16_img, (259, 59))

    Texto_Datos = Fuente.render(f"{Nombre} | [{InicialEst}]", True, "White")

    GANADOR_img = pygame.image.load("Assets/Cartel-GANADOR.png").convert_alpha()
    GANADOR_img = pygame.transform.scale(GANADOR_img, (376, 112))

    N = Matriz_1.shape[0]
    Marcas_1 = np.zeros((N, N), dtype = int)
    Marcas_2 = np.zeros((N, N), dtype = int)
    Bolillos_Sorteados = []

    Tarjeta_Ganadora_1 = False
    Tarjeta_Ganadora_2 = False
    Fin_del_Juego = False
    
    Corriendo = True
    while Corriendo:

        dt = reloj.tick(60) / 1000
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                Corriendo = False

            if (Seguir_img.Es_Presionado(event)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                if (len(Bolillos_Sorteados) < (N * N)) and (Fin_del_Juego == False):
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

                    Tarjeta_Ganadora_1 = True
                    Tarjeta_Ganadora_2 = True

                    for i in range(N):
                        for j in range(N):
                            if (Matriz_1[i, j] > 0) and (Marcas_1[i, j] == 0):
                                Tarjeta_Ganadora_1 = False
                            
                            if (Matriz_2[i, j] > 0) and (Marcas_2[i, j] == 0):
                                Tarjeta_Ganadora_2 = False
                    
                    if (Tarjeta_Ganadora_1) or (Tarjeta_Ganadora_2):
                        Fin_del_Juego = True

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
        
        if (Titulo == "A: Pobreza/Hambre"):
            Ventana.blit(Titulo_ODS_1_img, (210, 110))
            Ventana.blit(Titulo_ODS_2_img, (805, 110))

        elif (Titulo == "B: Salud/Educación"):
            Ventana.blit(Titulo_ODS_3_img, (210, 110))
            Ventana.blit(Titulo_ODS_4_img, (805, 110))
                    
        elif (Titulo == "C: Género/Agua"):
            Ventana.blit(Titulo_ODS_5_img, (210, 110))
            Ventana.blit(Titulo_ODS_6_img, (805, 110))
                        
        elif (Titulo == "D: Energía/Trabajo"):
            Ventana.blit(Titulo_ODS_7_img, (210, 110))
            Ventana.blit(Titulo_ODS_8_img, (805, 110))
                        
        elif (Titulo == "E: Industria/Desigualdad"):
            Ventana.blit(Titulo_ODS_9_img, (210, 110))
            Ventana.blit(Titulo_ODS_10_img, (805, 110))
                        
        elif (Titulo == "F: Ciudades/Producción"):
            Ventana.blit(Titulo_ODS_11_img, (210, 110))
            Ventana.blit(Titulo_ODS_12_img, (805, 110))
                        
        elif (Titulo == "G: Clima/Vida Submarina"):
            Ventana.blit(Titulo_ODS_13_img, (210, 110))
            Ventana.blit(Titulo_ODS_14_img, (805, 110))
                        
        elif (Titulo == "H: Ecosistemas/Paz"):
            Ventana.blit(Titulo_ODS_15_img, (210, 110))
            Ventana.blit(Titulo_ODS_16_img, (805, 110))

        Ventana.blit(Texto_Datos, (520, 50))

        if (Tarjeta_Ganadora_1):
            Ventana.blit(GANADOR_img, (157, 310))
        
        if (Tarjeta_Ganadora_2):
            Ventana.blit(GANADOR_img,(747, 310))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    Main()