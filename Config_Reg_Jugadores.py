import pygame, sys, os, Registro_Jugadores

class Dato_Jugador:
    def __init__ (self, Texto, Tamaño, Posicion, Fuente):
        self.Recuadro = pygame.Rect(Posicion, Tamaño)
        self.Color = "grey70"
        self.Texto = Texto
        self.Render_TXT = Fuente.render(Texto, 30, self.Color)
        self.Escrito = ""
        self.Render_Esc = Fuente.render(self.Escrito, 30, self.Color)
        self.Colision = self.Texto.get_rect(center = Posicion)
        self.Clickeado = False
        self.Dato = ""

    def Escritura(self, event, Fuente):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if  (self.Clickeado == True):
                if (self.Recuadro.collidepoint(event.pos)):
                    self.Clickeado = True
                else:
                    self.Clickeado = False 
                
                if (self.Clickeado == True):
                    self.Color = "White"
                else:
                    self.Color = "Grey70"
    
        if (event.type == pygame.KEYDOWN):
            if (self.Clickeado == True):
                if (event.key == pygame.K_BACKSPACE):
                    self.Escrito = self.Escrito[:-1]
                else:
                    if (self.Escrito < 30):
                        self.Escrito = self.Escrito + event.unicode
        
            self.Render_Esc = Fuente.render(self.Escrito, True, self.Color)

    def Dibujo(self, Ventana):
        Ventana.blit(self.Render_TXT, (self.Colision.x, self.Colision.y - 25))
        pygame.draw.rect(Ventana, self.Color, self.Recuadro, 2, 15)
        Ventana.blit(self.Render_Esc, (self.Recuadro.x + 5, self.Recuadro.y + 5))
