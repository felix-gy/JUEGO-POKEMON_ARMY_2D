import pygame
pygame.mixer.init()

verde_celeste = (86, 207, 225)
negro = (0,0,0)
blanco = (255,255,255)
Rojo_brillante = (255,0,0)
Rojo = (200,0,0)
negro_azul = (46, 64, 83)
negro_azul_2 = (23, 32, 42)
celeste = (72,191,227)
plomo = (127, 140, 141)
amarillo1 = (242, 193, 46)
amarillo2 = (242, 169, 34)
naranja = (242, 135, 5)
cafe = (166, 118, 60)
azul = (9, 103, 224)
morado = (32, 1, 64)
comicsans = pygame.font.match_font('comicsans')
#NUEVO BOTON
class Boton():
    def __init__(self, color, x,y,width,height, text):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,lienzo,outline=None):
        
        if outline:
            pygame.draw.rect(lienzo, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(lienzo, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 21)
            text = font.render(self.text, 1, (0,0,0))
            lienzo.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def seleccion_mouse(self, pos):
        
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


ancho_lienzo = 1120 +56*2
alto_lienzo = 672 + 56*2
lienzo = pygame.display.set_mode((ancho_lienzo,alto_lienzo))




arial = pygame.font.match_font("arial")
def muestra_texto(pantalla,fuente,texto,color,dimensiones,x,y):
    tipo_letra = pygame.font(fuente,dimensiones)
    superficie = tipo_letra.render(texto,True,color)
    rectangulo = superficie.get_rect()
    rectangulo.center(x,y)
    pantalla.blit(superficie,rectangulo)
pokeball = pygame.image.load("pokeball1.gif")
charmander_izquierda = pygame.image.load('charmander_1.png')
bloque_pasto = pygame.image.load('grass1.png')
bloque_pasto_1 = pygame.transform.scale(bloque_pasto, (56, 56))
pikachu_boton = pygame.image.load("pikachu_boton.png")
pikachu_izquierda = pygame.image.load('pikachu_izquierda.png')
pikachu_boton2 = pygame.image.load("pikachu_boton2.gif")
pikachu_derecha = pygame.image.load('pikachu_derecha.png')
pikachu_arriba = pygame.image.load('pikachu_arriba.png')
pikachu_abajo = pygame.image.load('pikachu_abajo.png')
bloque_pasto_2 = pygame.image.load("pasto_seleccion1.png")


sonido_pokeball = pygame.mixer.Sound("Pokeball Abriendose.wav")
soundtrack = pygame.mixer.Sound("Pokemon Soundtrack.mp3")

verde1 = (38,142,0)

charmander_boton1 = pygame.image.load("charmander_boton.png")
charmander_boton2 = pygame.image.load("charmander_boton2.gif")
charmander_derecha = pygame.image.load("charmander_derecha.png")
charmander_izquierda1 = pygame.image.load('charmander_1.png')
charmander_izquierda = pygame.transform.scale(charmander_izquierda, (34, 34))

riulu_boton1 = pygame.image.load("riulu_boton1.png")
riulu_boton2 = pygame.image.load("riulu_boton2.png")
riulu_izquierda = pygame.image.load("riolu_izquierda.png")
riulu_derecha = pygame.image.load( "riolu_derecha.png")

ram_boton1 = pygame.image.load("ram_boton1.png")
ram_boton2 = pygame.image.load("Sandshrew_boton2.gif")
Sandshrew_izquierda = pygame.image.load("ram_izquierda.png")
Sandshrew_derecha = pygame.image.load( "ram_derecha.png")

lapras_boton1 = pygame.image.load("lapras_boton1.png")
lapras_boton2 = pygame.image.load("lapras_boton2.png")
lapras_izquierda = pygame.image.load("lapras_izquierda.png")
lapras_derecha = pygame.image.load( "lapras_derecha.png")

gengar_boton1 = pygame.image.load("gengar_boton1.png")
gengar_boton2 = pygame.image.load("gengar_boton2.jpg")
gengar_izquierda = pygame.image.load("gengar_izquierda.gif")
gengar_derecha = pygame.image.load( "gengar_derecha.gif")



seleccion = False
boton_pikachu = False
boton_pikachu_eleccion = False
boton_charmander_eleccion = False
boton_riulu_eleccion = False
boton_ram_eleccion = False
boton_lapras_eleccion = False
boton_gengar_eleccion = False

turno1 = True
turno2 = False

contador_eleccion = 0

moverse1 = False
moverse2 = False
bloque_lista_piso = pygame.sprite.Group()
lista_todos_sprites = pygame.sprite.Group()

lista_pokemones_player1 = pygame.sprite.Group()

lista_pokemones_player2 = pygame.sprite.Group()

lista_radios = pygame.sprite.Group()

botones_activo_charmander = True 
botones_activo_pikachu = True 
botones_activo_riulu = True
botones_activo_ram = True 
botones_activo_lapras = True 
botones_activo_gengar = True 
dibujar_radio = False
estado_radio1 = False
estado_radio2 = False
ataque_estado1 = False
ataque_estado2 = False
poder_curacion1 =False
poder_curacion2 = False
turnos = False
Boton_poder_estado1 = False
Boton_poder_estado2 = False
contador_curacion = 0
fondo2 = pygame.image.load("fondo2.png")
fondo2_escalado = pygame.transform.scale(fondo2,( ancho_lienzo  , alto_lienzo - 56*3))
fondo_1 = pygame.image.load("fondo3.png")
fondo_pantalla = pygame.transform.scale(fondo_1,(ancho_lienzo, alto_lienzo))
ataque_sonido = pygame.mixer.Sound('ataque_pokemon.mp3')
curacion_sonido = pygame.mixer.Sound('curacion_pokemon.mp3')
lista_todos_pokemones = pygame.sprite.Group()
texto_activo = False
estado = True