import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.puntos = 0
		self.vida = 100
		self.estado = "bajando"
		self.imagenes = [util.cargar_imagen('imagenes/Bajando.png'),
						util.cargar_imagen('imagenes/Bajando-2.png'),
						util.cargar_imagen('imagenes/Subiendo.png'),
						util.cargar_imagen('imagenes/Subiendo-2.png'),
						util.cargar_imagen('imagenes/Izquierda.png'),
						util.cargar_imagen('imagenes/Izquierda-2.png'),
						util.cargar_imagen('imagenes/Derecha.png'),
						util.cargar_imagen('imagenes/Derecha-2.png'),]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(200, 10)
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			if teclas[K_LEFT] and self.rect.x>=10 and (self.rect.x-10)%2==0:
				if (self.rect.x-10)%2==0:
				    self.rect.x -= 10
				    self.image = self.imagenes[5]
				else:
					 self.rect.x -= 10
				     
				         
			elif teclas[K_RIGHT] and self.rect.x<=640-self.rect.width:
				 if (self.rect.x+10)%2==0:
				     self.rect.x += 10
				     self.image = self.imagenes[7]
				 else:
					  self.rect.x += 10
				       
				        
			if teclas[K_UP] and self.rect.y>=10:
				 if (self.rect.y-10)%2==0:
				     self.rect.y -= 10
				     self.image = self.imagenes[3]
				 else:
					  self.rect.y -= 10
				      
				
			elif teclas[K_DOWN] and self.rect.y<=480-self.rect.height:
				 if (self.rect.y+10)%2==0:
				     self.rect.y += 10
				     self.image = self.imagenes[1]
				 else:
					  self.rect.y += 10
				      
