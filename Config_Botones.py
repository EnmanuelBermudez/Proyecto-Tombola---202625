import pygame

class Boton:
    def __init__ (self, Ruta_Imagen, Tamaño, Posicion, Ruta_Sonido):
        self.Imagen = pygame.image.load(Ruta_Imagen).convert_alpha()
        self.Imagen = pygame.transform.scale(self.Imagen, Tamaño)
        self.Colision = self.Imagen.get_rect(topleft = Posicion)
        self.Sonido = pygame.mixer.Sound(Ruta_Sonido)

    def Dibujo(self, Ventana):
        Ventana.blit(self.Imagen, self.Colision)
    
    def Es_Presionado(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (self.Colision.collidepoint(event.pos)):
                self.Sonido.play()
                return True
        return False