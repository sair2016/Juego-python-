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


#lista Villanos
Villanos = [ Villano("Imagenes/Villanos/pez.png",10,20,"Imagenes/Balas/Bola_de_agua.png","Pez celestial"),
             Villano("Imagenes/Villanos/Roca.png",20,25,"Imagenes/Balas/Roca.png","Golem"),
             Villano("Imagenes/Villanos/Eva_01.png",30,30,"Imagenes/Balas/Rayo.png","Eva 01"),
             Villano("Imagenes/Villanos/Dragon.png",40,35,"Imagenes/Balas/fuego.png","Bowser"),
             ]
#lista fondos             
Fondos = [
         pygame.image.load("Imagenes/Fondos/Mar.jpg"),
         pygame.image.load("Imagenes/Fondos/Bosque.png"),
         pygame.image.load("Imagenes/Fondos/Ciudad.png"),
         pygame.image.load("Imagenes/Fondos/Castillo.jpg"),
         pygame.image.load("Imagenes/Fondos/Fondo.png"),
         ]
           






def impresion_disparo (usuario,tipo):

	 if len(usuario.Lista_Disparos)>0:
			for x in usuario.Lista_Disparos:
				x.trayectoria(tipo)
				x.dibujar(ventana)
				if x.posx < 10 :
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
	 
	
a=0 
x=0
while menu == 0:
	ventana.fill(negro)

 
	texto.pintar_nombres(40,"JUEGO",(255,255,255),300,0,ventana)
	texto.pintar_nombres(40,"Escoja un personaje",(255,255,255),200,50,ventana)
	texto.pintar_nombres(50,"Persione ESPACIO para continuar",(255,255,255),10,500,ventana)
	for n in chica.Imagenes:
          ventana.blit(n,(a,100))
          a +=48
        a=0      
	ventana.blit(cuadro,((x*48),100))
	pygame.display.update()
 	for event in pygame.event.get():
		 if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
		 elif event.type == KEYDOWN:
			 if event.key == K_LEFT and x>0:
				 x -= 1
				 chica.Imagen = chica.Imagenes[x]
			 if event.key == K_RIGHT and x<4:
				 x +=1
				 chica.Imagen = chica.Imagenes[x]
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
	 pygame.display.update()
	 

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
	 Villanos[nivel].disparar(ventana,20)
	 impresion_disparo(Villanos[nivel],"negativa")
	 impresion_disparo(chica,"positiva")
	 nivel = pasar_o_perder(chica,Villanos[nivel],nivel)
	 pygame.display.update()
	 
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
	 pygame.display.update()
	 
Intermedio_de_niveles(negro,texto,nivel,Villanos[nivel],ventana)

while nivel == 3:
	 ventana.blit(Fondos[nivel],(0,0))
	 dibujar_datos(chica,Villanos,negro,nivel,ventana)
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
	 pygame.display.update()
	 

	 	 
	
	 		
	 
	 
	 
	 

