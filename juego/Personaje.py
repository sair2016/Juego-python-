import sys, pygame
from pygame.locals import *
from random import randint
from Proyectil import *

class Heroe (pygame.sprite.Sprite):
 def __init__ (self):
	
         self.Imagenes = [
                 pygame.image.load("imagenes/Skins/Mujer.png"),
                 pygame.image.load("imagenes/Skins/mega-man.png"),
                 pygame.image.load("imagenes/Skins/Goku.png"),
                 pygame.image.load("imagenes/Skins/naruto.png"),
                 pygame.image.load("imagenes/Skins/luffy.png"),             
                 ]
                        
         self. Imagen = self.Imagenes[0]  
         
         self.posx= 0
         self.posy= 0
         self.velocidad = 20
         self.Lista_Disparos = []
         self.vida = 3
         self.rect = self.Imagen.get_rect()
         self.opc = 0
 def Movimiento (self,Ancho,Largo,ventana,posy,posx):
  self.posy =posy
  self.posx =posx	
  self.rect.left = posx
  self.rect.top = posy
  ventana.blit(self.Imagen,(posx,posy))
  	 
  for event in pygame.event.get():
		 if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
		 elif event.type == MOUSEBUTTONDOWN:
				  self.Disparo = proyectil("imagenes/Balas/Bala_Heroe.png",20,self.posy,self.posx)
				  self.Lista_Disparos.append(self.Disparo)
				 	 
 def Seleccion_imagen(self,ventana):
	 inicio = 0
	 final = 1
 	 for event in pygame.event.get():
		 if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
		 elif event.type == MOUSEBUTTONDOWN:
			 self.posx,self.posy = pygame.mouse.get_pos()
			 if self.posx>(48*inicio) and self.posx<(48*final):
				 inicio = 48*inicio
				 ventana.blit(self.seleccion,(inicio,100))
				 self.Imagen = self.Imagenes[inicio]
			 else:
				 inicio +=1
				 final +=1	
				 
 def continua ():
	 for event in pygame.event.get():
		 if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
		 elif event.type == KEYDOWN:
			 if event.key== K_SPACE:
				 self.opc= 1
				 
			 else:
				 self.opc = 0	 
	 				  
	 
	            
            
            
            
	 		 

			 
			 
		 
					  		   	 
  	
   
                  
		                 
