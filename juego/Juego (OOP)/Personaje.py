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
                 pygame.image.load("imagenes/Skins/Samus.png"),
                 pygame.image.load("imagenes/Skins/Athena.png"),
                 pygame.image.load("imagenes/Skins/Edzio.png"),
                 pygame.image.load("imagenes/Skins/Kula.png"),
                 pygame.image.load("imagenes/Skins/Rudo.png"),
                 pygame.image.load("imagenes/Skins/Sindel.png"),
                 pygame.image.load("imagenes/Skins/Skarlet.png"),
                 
                 ]
                 
         self.Imagenes_cliente = [
                 pygame.image.load("imagenes/Skins_cliente/Mujer.png"),
                 pygame.image.load("imagenes/Skins_cliente/Mega-man.png"),
                 pygame.image.load("imagenes/Skins_cliente/Goku.png"),
                 pygame.image.load("imagenes/Skins_cliente/Naruto.png"),
                 pygame.image.load("imagenes/Skins_cliente/Luffy.png"), 
                 pygame.image.load("imagenes/Skins_cliente/Alphonse.png"), 
                 pygame.image.load("imagenes/Skins_cliente/Edward.png"), 
                 pygame.image.load("imagenes/Skins_cliente/Charizard.png"), 
                 pygame.image.load("imagenes/Skins_cliente/Dragonite.png"),
                 pygame.image.load("imagenes/Skins_cliente/MasterChief.png"),
                 pygame.image.load("imagenes/Skins_cliente/Linterna-verde.png"),
                 pygame.image.load("imagenes/Skins_cliente/Superman.png"),
                 pygame.image.load("imagenes/Skins_cliente/Batman.png"),
                 pygame.image.load("imagenes/Skins_cliente/Magneto.png"),  
                 pygame.image.load("imagenes/Skins_cliente/Thanos.png"), 
                 pygame.image.load("imagenes/Skins_cliente/Antorcha.png"),  
                 pygame.image.load("imagenes/Skins_cliente/Iron-man.png"),
                 pygame.image.load("imagenes/Skins_cliente/Spider-man.png"),       
                 pygame.image.load("imagenes/Skins_cliente/Thor.png"),
                 pygame.image.load("imagenes/Skins_cliente/Ghost-rider.png"),
                 pygame.image.load("imagenes/Skins_cliente/Capitan-america.png"),
                 pygame.image.load("imagenes/Skins_cliente/Wolverine.png"),
                 pygame.image.load("imagenes/Skins_cliente/Samus.png"),
                 pygame.image.load("imagenes/Skins_cliente/Athena.png"),
                 pygame.image.load("imagenes/Skins_cliente/Edzio.png"),
                 pygame.image.load("imagenes/Skins_cliente/Kula.png"),
                 pygame.image.load("imagenes/Skins_cliente/Rudo.png"),
                 pygame.image.load("imagenes/Skins_cliente/Sindel.png"),
                 pygame.image.load("imagenes/Skins_cliente/Skarlet.png"),
                 
                 ]                 
                 
         self.Imagenes_muestra = [
                          pygame.image.load("imagenes/Skins_muestra/Mujer.png"),
                          pygame.image.load("imagenes/Skins_muestra/Mega-man.png"),
                          pygame.image.load("imagenes/Skins_muestra/Goku.png"),
                          pygame.image.load("imagenes/Skins_muestra/Naruto.png"),
                          pygame.image.load("imagenes/Skins_muestra/Luffy.png"), 
                          pygame.image.load("imagenes/Skins_muestra/Alphonse.png"), 
                          pygame.image.load("imagenes/Skins_muestra/Edward.png"), 
                          pygame.image.load("imagenes/Skins_muestra/Charizard.png"), 
                          pygame.image.load("imagenes/Skins_muestra/Dragonite.png"),
                          pygame.image.load("imagenes/Skins_muestra/MasterChief.png"),
                          pygame.image.load("imagenes/Skins_muestra/Linterna-verde.png"),
                          pygame.image.load("imagenes/Skins_muestra/Superman.png"),
                          pygame.image.load("imagenes/Skins_muestra/Batman.png"),
                          pygame.image.load("imagenes/Skins_muestra/Magneto.png"),  
                          pygame.image.load("imagenes/Skins_muestra/Thanos.png"), 
                          pygame.image.load("imagenes/Skins_muestra/Antorcha.png"),  
                          pygame.image.load("imagenes/Skins_muestra/Iron-man.png"),
                          pygame.image.load("imagenes/Skins_muestra/Spider-man.png"),       
                          pygame.image.load("imagenes/Skins_muestra/Thor.png"),
                          pygame.image.load("imagenes/Skins_muestra/Ghost-rider.png"),
                          pygame.image.load("imagenes/Skins_muestra/Capitan-america.png"),
                          pygame.image.load("imagenes/Skins_muestra/Wolverine.png"),
                          pygame.image.load("imagenes/Skins_muestra/Samus.png"),
                          pygame.image.load("imagenes/Skins_muestra/Athena.png"),
                          pygame.image.load("imagenes/Skins_muestra/Edzio.png"),
                          pygame.image.load("imagenes/Skins_muestra/Kula.png"),
                          pygame.image.load("imagenes/Skins_muestra/Rudo.png"),
                          pygame.image.load("imagenes/Skins_muestra/Sindel.png"),
                          pygame.image.load("imagenes/Skins_muestra/Skarlet.png"),
                          ]        
         self.Balas=[]                
         self.Imagen = self.Imagenes[0]  
         
         self.posx= 0
         self.posy= 0
         self.velocidad = 20
         self.Lista_Disparos = []
         self.vida = 5
         self.rect = self.Imagen.get_rect()
         self.opc = 0
        
 def Movimiento (self,ventana,posx,posy):
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
				  self.Disparo = proyectil("imagenes/Balas/Bala_Heroe.png",18,self.posy,self.posx)
				  self.Lista_Disparos.append(self.Disparo)
				  
		 if event.type == KEYDOWN:
			 if event.key == K_s:
				 self.x= 700
				 while self.x>50:
				  self.Disparo = proyectil("imagenes/Balas/Bala_Heroe.png",20,self.x,self.posx)
				  self.Lista_Disparos.append(self.Disparo)
				  self.x -= 50
					 		  
				 	 

				 
	 
	            
            
            
            
	 		 

			 
			 
		 
					  		   	 
  	
   
                  
		                 
