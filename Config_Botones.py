import pygame

class Boton:
    def __init__ (self, Ruta_Imagen, Tamaño, Posicion, Ruta_Sonido):
        self.imagen = pygame.image.load(Ruta_Imagen).convert_alpha()
        self.imagen = pygame.transform.smoothscale(self.imagen, Tamaño)
        self.Colision = self.imagen.get_rect(topleft = Posicion)
        self.Sonido = pygame.mixer.Sound(Ruta_Sonido)
        self.Presionado = False

    def draw(self, Ventana):
        Ventana.blit(self.imagen, self.Colision)
    
    def es_presionado(self):
        Posicion_Mouse = pygame.mouse.get_pos()
        Click_Izquierdo = pygame.mouse.get_pressed()[0]

        if (self.Colision.collidepoint(Posicion_Mouse)):
            if (Click_Izquierdo and not self.Presionado):
                self.Presionado = True
                self.Sonido.play()
                return True
            
        if (not Click_Izquierdo):
            self.Presionado = False
        return False