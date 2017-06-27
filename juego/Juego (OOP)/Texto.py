import sys, pygame
from pygame.locals import *
from random import randint

class textos:
	def __init__(self):
		self.nivel= "Nivel"
		self.vida = "Vida"
		
	def pintar_nombres(self,numero,texto,color,x,y,ventana):
		self.mifuente =pygame.font.Font("3Dventure.ttf",numero)
		self.mitexto = self.mifuente.render(texto,0,color)
		ventana.blit(self.mitexto,(x,y))
		
			
		
