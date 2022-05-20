import pygame,sys
from pygame.locals import *
from Botones import *

class Pokemon(pygame.sprite.Sprite):  
    def __init__(self,nombre,imagen,imagen_reversa,x,y,vida,ataque,fuerza,poder,nombredelpoder,tipo):
        super().__init__()
        self.nombre = nombre
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image_reversa = imagen_reversa
        self.vida = vida 
        self.ataque = ataque    
        self.fuerza = fuerza   
        self.poder = poder
        self.nombredelpoder = 'nombredelpoder'
        self.tipo = tipo
     

class Pokeball(pygame.sprite.Sprite):
    
    def __init__(self,imagen,x,y):
        super().__init__()
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


pikachu = Pokemon('Pikachu',pikachu_derecha,pikachu_izquierda,0,0,370,55,30,90,'Impactrueno','Electrico')

charmander = Pokemon('Charmander',charmander_derecha, charmander_izquierda, 0, 0,390,52,25,90,'Arañaso','Fuego')

lapras = Pokemon('Lapras',lapras_derecha, lapras_izquierda, 0, 0,410,65,30,90,'Absorberagua','Agua')

Sandshrew = Pokemon('Sandshrew',Sandshrew_derecha , Sandshrew_izquierda, 0, 0,400,75,20,90,'Veldearena','Tierra')

gengar = Pokemon('Gengar',gengar_derecha,gengar_izquierda, 0,0,345,83,10,100,'Shadow_Ball','Fantasma')

riulu = Pokemon('Riolu',riulu_derecha,riulu_izquierda, 0,0,374,59,25,70,'Aguante Endure','Lucha')

pokeball_imagen = pygame.transform.scale(pokeball,(15, 15))

pokeball1 = Pokeball(pokeball_imagen, 0, 0)

print(pikachu.nombre)
print(gengar.tipo)


   