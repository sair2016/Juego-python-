import sys, pygame
from pygame.locals import *
from random import randint 
from Personaje import *
from Villano import *
from Proyectil import *
import time
from Texto import * 

#Valores globales
Ancho = 1000
Largo = 700
negro = (0,0,0)
blanco = (255,255,255)
pygame.init()
ventana = pygame.display.set_mode((Ancho,Largo))
pygame.display.set_caption("JUEGO")
texto = textos()             
chica = Heroe()
posy,posx=0,0
nivel = 0
menu = 0 
cuadro = pygame.image.load("imagenes/Seleccion.png")
a=0 
x=0
y=100
b=100
c=0
pygame.mixer.music.load("Sonidos/seleccion.mp3")

#matriz imprecion
impresion = [
             
             ]

#lista Villanos
Villanos = [ Villano("Imagenes/Villanos/pez.png",100,5,"Imagenes/Balas/Bola_de_agua.png","Pez celestial"),
             Villano("Imagenes/Villanos/Roca.png",200,3,"Imagenes/Balas/Roca.png","Golem"),
             Villano("Imagenes/Villanos/Eva_01.png",300,6,"Imagenes/Balas/Rayo.png","Eva 01"),
             Villano("Imagenes/Villanos/Dragon.png",400,7,"Imagenes/Balas/fuego.png","Bowser"),
             ]
#lista fondos             
Fondos = [
         pygame.image.load("Imagenes/Fondos/Mar.jpg"),
         pygame.image.load("Imagenes/Fondos/Bosque.png"),
         pygame.image.load("Imagenes/Fondos/Ciudad.png"),
         pygame.image.load("Imagenes/Fondos/Castillo_bowser.png"),
         pygame.image.load("Imagenes/Fondos/Fondo.png"),
         ]
           






def impresion_disparo (usuario,tipo):

	 if len(usuario.Lista_Disparos)>0:
			for x in usuario.Lista_Disparos:
				x.trayectoria(tipo)
				x.dibujar(ventana)
				if x.posx < 10 :
					usuario.Lista_Disparos.remove(x)
					
def eliminar_disparos (usuario):

	 if len(usuario.Lista_Disparos)>0:
			for x in usuario.Lista_Disparos:
			   usuario.Lista_Disparos.remove(x)					

def pierde_vida (Victima,usuario):
	for n in usuario.Lista_Disparos:
		
	   if Victima.rect.colliderect(n.rect):
		Victima.vida -=1
		usuario.Lista_Disparos.remove(n)
		
def pasar_o_perder(heroe,villano,nivel):
	if heroe.vida <= 0:
		nivel -= 1
		return nivel
	elif villano.vida <=0:
		nivel += 1
		return nivel
	else:
		nivel =	nivel
		return nivel
	   			        
def Intermedio_de_niveles(color,texto,nivel,villano,ventana):
	 
    ventana.fill(negro)
    pygame.display.update()
    time.sleep(1)
    texto.pintar_nombres(40,"Nivel "+str(nivel),(255,255,255),300,0,ventana)
    pygame.display.update()
    time.sleep(1)	 
    texto.pintar_nombres(40,"Villano: "+Villanos[nivel].nombre,(255,255,255),200,50,ventana)
    pygame.display.update()
    time.sleep(2)
	 	            			
def dibujar_datos(heroe,villano,color,nivel,ventana):
	 texto.pintar_nombres(30,"Nivel "+str(nivel),color,350,0,ventana)
	 texto.pintar_nombres(30,"Heroe: Chica",color,0,0,ventana)
	 texto.pintar_nombres(30,"Vida: " + str(heroe.vida) ,color,0,21,ventana)
	 texto.pintar_nombres(30,"Villano:" + villano[nivel].nombre,color,600,0,ventana)
	 texto.pintar_nombres(30,"Vida: " + str(villano[nivel].vida) ,color,600,21,ventana)
	 
def choque_balas (usuario, victima):
    for n in usuario.Lista_Disparos:
        for m in victima.Lista_Disparos:
			if n.rect.colliderect(m.rect):
				usuario.Lista_Disparos.remove(n)
				victima.Lista_Disparos.remove(m)
				
def Toca_villano(usuario, Victima):
	if 	Victima.rect.colliderect(usuario.rect):
		Victima.vida = 0			
           
def game_over (nivel,texto,ventana):
	if nivel <=0:
		ventana.fill(negro)
		texto.pintar_nombres(40,"GAME OVER",(255,255,255),300,0,ventana)
		pygame.display.update()
		time.sleep(5)
		sys.exit()
		
			

