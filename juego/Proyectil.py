import sys, pygame
from pygame.locals import *
from random import randint

class proyectil:
	
	def __init__ (self,nombre_imagen,velocidad,posy,posx):
		
		self.velocidad = velocidad
		self.Imagen = pygame.image.load(nombre_imagen)
		self.posy = posy
		self.posx = posx
		self.rect = self.Imagen.get_rect()
		
	def trayectoria(self,tipo):
		
		if tipo == "negativa":
		   self.posx -= self.velocidad 
		else:
			self.posx+= self.velocidad  
		self.rect.left = self.posx
		self.rect.top = self.posy	
		
	def dibujar (self,ventana):
		ventana.blit(self.Imagen,(self.posx,self.posy))
