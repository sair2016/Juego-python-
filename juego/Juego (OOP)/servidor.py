import socket
import threading
import socket
import sys, pygame
from pygame.locals import *
from random import randint 
from Personaje import *
from Villano import *
from Proyectil import *
import time
from Texto import *


procesos = list()


s = socket.socket()
s.bind(("localhost", 8888))
s.listen(1) 
sc, addr = s.accept()
puntos=0
  	
   
		

 
def s2(p):
 p=0
 Ancho = 1000 #ancho ventana
 Largo = 700 #largo ventana
 negro = (0,0,0) #color
 blanco = (255,255,255) #color
 pygame.init() # iniciacion 
 ventana = pygame.display.set_mode((Ancho,Largo)) #creacion de ventana
 pygame.display.set_caption("JUEGO") #titulo de la ventana 
 Fondos = [
         pygame.image.load("Imagenes/Fondos/Mar.jpg"),
         pygame.image.load("Imagenes/Fondos/Ciudad.png"),
         pygame.image.load("Imagenes/Fondos/Castillo_bowser.png"),
         pygame.image.load("Imagenes/Fondos/Fondo.png"),
         pygame.image.load("Imagenes/Fondos/Bosque.png"),
         ]
 while True:
	 
	 ventana.blit(Fondos[p],(0,0))
	 time.sleep(0.2)
	 pygame.display.update()
     

d = threading.Thread(target=s2,args=(p,))
procesos.append(d)
d.start()