while menu == 0:
	ventana.fill(negro)
	print a
	print b

 
	texto.pintar_nombres(40,"JUEGO",(255,255,255),300,0,ventana)
	texto.pintar_nombres(40,"Escoja un personaje",(255,255,255),200,50,ventana)
	texto.pintar_nombres(50,"Persione ESPACIO para continuar",(255,255,255),10,500,ventana)

	for n in chica.Imagenes:
          ventana.blit(n,(x*55,y))
          x +=1
          if x>9:
			  y +=55
			  x=0
	
	x = 0
	y = 100	
  
	ventana.blit(cuadro,((a*55),b))
	ventana.blit(pygame.transform.rotozoom(chica.Imagen, 0, 3),(600,200))
	pygame.display.update()
 	for event in pygame.event.get():
		 if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
		 elif event.type == KEYDOWN:
			 if event.key == K_LEFT and a>0:
				 a -= 1
				 chica.Imagen = chica.Imagenes[a+c]
				 pygame.mixer.music.play()
			 if event.key == K_RIGHT and a<11:
				 a +=1
				 chica.Imagen = chica.Imagenes[a+c]
				 pygame.mixer.music.play()
			 if event.key == K_DOWN:
				 c +=10

				 b +=55
				 pygame.mixer.music.play
				 chica.Imagen = chica.Imagenes[a+c]
				 
			 if event.key == K_UP:
				 c -=10
				 b -=55 
				 chica.Imagen = chica.Imagenes[a+c] 
				 pygame.mixer.music.play				 	  	 
			 if event.key == K_SPACE:
				 menu = 1
				 
				 
			 
					 	 
		 
	 	
		
pygame.mouse.set_visible(False)	
		

while nivel== 0 :
	 ventana.blit(Fondos[nivel],(0,0))
	 dibujar_datos(chica,Villanos,negro,nivel,ventana)
	 chica.Movimiento(Ancho,Largo,ventana,posy,posx)
	 posx,posy = pygame.mouse.get_pos()
	 posy = posy-29
	 posx = posx-29
	 pierde_vida(chica,Villanos[nivel])
	 pierde_vida(Villanos[nivel],chica)
	 Villanos[nivel].movimiento(ventana,Largo)
	 Villanos[nivel].disparar(ventana,25)
	 impresion_disparo(Villanos[nivel],"negativa")
	 impresion_disparo(chica,"positiva")
	 nivel = pasar_o_perder(chica,Villanos[nivel],nivel)
	 choque_balas(chica,Villanos[nivel])
	 Toca_villano(Villanos[nivel],chica)
	 pygame.display.update()
	 
game_over (nivel,texto,ventana)	 	 
eliminar_disparos(chica)
eliminar_disparos(Villanos[nivel-1])
Intermedio_de_niveles(negro,texto,nivel,Villanos[nivel],ventana)		 
	 
while nivel == 1:

	 ventana.blit(Fondos[nivel],(0,0))
	 dibujar_datos(chica,Villanos,negro,nivel,ventana)
	 chica.Movimiento(Ancho,Largo,ventana,posy,posx)
	 posx,posy = pygame.mouse.get_pos()
	 posy = posy-29
	 posx = posx-29
	 pierde_vida(chica,Villanos[nivel])
	 pierde_vida(Villanos[nivel],chica)
	 Villanos[nivel].movimiento(ventana,Largo)
	 Villanos[nivel].disparar(ventana,30)
	 impresion_disparo(Villanos[nivel],"negativa")
	 impresion_disparo(chica,"positiva")
	 nivel = pasar_o_perder(chica,Villanos[nivel],nivel)
	 choque_balas(chica,Villanos[nivel])
	 Toca_villano(Villanos[nivel],chica)
	 pygame.display.update()

game_over (nivel,texto,ventana)	 
eliminar_disparos(chica)
eliminar_disparos(Villanos[nivel-1])	 
Intermedio_de_niveles(negro,texto,nivel,Villanos[nivel],ventana)

while nivel == 2:
	 ventana.blit(Fondos[nivel],(0,0))
	 dibujar_datos(chica,Villanos,blanco,nivel,ventana)
	 chica.Movimiento(Ancho,Largo,ventana,posy,posx)
	 posx,posy = pygame.mouse.get_pos()
	 posy = posy-29
	 posx = posx-29
	 pierde_vida(chica,Villanos[nivel])
	 pierde_vida(Villanos[nivel],chica)
	 Villanos[nivel].movimiento(ventana,Largo)
	 Villanos[nivel].disparar(ventana,10)
	 impresion_disparo(Villanos[nivel],"negativa")
	 impresion_disparo(chica,"positiva")
	 nivel = pasar_o_perder(chica,Villanos[nivel],nivel)
	 choque_balas(chica,Villanos[nivel])
	 Toca_villano(Villanos[nivel],chica)
	 pygame.display.update()

game_over (nivel,texto,ventana)
eliminar_disparos(chica)
eliminar_disparos(Villanos[nivel-1])	 
Intermedio_de_niveles(negro,texto,nivel,Villanos[nivel],ventana)

while nivel == 3:
	 ventana.blit(Fondos[nivel],(0,0))
	 dibujar_datos(chica,Villanos,(255,255,255),nivel,ventana)
	 chica.Movimiento(Ancho,Largo,ventana,posy,posx)
	 posx,posy = pygame.mouse.get_pos()
	 posy = posy-29
	 posx = posx-29
	 pierde_vida(chica,Villanos[nivel])
	 pierde_vida(Villanos[nivel],chica)
	 Villanos[nivel].movimiento(ventana,Largo)
	 Villanos[nivel].disparar(ventana,2)
	 impresion_disparo(Villanos[nivel],"negativa")
	 impresion_disparo(chica,"positiva")
	 nivel = pasar_o_perder(chica,Villanos[nivel],nivel)
	 choque_balas(chica,Villanos[nivel])
	 Toca_villano(Villanos[nivel],chica)
	 pygame.display.update()
	 
game_over (nivel,texto,ventana)	 
	 
	 
	 

