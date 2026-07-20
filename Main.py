import pygame, struct, random, datetime, sys, os, Reto_2, Reto_3, Menu
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

def Main (Matriz_1, Matriz_2, Titulo, Nombre, InicialEst, Cedula):
    pygame.init()
    Ventana = pygame.display.set_mode((1280,720), pygame.RESIZABLE | pygame.SCALED)
    pygame.display.set_caption("Tombola")
    reloj = pygame.time.Clock()

    Icono = pygame.image.load("Assets/Tombola-Icono.png")
    pygame.display.set_icon(Icono)

    Fondo_Juego_img = pygame.image.load("Assets/Fondo-Juego.png").convert()
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

    Frase_ODS_1 = ""
    Frase_ODS_2 = ""

    Contador_Boton = 0

    N = Matriz_1.shape[0]
    Marcas_1 = np.zeros((N, N), dtype = int)
    Marcas_2 = np.zeros((N, N), dtype = int)
    Bolillos_Sorteados = []

    Tarjeta_Ganadora_1 = False
    Tarjeta_Ganadora_2 = False
    Fin_del_Juego = False

    Puntos_Acumulados = 0
    Guardar_Juego = False

    VOLVER_AL_MENU_img = Boton("Assets/Boton-Volver-al-Menu.png", (143,149), (20, 20), "Assets/Sonido-Boton-Click.mp3")
    
    Corriendo = True
    while Corriendo:

        dt = reloj.tick(60) / 1000
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                Corriendo = False

            if (Seguir_img.Es_Presionado(event)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                if (len(Bolillos_Sorteados) < (N * N)) and (Fin_del_Juego == False):
                    Contador_Boton = Contador_Boton + 1
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

                        if (Guardar_Juego == False):
                            Sorteados_Tarjeta = []
                            if (Tarjeta_Ganadora_1):
                                Ganadora_Juego  = Matriz_1

                            elif (Tarjeta_Ganadora_2):
                                Ganadora_Juego = Matriz_2

                        for i in range(N):
                            for j in range(N):
                                if (Ganadora_Juego[i, j] > 0):
                                    Puntos_Acumulados = Puntos_Acumulados + Ganadora_Juego[i, j]
                                    Sorteados_Tarjeta.append(Ganadora_Juego[i, j])

                        Puntos_Acumulados_TXT = Fuente_Negrita.render(f"[Puntos Acumulados: {Puntos_Acumulados}]", True, "Red")

                        Ahora = datetime.datetime.now()
                        Fecha_STR = Ahora.strftime("%d-%m-%Y %H:%M")
                        Reto_3.guardar_juego_binario(Cedula, Fecha_STR, Sorteados_Tarjeta, Bolillos_Sorteados)
                        
                        Guardar_Juego = True

        Texto_Num_Sorteados = ""
        
        for B in Bolillos_Sorteados:
            Texto_Num_Sorteados = Texto_Num_Sorteados + str(B) + " "
        
        Render_Num_Sorteados = Fuente_Negrita.render (Texto_Num_Sorteados, True, "White")
        Colision_Num_Sorteados = Render_Num_Sorteados.get_rect(center = (640, 20))

        if (VOLVER_AL_MENU_img.Es_Presionado(event)):
            Corriendo = False

        Ventana.blit(Fondo_Juego_img, (0, 0))
        Seguir_img.Dibujo(Ventana)
        Dibujar_Tarjeta(Ventana, Matriz_1, Marcas_1, Marca_img, Fuente, Tamaño_Celda, 170, 190)
        Dibujar_Tarjeta(Ventana, Matriz_2, Marcas_2, Marca_img, Fuente, Tamaño_Celda, 760, 190)
        Ventana.blit(Render_Num_Sorteados, Colision_Num_Sorteados)
        
        if (Titulo == "A: Pobreza/Hambre"):
            Ventana.blit(Titulo_ODS_1_img, (210, 110))
            Ventana.blit(Titulo_ODS_2_img, (805, 110))
            Frase_ODS_1 = "Que la dignidad reemplace a la escasez en cada rincón del mundo."
            Frase_ODS_2 = "Platos llenos y cosechas prósperas para nutrir a toda la humanidad."

        elif (Titulo == "B: Salud/Educación"):
            Ventana.blit(Titulo_ODS_3_img, (210, 110))
            Ventana.blit(Titulo_ODS_4_img, (805, 110))
            Frase_ODS_1 = "Vida sana y cuidado pleno para cada persona, en cada etapa de su camino."
            Frase_ODS_2 = "El conocimiento como llave maestra hacia un futuro libre."
                    
        elif (Titulo == "C: Género/Agua"):
            Ventana.blit(Titulo_ODS_5_img, (210, 110))
            Ventana.blit(Titulo_ODS_6_img, (805, 110))
            Frase_ODS_1 = "Mismos derechos, mismas oportunidades: el empoderamiento no tiene género."
            Frase_ODS_2 = "Que el agua fluya como fuente de vida y derecho innegable."
                        
        elif (Titulo == "D: Energía/Trabajo"):
            Ventana.blit(Titulo_ODS_7_img, (210, 110))
            Ventana.blit(Titulo_ODS_8_img, (805, 110))
            Frase_ODS_1 = "Iluminar el mañana con energía limpia, infinita y al alcance de cada hogar."
            Frase_ODS_2 = "Progreso económico que dignifique el trabajo sin dañar el planeta."
                        
        elif (Titulo == "E: Industria/Desigualdad"):
            Ventana.blit(Titulo_ODS_9_img, (210, 110))
            Ventana.blit(Titulo_ODS_10_img, (805, 110))
            Frase_ODS_1 = "Construir el futuro con ingenio, conexiones sólidas y sostenibilidad."
            Frase_ODS_2 = "Nivelar la sociedad para que ningún origen defina nuestro destino."
                        
        elif (Titulo == "F: Ciudades/Producción"):
            Ventana.blit(Titulo_ODS_11_img, (210, 110))
            Ventana.blit(Titulo_ODS_12_img, (805, 110))
            Frase_ODS_1 = "Ciudades donde convivencia, desarrollo y naturaleza respiren juntos."
            Frase_ODS_2 = "Usar los recursos de hoy con verdadera responsabilidad por el mañana."
                        
        elif (Titulo == "G: Clima/Vida Submarina"):
            Ventana.blit(Titulo_ODS_13_img, (210, 110))
            Ventana.blit(Titulo_ODS_14_img, (805, 110))
            Frase_ODS_1 = "Actuar ahora para sanar nuestra casa común antes de que sea tarde."
            Frase_ODS_2 = "Proteger el azul de nuestros océanos, el latido que da vida al mundo."
                        
        elif (Titulo == "H: Ecosistemas/Paz"):
            Ventana.blit(Titulo_ODS_15_img, (210, 110))
            Ventana.blit(Titulo_ODS_16_img, (805, 110))
            Frase_ODS_1 = "Cuidar los bosques y cada especie que comparte nuestra tierra."
            Frase_ODS_2 = "Paz sin miedo, justicia sin barreras y sistemas justos para todos."

        Frase_ODS_1_TXT = Fuente.render(Frase_ODS_1, True, "White")
        Colision_Frase_1 = Frase_ODS_1_TXT.get_rect(center = (640, 650))
        Recuadro_Frase_1 = pygame.Rect(Colision_Frase_1.x - 10, Colision_Frase_1.y - 10, Colision_Frase_1.width + 20, Colision_Frase_1.height + 20)
        Transparencia_Recuadro_1 = pygame.Surface((Recuadro_Frase_1.width, Recuadro_Frase_1.height), pygame.SRCALPHA)
        pygame.draw.rect(Transparencia_Recuadro_1, (0, 0, 0, 200), (0, 0, Recuadro_Frase_1.width, Recuadro_Frase_1.height), 0, 15)

        Frase_ODS_2_TXT = Fuente.render(Frase_ODS_2, True, "White")
        Colision_Frase_2 = Frase_ODS_2_TXT.get_rect(center = (640, 650))
        Recuadro_Frase_2 = pygame.Rect(Colision_Frase_2.x - 10, Colision_Frase_2.y - 10, Colision_Frase_2.width + 20, Colision_Frase_2.height + 20)
        Transparencia_Recuadro_2 = pygame.Surface((Recuadro_Frase_2.width, Recuadro_Frase_2.height), pygame.SRCALPHA)
        pygame.draw.rect(Transparencia_Recuadro_2, (0, 0, 0, 200), (0, 0, Recuadro_Frase_2.width, Recuadro_Frase_2.height), 0, 15)

        Ventana.blit(Texto_Datos, (520, 50))

        if (Tarjeta_Ganadora_1):
            Ventana.blit(GANADOR_img, (157, 310))

            if (Puntos_Acumulados_TXT != None):
                Colision_Puntos = Puntos_Acumulados_TXT.get_rect(center = (345, 565))
                Ventana.blit(Puntos_Acumulados_TXT, Colision_Puntos)

            VOLVER_AL_MENU_img.Dibujo(Ventana)
        
        if (Tarjeta_Ganadora_2):
            Ventana.blit(GANADOR_img,(747, 310))
            
            if (Puntos_Acumulados_TXT != None):
                Colision_Puntos = Puntos_Acumulados_TXT.get_rect(center = (935, 565))
                Ventana.blit(Puntos_Acumulados_TXT, Colision_Puntos)

            VOLVER_AL_MENU_img.Dibujo(Ventana)

        if (Contador_Boton % 4 == 1) or (Contador_Boton % 4 == 2):
            Ventana.blit(Transparencia_Recuadro_1, (Recuadro_Frase_1.x, Recuadro_Frase_1.y))
            Ventana.blit(Frase_ODS_1_TXT, Colision_Frase_1)
            pygame.display.flip()
        
        else:
            Ventana.blit(Transparencia_Recuadro_2, (Recuadro_Frase_2.x, Recuadro_Frase_2.y))
            Ventana.blit(Frase_ODS_2_TXT, Colision_Frase_2)
            pygame.display.flip()


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    Main()