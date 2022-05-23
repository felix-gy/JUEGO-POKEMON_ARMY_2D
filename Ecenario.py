import pygame,sys
from pygame.locals import *

import time
from Botones import *

pygame.init()

#ESTE ES UN ENECESARIO
     
botones_activo = True

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top = pygame.mouse.get_pos()
class Objeto(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):
        super().__init__()
        self.imagen1 = imagen1
        self.imagen2 = imagen2
        self.imagen_actual = self.imagen1
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen2
        else:
            self.imagen_actual = self.imagen1
        
        lienzo.blit(self.imagen_actual,self.rect)

cursor1 = Cursor()  
pygame.display.set_caption("Pokemon Army 2D")

botones_activo = True

if botones_activo == True :
    pikachu_eleccion = Objeto(pikachu_boton, pikachu_boton2,100 , 556 + 56*2)
    charmander_seleccion = Objeto(charmander_boton1,charmander_boton2,200, 556+ 56*2)
    riulu_seleccion = Objeto(riulu_boton1, riulu_boton2, 300 , 556+ 56*2)
    ram_seleccion = Objeto(ram_boton1, ram_boton2, 400 , 556+ 56*2)
    lapras_seleccion = Objeto(lapras_boton1, lapras_boton2, 500 , 556+ 56*2)
    gengar_seleccion = Objeto(gengar_boton1, gengar_boton2, 600 , 556+ 56*2)

bloque = 56

bloque_de_inicio = Objeto(bloque_pasto_1, bloque_pasto_2, 56 ,bloque*2)    
bloque_de_inicio2 = Objeto(bloque_pasto_1, bloque_pasto_2, 56 ,bloque * 3 )
bloque_de_inicio3 = Objeto(bloque_pasto_1, bloque_pasto_2, 56 ,bloque * 4 )
bloque_de_inicio4 = Objeto(bloque_pasto_1, bloque_pasto_2, 56 ,bloque * 5 )
bloque_de_inicio5 = Objeto(bloque_pasto_1, bloque_pasto_2, 56 ,bloque * 6 )
bloque_de_inicio6 = Objeto(bloque_pasto_1, bloque_pasto_2, 56 ,bloque * 7 )
bloque_de_inicio7 = Objeto(bloque_pasto_1, bloque_pasto_2, 56 ,bloque * 8 )
bloque_de_inicio8 = Objeto(bloque_pasto_1, bloque_pasto_2, 56 ,bloque * 9 )

bloque_de_inicio11 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 2  ,bloque *2)
bloque_de_inicio22 = Objeto(bloque_pasto_1, bloque_pasto_2, bloque * 2 ,bloque * 3)
bloque_de_inicio33 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 2 ,bloque * 4)
bloque_de_inicio44 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 2  ,bloque* 5)
bloque_de_inicio55 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 2  ,bloque* 6)
bloque_de_inicio66 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 2  ,bloque * 7)
bloque_de_inicio77 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 2 ,bloque * 8)
bloque_de_inicio88 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 2  ,bloque * 9)

bloque_de_inicio111 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 19    ,bloque*2)
bloque_de_inicio222 = Objeto(bloque_pasto_1, bloque_pasto_2, bloque * 19 ,bloque * 3)
bloque_de_inicio333 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 19 ,bloque * 4)
bloque_de_inicio444 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 19  ,bloque* 5)
bloque_de_inicio555 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 19  ,bloque* 6)
bloque_de_inicio666 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 19  ,bloque * 7)
bloque_de_inicio777 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 19 ,bloque * 8)
bloque_de_inicio888 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 19  ,bloque * 9)

bloque_de_inicio1111 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 20    ,bloque*2)
bloque_de_inicio2222 = Objeto(bloque_pasto_1, bloque_pasto_2, bloque * 20 ,bloque * 3)
bloque_de_inicio3333 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 20 ,bloque * 4)
bloque_de_inicio4444 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 20  ,bloque* 5)
bloque_de_inicio5555 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 20  ,bloque* 6)
bloque_de_inicio6666 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 20  ,bloque * 7)
bloque_de_inicio7777 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 20 ,bloque * 8)
bloque_de_inicio8888 = Objeto(bloque_pasto_1, bloque_pasto_2,  bloque * 20  ,bloque * 9)


def funcion_bloque_de_inicio():
    bloque_de_inicio.update(lienzo, cursor1)
    bloque_de_inicio2.update(lienzo, cursor1)
    bloque_de_inicio3.update(lienzo, cursor1)
    bloque_de_inicio4.update(lienzo, cursor1)
    
    bloque_de_inicio6.update(lienzo, cursor1)
    bloque_de_inicio7.update(lienzo, cursor1)
    bloque_de_inicio8.update(lienzo, cursor1)

    bloque_de_inicio11.update(lienzo, cursor1)
    bloque_de_inicio22.update(lienzo, cursor1)
    bloque_de_inicio33.update(lienzo, cursor1)
    bloque_de_inicio44.update(lienzo, cursor1)
    bloque_de_inicio55.update(lienzo, cursor1)
    bloque_de_inicio66.update(lienzo, cursor1)
    bloque_de_inicio77.update(lienzo, cursor1)
    bloque_de_inicio88.update(lienzo, cursor1)

    bloque_de_inicio111.update(lienzo, cursor1)
    bloque_de_inicio222.update(lienzo, cursor1)
    bloque_de_inicio333.update(lienzo, cursor1)
    bloque_de_inicio444.update(lienzo, cursor1)
    bloque_de_inicio555.update(lienzo, cursor1)
    bloque_de_inicio666.update(lienzo, cursor1)
    bloque_de_inicio777.update(lienzo, cursor1)
    bloque_de_inicio888.update(lienzo, cursor1)

    bloque_de_inicio1111.update(lienzo, cursor1)
    bloque_de_inicio2222.update(lienzo, cursor1)
    bloque_de_inicio3333.update(lienzo, cursor1)
    bloque_de_inicio4444.update(lienzo, cursor1)
    bloque_de_inicio5555.update(lienzo, cursor1)
    bloque_de_inicio6666.update(lienzo, cursor1)
    bloque_de_inicio7777.update(lienzo, cursor1)
    bloque_de_inicio8888.update(lienzo, cursor1)

pokemon_a_seleccionar = None
class Radio(pygame.sprite.Sprite):      
    def __init__(self,ancho,alto,color):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = pygame.Surface([ancho , alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = 56
        self.rect.y = 56
        self.rect.centerx = 0
        self.rect.centery = 0
        self.ancho = ancho 
        self.alto = alto
blqoue = 54


def muestra_texto(pantalla,fuente,texto,color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie,rectangulo)