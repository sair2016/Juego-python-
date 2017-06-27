import sys, pygame
from pygame.locals import *
from random import randint
from Proyectil import *

class Villano (pygame.sprite.Sprite):
	def __init__ (self,nombre_imagen,vida,velocidad,Imagen_proyectil,nombre):
		
		self.vida= vida
		self.Imagen = pygame.image.load(nombre_imagen)
		self.posx = 800
		self.posy = 100
		self.estado = "bajando"
		self.velocidad = velocidad
		self.rect = self.Imagen.get_rect()
		self.Lista_Disparos = []
		self.Imagen_Disparo = Imagen_proyectil
		self.nombre = nombre
		
		
	def movimiento (self, ventana, Alto):
		
		ventana.blit(self.Imagen,(self.posx,self.posy)) 
		
		if self.estado == "bajando" and self.posy >= (Alto-100):	
			 self.estado = "subiendo" 
		elif self.estado == "subiendo" and self.posy <= 100: 	 
			 self.estado="bajando"
			 
		if self.estado == "bajando":
			self.posy += self.velocidad
		else: 	self.posy -= self.velocidad
		self.rect.left = self.posx
		self.rect.top = self.posy 
	def disparar (self,ventana,n):
		
	   y =randint(0,100)
	   if y%n == 0:    	
		 self.Disparo = proyectil(self.Imagen_Disparo,5,self.posy,self.posx)	
		 self.Lista_Disparos.append(self.Disparo)
		 
				
		
	
		
		
	    
	    
	   	
		
			 
		

	    	
		
