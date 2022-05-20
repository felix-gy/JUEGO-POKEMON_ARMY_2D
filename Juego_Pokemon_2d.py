import pygame,sys
from pygame.locals import *
import random
import time
from Botones import *
from Pokemones import *
from Ecenario import *



pygame.init()
pygame.mixer.init()
#ancho_lienzo = 780
#alto_lienzo = 600

pygame.display.set_caption("Pokemon Army 2D")
moverse = False
def funcionmoverse():
    global moverse
    moverse1 = True
#colores



contador_movimientos = 0

#PRUEBA -- CREAR UN BLOQUE
class Block(pygame.sprite.Sprite):
    def __init__(self, ancho, alto,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho , alto])
        self.image.fill(verde1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.width = ancho
        self.height = alto
class imagen_sprite(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

class texto(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__(self)  
        

lienzo.fill(blanco)


contador_movimientos_player1 = 0
contador_movimientos_player2 = 0











greenboton = Boton(verde_celeste, 1080, 20, 70,30 ,'SALIR')
 
boton_moverse1 = Boton(celeste,30 +56 , 525 + 112,80 ,25, 'MOVERSE 1')
boton_moverse2 = Boton(Rojo,700+56, 525 + 112,80 ,25, 'MOVERSE 2')

Boton_Attack1 = Boton(verde_celeste,130+56, 525 + 112,80,25,'Attack')
Boton_Attack2 = Boton(Rojo,800+56, 525 + 112,80,25,'Attack')

Boton_Poder1 = Boton(naranja,230+56, 525 + 112,80,25,'Poder')
Boton_Poder2 = Boton(naranja,900+56, 525 + 112,80,25,'Poder')
def dibujarboton():
    greenboton.draw(lienzo)






def funcionboton():
    pygame.QUIT
    pygame.quit()
    jugando = False
    sys.exit()

clock = pygame.time.Clock()

#charmander = Pokemon(charmander_izquierda, 0,0 )



###########piso_verde = Pokemon(bloque_pasto, 0, 0)

lista_piso_verde = pygame.sprite.Group()

#bloque_lista_piso.add(piso_verde)

bloque_cursor = Block(1, 1, 0, 0)

lista_todos_sprites.add(bloque_cursor)


for b in range(56,600,56):
   for i in range(0,1200,56):
        bloque1 = Pokeball(bloque_pasto_1,i , b)
        #bloque1 = Block(56, 56, i, b)
        bloque_lista_piso.add(bloque1) 







fondo = pygame.image.load('fondo_1.png') #Fondo cargar imagen
ubicar = False




for i in range(56,1200,56):
    pygame.draw.line(lienzo, negro, (0,i), (1500,i),1)
    pygame.draw.line(lienzo, negro, (i,0), (i,1500),1)





lista_pikachu = pygame.sprite.Group()
lista_pikachu.add(pikachu)

lista_charmander = pygame.sprite.Group()
lista_charmander.add(charmander)

lista_riulu = pygame.sprite.Group()
lista_riulu.add(riulu)

lista_ram = pygame.sprite.Group()
lista_ram.add(Sandshrew)

lista_lapras = pygame.sprite.Group()
lista_lapras.add(lapras)

lista_gengar = pygame.sprite.Group()
lista_gengar.add(gengar)

contador_eleccion = 0 
if contador_eleccion == 6:
    time.sleep(1)
    #turno1 = False
    #turno2 = False

        

jugando = True

#for n in range(2,10,2):    
 #   bloqueradio = Radio(pikachu)           
  #  lista_radio_pikachu.add(bloqueradio) 
bloque_radio_a_ubicar = Radio(bloque * 7,bloque * 5,celeste)
while jugando:#para la ejecucion de eventos
    
    def ubicar_radio1(bloque_radio_a_ubicar,pokemon_a_radio1):
        bloque_radio_a_ubicar.rect.centerx = pokemon_a_radio1.rect.x + 20 
        bloque_radio_a_ubicar.rect.centery = pokemon_a_radio1.rect.y + 20
        lista_radios.add(bloque_radio_a_ubicar)    
    def ubicar_radio2(bloque_radio_a_ubicar,pokemon_a_radio2):
        bloque_radio_a_ubicar.rect.centerx = pokemon_a_radio2.rect.x + 20 
        bloque_radio_a_ubicar.rect.centery = pokemon_a_radio2.rect.y + 20
        lista_radios.add(bloque_radio_a_ubicar)     #for n in range(2,10,2):    
    
    if contador_eleccion == 6:
        time.sleep(1)
        pygame.mixer.Sound.play(soundtrack,-1)
        turnos = True
        contador_eleccion +=1


 
    def Casilla_de_ubicacion(bloque,pokemon_a_seleccionar):
        #print('EVENTO')
        if evento.type == pygame.MOUSEBUTTONDOWN:
            #print('CASILLA DE UBICACION')
            if cursor1.colliderect(bloque):
                #print("ok")
                boton_pikachu_eleccion = False
                pokeball1.rect.x = bloque.rect.x 
                pokeball1.rect.y = bloque.rect.y
                pygame.mixer.Sound.play(sonido_pokeball)
                time.sleep(1)
                lista_todos_pokemones.add(pokemon_a_seleccionar)
                pokemon_a_seleccionar.rect.x = bloque.rect.x +  8
                pokemon_a_seleccionar.rect.y = bloque.rect.y +  8
                time.sleep(1)                
                lista_todos_sprites.remove(pokeball1)
                ubicando  = False
                if contador_eleccion <= 2:
                    print('PLAYER 1')
                    print(str(pokemon_a_seleccionar))
                    lista_pokemones_player1.add(pokemon_a_seleccionar)
                if contador_eleccion >= 3:
                    print('PLAYER 2')
                    pokemon_a_seleccionar.image = pokemon_a_seleccionar.image_reversa
                    print(pokemon_a_seleccionar)
                    lista_pokemones_player2.add(pokemon_a_seleccionar)
    lista_impactos_bloques1 = pygame.sprite.spritecollide(bloque_cursor, lista_pikachu, False)
    lista_impactos_bloques2 = pygame.sprite.spritecollide(bloque_cursor, lista_charmander, False)
    lista_impactos_bloques3 = pygame.sprite.spritecollide(bloque_cursor, lista_riulu, False)
    lista_impactos_bloques4 = pygame.sprite.spritecollide(bloque_cursor, lista_ram, False)
    lista_impactos_bloques5 = pygame.sprite.spritecollide(bloque_cursor, lista_lapras, False)
    lista_impactos_bloques6 = pygame.sprite.spritecollide(bloque_cursor, lista_gengar, False)

    lista_seleccion_player1 = pygame.sprite.spritecollide(bloque_cursor, lista_pokemones_player1,False)
    lista_seleccion_player2 = pygame.sprite.spritecollide(bloque_cursor, lista_pokemones_player2,False)
    pos = pygame.mouse.get_pos()


    cursor1.update()

    
    if turnos:
        
        if turno1 == True:
            contador_movimientos_player2 = 0
            if estado_radio1:
                ubicar_radio1(bloque_radio_a_ubicar, pokemon_a_radio1)
                estado_radio2 =False
            
 
            ataque_estado2 = False


            #print('player1')
            #print(contador_movimientos_player1)
            Boton_Attack1.draw(lienzo)
            boton_moverse1.draw(lienzo)
            if estado:
                if lista_impactos_bloques5:
                    if lista_pokemones_player1:
                        Boton_poder_estado1 = True
                        estado = False

            if Boton_poder_estado1:
                Boton_Poder1.draw(lienzo)

            #player1(contador_movimientos_player1)
        muestra_texto(lienzo,comicsans, str(contador_movimientos_player1) , blanco, 30,42, 640)
        if turno2 == True:
            contador_movimientos_player1 = 0
            if estado_radio2:  
                ubicar_radio2(bloque_radio_a_ubicar, pokemon_a_radio2)
                estado_radio1 = False
            ataque_estado1 = False
            
            #print('player2')
            #print(contador_movimientos_player2)

            boton_moverse2.draw(lienzo)

            Boton_Attack2.draw(lienzo)
            if estado:
                if lista_impactos_bloques5:
                    if lista_pokemones_player2:
                        Boton_poder_estado2 = True
                        estado = False

            if Boton_poder_estado2:
                Boton_Poder2.draw(lienzo)
            muestra_texto(lienzo,comicsans, str(contador_movimientos_player2) , blanco, 30,1059, 640)
            turno1 = False
        #player2(contador_movimientos_player1)

        
    if contador_movimientos_player1 == 3:
        turno2 = True
        turno1  = False
        moverse1 = False
        moverse2 = False
    if contador_movimientos_player2 == 3:
        turno1 = True
        turno2 =False
        moverse1 = False
        moverse2  =False


    def Ubicacion(Pokemon_a_ubicar):
        Pokemon_a_ubicar.rect.x = pos[0] - 16
        Pokemon_a_ubicar.rect.y = pos[1] - 16
        lista_todos_sprites.add(Pokemon_a_ubicar)
    if boton_pikachu == True:
        Ubicacion(pikachu)
    if boton_pikachu_eleccion == True:
        Ubicacion(pokeball1)
        pokemon_a_seleccionar = pikachu
        seleccion = True
    if boton_charmander_eleccion == True:
        Ubicacion(pokeball1)
        pokemon_a_seleccionar = charmander
        seleccion = True
    if boton_riulu_eleccion == True:
        Ubicacion(pokeball1)
        pokemon_a_seleccionar = riulu
        seleccion = True
    if boton_ram_eleccion == True:
        Ubicacion(pokeball1)
        pokemon_a_seleccionar = Sandshrew
        seleccion = True
    if boton_lapras_eleccion == True:
        Ubicacion(pokeball1)
        pokemon_a_seleccionar = lapras
        seleccion = True
    if boton_gengar_eleccion == True:
        Ubicacion(pokeball1)
        pokemon_a_seleccionar = gengar
        seleccion = True
    

    dibujarboton()

    



    if botones_activo_charmander == True :
        charmander_seleccion.update(lienzo, cursor1)
        
    if botones_activo_pikachu == True :
        pikachu_eleccion.update(lienzo, cursor1)
    if botones_activo_riulu == True :
        riulu_seleccion.update(lienzo, cursor1)
    if botones_activo_ram == True :
        ram_seleccion.update(lienzo, cursor1)
    if botones_activo_lapras == True :
        lapras_seleccion.update(lienzo, cursor1)
    if botones_activo_gengar == True :
        gengar_seleccion.update(lienzo, cursor1)

    
        
    pos = pygame.mouse.get_pos()    
    bloque_cursor.rect.x = pos[0]
    bloque_cursor.rect.y = pos[1]

    
    bloque_lista_piso.draw(lienzo)
    #boton('MOVERSE', 200,500, 100, 40,celeste, verde_celeste,funcionmoverse)
       

    lista_impactos_bloques = pygame.sprite.spritecollide(pikachu, bloque_lista_piso, False)
    #if lista_impactos_bloques:
     #   print("_-pisado-_")


    lista_seleccion_radio_pikachu = pygame.sprite.spritecollide(bloque_cursor, lista_radios,False)

    lista_seleccion_ataque_player2 = pygame.sprite.spritecollide(bloque_cursor, lista_pokemones_player2,False)
    lista_seleccion_ataque_player1 = pygame.sprite.spritecollide(bloque_cursor, lista_pokemones_player1,False)

    if lista_seleccion_ataque_player2:
        if pikachu.vida <= 0:
            pikachu.kill()
        if charmander.vida <= 0:
            charmander.kill()
        if riulu.vida <= 0:
            riulu.kill()
        if lapras.vida <= 0:
            lapras.kill()
        if gengar.vida <= 0:
            gengar.kill()
        if Sandshrew.vida <= 0:
            Sandshrew.kill()            
    lista_pokemones_radio_ataque_player1 = pygame.sprite.spritecollide(bloque_radio_a_ubicar,lista_pokemones_player2 ,False)

    lista_pokemones_radio_ataque_player2 = pygame.sprite.spritecollide(bloque_radio_a_ubicar,lista_pokemones_player1 ,False)
    
    def ataque_player1(pokemon_seleccionado_player1,pokemon_seleccionado_player2):
        print(pokemon_seleccionado_player1.nombre)
        print('ataque')
        print(pokemon_seleccionado_player1.ataque)
        print(pokemon_seleccionado_player2.nombre)
        print('vida1')
        print(pokemon_seleccionado_player2.vida)
        pygame.mixer.Sound.play(ataque_sonido) 
        pokemon_seleccionado_player2.vida = pokemon_seleccionado_player2.vida - pokemon_seleccionado_player1.ataque
        print(pokemon_seleccionado_player2.nombre)
        print('vida 2')
        print(pokemon_seleccionado_player2.vida,)
    def ataque_player2(pokemon_seleccionado_player2,pokemon_seleccionado_player1):
        print(pokemon_seleccionado_player2.nombre)
        print('ataque')
        print(pokemon_seleccionado_player2.ataque)
        print(pokemon_seleccionado_player1.nombre)
        print('vida1')
        print(pokemon_seleccionado_player1.vida)
        pokemon_seleccionado_player1.vida = pokemon_seleccionado_player1.vida - pokemon_seleccionado_player2.ataque
        print(pokemon_seleccionado_player1.nombre)
        print('vida 2')
        print(pokemon_seleccionado_player1.vida)
        pygame.mixer.Sound.play(ataque_sonido) 
    def poder_curacion(pokemon_seleccionado_player1):
        dibujar_radio = False
        print(pokemon_seleccionado_player1.nombre)
        print(pokemon_seleccionado_player1.vida)
        print("curacion")
        pokemon_seleccionado_player1.vida = pokemon_seleccionado_player1.vida + 30
        print(pokemon_seleccionado_player1.vida)
        pygame.mixer.Sound.play(curacion_sonido)

    #if lista_impactos_bloques:
    #    print("encima")
    #    bloque1.image = pikachu_derecha
    #    piso_verde.image = pikachu_abajo
    
    funcion_bloque_de_inicio()
    if dibujar_radio:
        lista_radios.draw(lienzo) 
    
    lista_todos_sprites.draw(lienzo)
    lista_todos_pokemones.draw(lienzo)
    pygame.display.update()
    for evento in pygame.event.get(): 
        pos = pygame.mouse.get_pos()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if greenboton.seleccion_mouse(pos): 
                #print("Click")
                funcionboton()
            if turno1 == True:   
                if boton_moverse1.seleccion_mouse(pos):
                    moverse2 = False
                    moverse1 = True
                    contador_moviemientos_player2 = 0
                    contador_moviemientos_player1 = 0
                    dibujar_radio = False

                if Boton_Attack1.seleccion_mouse(pos):
                    #print('ataqueen')
                    dibujar_radio = True
                    ataque_estado2 = False
                    ataque_estado1 = True
                if  Boton_Poder1.seleccion_mouse(pos):
                    
                    dibujar_radio = True
                    poder_curacion1 = True
                    poder_curacion2 = False
                    
            if turno2 == True:   
                #print("Clicknmoverse1")
                if boton_moverse2.seleccion_mouse(pos):
                    
                    moverse1 = False
                    moverse2 = True
                    contador_moviemientos_player1 = 0
                    contador_moviemientos_player2 = 0
                    dibujar_radio = False

                if Boton_Attack2.seleccion_mouse(pos):
                    print('ataqueen')
                    dibujar_radio = True
                    ataque_estado1 = False
                    ataque_estado2 = True
                if  Boton_Poder2.seleccion_mouse(pos):
                    poder_curacion1 = False
                    poder_curacion2 = True
                    bloque_radio_a_ubicar = Radio(bloque * 5,bloque * 5,celeste)
                    dibujar_radio = True
                #print('clickboton2 moverse')

            if lista_impactos_bloques1:
                lista_radios.remove(bloque_radio_a_ubicar)
                pokemon_a_mover = pikachu
                #print('pikachu')
                bloque_radio_a_ubicar = Radio(bloque * 7,bloque * 5,amarillo1)
            if lista_impactos_bloques2:
                lista_radios.remove(bloque_radio_a_ubicar)
                pokemon_a_mover = charmander
                bloque_radio_a_ubicar = Radio(bloque * 5,bloque * 5,naranja)
            if lista_impactos_bloques3:
                lista_radios.remove(bloque_radio_a_ubicar)
                pokemon_a_mover = riulu
                bloque_radio_a_ubicar = Radio(bloque * 3,bloque * 3,azul)
            if lista_impactos_bloques4:
                lista_radios.remove(bloque_radio_a_ubicar)
                pokemon_a_mover = Sandshrew
                bloque_radio_a_ubicar =  Radio(bloque * 3,bloque * 3,cafe)
            if lista_impactos_bloques5:
                lista_radios.remove(bloque_radio_a_ubicar)
                pokemon_a_mover = lapras
                bloque_radio_a_ubicar = Radio(bloque * 5,bloque * 5,celeste)
            if lista_impactos_bloques6:
                lista_radios.remove(bloque_radio_a_ubicar)
                pokemon_a_mover = gengar
                bloque_radio_a_ubicar = Radio(bloque * 5,bloque * 5,morado)
            if lista_seleccion_player1:
                print('PLAYER 1 POKEMON')
                pokemon_a_mover_player1 = pokemon_a_mover
                pokemon_seleccionado_player1 = pokemon_a_mover
                pokemon_a_radio1 = pokemon_a_mover
                estado_radio2 = False
                estado_radio1 = True
                texto_activo = True
              #  if contador_curacion == 2:
               #     pokemona_a_curar = pokemon_a_mover
            if lista_seleccion_player2:
                pokemon_a_mover_player2 = pokemon_a_mover
                print('PLAYER 2 POKEMON')
                pokemon_a_radio2 = pokemon_a_mover
                pokemon_seleccionado_player2 = pokemon_a_mover
                #if contador_curacion == 2:
                 #   pokemona_a_curar = pokemon_a_mover
                  #  contador_eleccion -=2                
                estado_radio1 = False
                estado_radio2 = True
                texto_activo = True

            if ataque_estado1:
                if lista_pokemones_radio_ataque_player1:
                    if lista_seleccion_ataque_player2:
                        #print("ATAQUE1")
                        #contador_curacion +=1
                        ataque_player1(pokemon_seleccionado_player1, pokemon_seleccionado_player2)
                    
                        contador_movimientos_player1 += 1
                        ataque_estado1 = False
                        
            if ataque_estado2:
                if lista_pokemones_radio_ataque_player2:
                    if lista_seleccion_ataque_player1:
                        #print("ATAQUE2")
                        ataque_player2(pokemon_seleccionado_player2, pokemon_seleccionado_player1)
                        contador_movimientos_player2 += 1
                        ataque_estado2 = False
            if poder_curacion1:
                if lista_pokemones_radio_ataque_player1:
                    if lista_seleccion_ataque_player1:
                        print("Curacion1")
                        poder_curacion(pokemon_a_mover)
                        contador_movimientos_player1 += 1
                        lista_pokemones_radio_ataque_player1: False
            if poder_curacion2:
                if lista_pokemones_radio_ataque_player2:
                    if lista_seleccion_ataque_player2:
                        print("Curacion2")
                        poder_curacion1
                        poder_curacion(pokemon_a_mover)
                        contador_movimientos_player2 += 1
                        lista_pokemones_radio_ataque_player2: False

            if lista_seleccion_radio_pikachu:
                print('RADIO PIKACHU')
            if botones_activo_charmander == True :
                if cursor1.colliderect(charmander_seleccion):
                    print("charmander")
                    boton_charmander_eleccion = True
                    Ubicacion(pokeball1)
                    botones_activo_charmander  = False
            if botones_activo_pikachu == True :
                if cursor1.colliderect(pikachu_eleccion):
                    print("elegir")
                    boton_pikachu_eleccion = True
                    Ubicacion(pokeball1)
                    botones_activo_pikachu = False
            if botones_activo_riulu == True :
                if cursor1.colliderect(riulu_seleccion):
                    print("elegir")
                    boton_riulu_eleccion = True
                    Ubicacion(pokeball1)
                    botones_activo_riulu = False
            if botones_activo_ram == True: 
                if cursor1.colliderect(ram_seleccion):
                    print("elegir")
                    boton_ram_eleccion = True
                    Ubicacion(pokeball1)
                    botones_activo_ram = False                                        
            if botones_activo_lapras == True :
                if cursor1.colliderect(lapras_seleccion):
                    print("elegir")
                    boton_lapras_eleccion = True
                    Ubicacion(pokeball1)
                    botones_activo_lapras = False
            if botones_activo_gengar == True :
                if cursor1.colliderect(gengar_seleccion):
                    print("elegir")
                    boton_gengar_eleccion = True
                    Ubicacion(pokeball1) 
                    botones_activo_gengar = False 
            if seleccion == True :
                #if turno1 == True:    
                Casilla_de_ubicacion(bloque_de_inicio, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio2, pokemon_a_seleccionar) 
                Casilla_de_ubicacion(bloque_de_inicio3, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio4, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio5, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio6, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio7, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio8, pokemon_a_seleccionar)
                
                Casilla_de_ubicacion(bloque_de_inicio11, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio22, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio33, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio44, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio55, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio66, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio77, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio88, pokemon_a_seleccionar)
                
                
                #if turno2 == True:

                Casilla_de_ubicacion(bloque_de_inicio111, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio222, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio333, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio444, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio555, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio666, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio777, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio888, pokemon_a_seleccionar)

                Casilla_de_ubicacion(bloque_de_inicio1111, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio2222, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio3333, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio4444, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio5555, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio6666, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio7777, pokemon_a_seleccionar)
                Casilla_de_ubicacion(bloque_de_inicio8888, pokemon_a_seleccionar)
                contador_eleccion +=1
                boton_pikachu_eleccion = False
                boton_charmander_eleccion = False
                boton_riulu_eleccion = False
                boton_ram_eleccion = False
                boton_lapras_eleccion = False
                boton_gengar_eleccion = False

                seleccion = False
        if evento.type == pygame.MOUSEMOTION:
            if greenboton.seleccion_mouse(pos):
                greenboton.color = Rojo
            else:
                greenboton.color = verde_celeste

        if ubicar: 
            if evento.type == pygame.MOUSEBUTTONDOWN:
                ubicar = False
                print("Click")
   
        #if evento.type == pygame.MOUSEBUTTONDOWN:
        #    if bloque1.radio(pos):
        #        print('pasto')
        if evento.type == pygame.MOUSEMOTION:
            if boton_moverse1.seleccion_mouse(pos):
                boton_moverse1.color = celeste
            else:
                boton_moverse1.color = verde_celeste

            if boton_moverse2.seleccion_mouse(pos):
                boton_moverse2.color = Rojo_brillante
            else:
                boton_moverse2.color = Rojo

            if Boton_Attack1.seleccion_mouse(pos):
                Boton_Attack1.color = celeste
            else:
                Boton_Attack1.color = verde_celeste
          
        if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                pygame.QUIT
                jugando = False
            if moverse1 == True:
                print('mover1 encendido')
                if evento.key == K_LEFT:                       
                    pokemon_a_mover_player1.rect.x = pokemon_a_mover_player1.rect.x - 56
                    #pokemon_a_mover.image = pikachu_izquierda
                    contador_movimientos_player1 += 1
                    #print('derecha')
                if evento.key == K_RIGHT:
                    pokemon_a_mover_player1.rect.x = pokemon_a_mover_player1.rect.x + 56
                    #pokemon_a_mover..image = pikachu_derecha
                    contador_movimientos_player1 += 1
                if evento.key == K_UP:
                    pokemon_a_mover_player1.rect.y = pokemon_a_mover_player1.rect.y - 56
                    #pokemon_a_mover..image = pikachu_arrib
                    contador_movimientos_player1 += 1
                if evento.key == K_DOWN:
                    pokemon_a_mover_player1.rect.y = pokemon_a_mover_player1.rect.y + 56
                    #ikachu.image = pikachu_abajo
                    contador_movimientos_player1 += 1


            if moverse2 == True:
                print('moverse 2 encendido')
                if evento.key == K_LEFT:
                    pokemon_a_mover_player2.rect.x = pokemon_a_mover_player2.rect.x - 56
                    #pokemon_a_mover.image = pikachu_izquierda
                    contador_movimientos_player2 += 1
                if evento.key == K_RIGHT:
                    pokemon_a_mover_player2.rect.x = pokemon_a_mover_player2.rect.x + 56
                    #pokemon_a_mover..image = pikachu_derecha
                    contador_movimientos_player2 += 1
                if evento.key == K_UP:
                    pokemon_a_mover_player2.rect.y = pokemon_a_mover_player2.rect.y - 56
                    #pokemon_a_mover..image = pikachu_arrib
                    contador_movimientos_player2 += 1
                if evento.key == K_DOWN:
                    pokemon_a_mover_player2.rect.y = pokemon_a_mover_player2.rect.y + 56
                    #ikachu.image = pikachu_abajo
                    contador_movimientos_player2 += 1
                
        if evento.type == pygame.QUIT:
            pygame.quit() # quit the screen
            jugando = False
            sys.exit()
    
    #lienzo.fill(negro)
    lienzo.blit(fondo_1,[0,0])
    if texto_activo:
        muestra_texto(lienzo,comicsans, str(pokemon_a_mover.nombre) , blanco, 33,590 , 640)
        muestra_texto(lienzo,comicsans, 'Vida: '+ str(pokemon_a_mover.vida) , blanco, 27,600 , 660)
        muestra_texto(lienzo,comicsans, 'Ataque: '+ str(pokemon_a_mover.ataque) , blanco, 27,600 , 680)
print(lista_pokemones_player1)
print(lista_pokemones_player2)
