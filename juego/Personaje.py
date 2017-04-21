import sys, pygame
from pygame.locals import *
from random import randint
from Proyectil import *

class Heroe (pygame.sprite.Sprite):
 def __init__ (self):
	
         self.Imagenes = [
                 pygame.image.load("imagenes/Skins/Mujer.png"),
                 pygame.image.load("imagenes/Skins/Mega-man.png"),
                 pygame.image.load("imagenes/Skins/Goku.png"),
                 pygame.image.load("imagenes/Skins/Naruto.png"),
                 pygame.image.load("imagenes/Skins/Luffy.png"), 
                 pygame.image.load("imagenes/Skins/Alphonse.png"), 
                 pygame.image.load("imagenes/Skins/Edward.png"), 
                 pygame.image.load("imagenes/Skins/Charizard.png"), 
                 pygame.image.load("imagenes/Skins/Dragonite.png"),
                 pygame.image.load("imagenes/Skins/MasterChief.png"),
                 pygame.image.load("imagenes/Skins/Linterna-verde.png"),
                 pygame.image.load("imagenes/Skins/Superman.png"),
                 pygame.image.load("imagenes/Skins/Batman.png"),
                 pygame.image.load("imagenes/Skins/Magneto.png"),  
                 pygame.image.load("imagenes/Skins/Thanos.png"), 
                 pygame.image.load("imagenes/Skins/Antorcha.png"),  
                 pygame.image.load("imagenes/Skins/Iron-man.png"),
                 pygame.image.load("imagenes/Skins/Spider-man.png"),       
                 pygame.image.load("imagenes/Skins/Thor.png"),
                 pygame.image.load("imagenes/Skins/Ghost-rider.png"),
                 pygame.image.load("imagenes/Skins/Capitan-america.png"),
                 pygame.image.load("imagenes/Skins/Wolverine.png"),
                 
                 ]
                 
         self.Imagenes_muestra = [
                          pygame.image.load("imagenes/Skins_muestra/Mujer.png"),
                          pygame.image.load("imagenes/Skins_muestra/Mega-man.png"),
                          pygame.image.load("imagenes/Skins_muestra/Goku.jpeg"),
                          pygame.image.load("imagenes/Skins_muestra/Naruto.png"),
                          pygame.image.load("imagenes/Skins_muestra/Luffy.png"), 
                          pygame.image.load("imagenes/Skins_muestra/Alphonse.png"), 
                          pygame.image.load("imagenes/Skins_muestra/Edward.png"), 
                          pygame.image.load("imagenes/Skins_muestra/Charizard.png"), 
                          pygame.image.load("imagenes/Skins_muestra/Dragonite.png"),
                          pygame.image.load("imagenes/Skins_muestra/MasterChief.jpeg"),
                          pygame.image.load("imagenes/Skins_muestra/Linterna-verde.png"),
                          pygame.image.load("imagenes/Skins_muestra/Superman.png"),
                          pygame.image.load("imagenes/Skins_muestra/Batman.png"),
                          pygame.image.load("imagenes/Skins_muestra/Magneto.png"),  
                          pygame.image.load("imagenes/Skins_muestra/Thanos.jpeg"), 
                          pygame.image.load("imagenes/Skins_muestra/Antorcha.png"),  
                          pygame.image.load("imagenes/Skins_muestra/Iron-man.png"),
                          pygame.image.load("imagenes/Skins_muestra/Spider-man.png"),       
                          pygame.image.load("imagenes/Skins_muestra/Thor.png"),
                          pygame.image.load("imagenes/Skins_muestra/Ghost-rider.png"),
                          pygame.image.load("imagenes/Skins_muestra/Capitan-america.png"),
                          pygame.image.load("imagenes/Skins_muestra/Wolverine.png"),
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
	 				  
	 
	            
            
            
            
	 		 

			 
			 
		 
					  		   	 
  	
   
                  
		                 
