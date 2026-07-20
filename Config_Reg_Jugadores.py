import pygame, sys, os

class Dato_Jugador:
    def __init__ (self, Texto, Tamaño, Posicion, Color_Inactivo, Fuente, Fuente_Negrita):
        self.Recuadro = pygame.Rect(Posicion, Tamaño)
        self.Color = Color_Inactivo
        self.Texto = Texto
        self.Render_TXT = Fuente_Negrita.render(Texto, True, self.Color)
        self.Escrito = ""
        self.Render_Esc = Fuente.render(self.Escrito, True, self.Color)
        self.Colision = self.Render_TXT.get_rect(center = Posicion)
        self.Clickeado = False
        self.Dato = ""

    def Escritura(self, event, Color_Inactivo, Color_Activo, Fuente, Fuente_Negrita, Tamaño_Caracteres):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (self.Recuadro.collidepoint(event.pos)):
                self.Clickeado = True
            else:
                self.Clickeado = False 
            
            if (self.Clickeado == True):
                self.Color = Color_Activo
            else:
                self.Color = Color_Inactivo
      
        self.Render_TXT = Fuente_Negrita.render(self.Texto, True, self.Color)
        self.Render_Esc = Fuente.render(self.Escrito, True, self.Color)
    
        if (event.type == pygame.KEYDOWN):
            if (self.Clickeado == True):
                if (event.key == pygame.K_BACKSPACE):
                    self.Escrito = self.Escrito[:-1]
                else:
                    if (len(self.Escrito) < Tamaño_Caracteres):
                        self.Escrito = self.Escrito + event.unicode
        
            self.Render_Esc = Fuente.render(self.Escrito, True, self.Color)

    def Dibujo(self, Ventana, Pos_Escrito_X, Pos_Escrito_Y):
        Ventana.blit(self.Render_TXT, (self.Colision.x + 150, self.Colision.y - 25))
        pygame.draw.rect(Ventana, self.Color, self.Recuadro, 2, 15)
        Ventana.blit(self.Render_Esc, (self.Recuadro.x + Pos_Escrito_X, self.Recuadro.y + Pos_Escrito_Y))