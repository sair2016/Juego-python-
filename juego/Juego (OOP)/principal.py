import sys, pygame
from pygame.locals import *
from random import randint 
from Personaje import *
from Villano import *
from Proyectil import *
import time
from Texto import * 
import socket
import threading

 
pygame.init() # iniciacion 
procesos = list()
Flechax,Flechay=0,0
texto = textos() 
Ancho = 1000 #ancho ventana
Largo = 700 #largo ventana	
ventana = pygame.display.set_mode((Ancho,Largo)) #creacion de ventana
pygame.display.set_caption("SHALOWGAME") #titulo de la ventana

Fondos = [
         pygame.image.load("Imagenes/Fondos/Mar.jpg"),
         pygame.image.load("Imagenes/Fondos/Ciudad.png"),
         pygame.image.load("Imagenes/Fondos/Castillo_bowser.png"),
         pygame.image.load("Imagenes/Fondos/Fondo.png"),
         pygame.image.load("Imagenes/Fondos/Bosque.png"),
         ]
         
sonidos=[
          pygame.mixer.Sound("Sonidos/seleccion2.wav"),
          pygame.mixer.Sound("Sonidos/Goku.wav"),
          pygame.mixer.Sound("Sonidos/Naruto.wav"),
          pygame.mixer.Sound("Sonidos/Mega-man.wav"),
          pygame.mixer.Sound("Sonidos/Megalovania.wav"), 
          pygame.mixer.Sound("Sonidos/Feel_Good.wav"), 

        ]

heroe = Heroe()
   
def Ecoger_personaje(ventana,texto,chica,sonido):
	
  
  menu = 1 
  cuadro =  pygame.image.load("imagenes/Seleccion.png")	
  a=0 #cuadro seleccion coordenada x 
  x=0 #imagenes coordenada x
  y=100#imagenes coordenada y
  b=100#cuadro seleccion coordenada y
  c=0 # cuadro seleccion suma en y 
  	
  while menu == 1:
	 ventana.fill((0,0,0))
	 texto.pintar_nombres(40,"JUEGO",(255,255,255),300,0,ventana)
	 texto.pintar_nombres(40,"Escoja un personaje",(255,255,255),200,50,ventana)
	 texto.pintar_nombres(50,"Persione ESPACIO para continuar",(255,255,255),10,500,ventana)
         ventana.blit(cuadro,((a*55),b))
	 for n in chica.Imagenes:
           ventana.blit(n,(x*55,y))
           x +=1
           if x>9:
			   y +=55
			   x=0
	
	 x = 0
	 y = 100	
	
	 ventana.blit(chica.Imagenes_muestra[a+c],(600,100))
	 pygame.display.update()
 	 for event in pygame.event.get():
		  if event.type == QUIT:
			  pygame.quit()
			  sys.exit()
		  elif event.type == KEYDOWN:
			  if event.key == K_LEFT and a>0:
				  a -= 1
				  sonido[0].play()
				  ventana.blit(chica.Imagenes_muestra[a+c],(600,100))
			  if event.key == K_RIGHT and a<9:
				  a +=1
				  sonido[0].play()
				  ventana.blit(chica.Imagenes_muestra[a+c],(600,100))
			  if event.key == K_DOWN and c<20:
				  c +=10

				  b +=55
				  sonido[0].play()
				  ventana.blit(chica.Imagenes_muestra[a+c],(600,100))
				 
			  if event.key == K_UP and c>0:
				  c -=10
				  b -=55  
				  sonido[0].play()
				  ventana.blit(chica.Imagenes_muestra[a+c],(600,00))				 	  	 
			  if event.key == K_SPACE:
				  sonido[1].play()
				  menu = 2	      
  return (a+c)

def impresion_disparo (usuario,tipo):
 
	 if len(usuario.Lista_Disparos)>0:
			for x in usuario.Lista_Disparos:
				x.trayectoria(tipo)
				x.dibujar(ventana)
				if x.posx < 10 or x.posx>990 :
					usuario.Lista_Disparos.remove(x)
				
def Disparo_conexion (Lista,heroe):
	if Lista[2]!=" ":
		heroe.Disparo = proyectil("imagenes/Balas/Bala_Heroe.png",18,int (Lista[2]),int(Lista[3]))
	        heroe.Lista_Disparos.append(heroe.Disparo) 
				
def Movimiento (usuario,ventana,posx,posy):
  usuario.posy =posy
  usuario.posx =posx	
  usuario.rect.left = posx
  usuario.rect.top = posy
  ventana.blit(usuario.Imagen,(posx,posy))
  envio=" " 	 
  for event in pygame.event.get():
		 if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
		 elif event.type == MOUSEBUTTONDOWN:
				  usuario.Disparo = proyectil("imagenes/Balas/Bala_Heroe.png",18,usuario.posy,usuario.posx)
				  usuario.Lista_Disparos.append(usuario.Disparo)
				  envio= str(usuario.posy)+","+str(usuario.posx)
  return envio

def Envio_disparo (x):
 
	 for event in pygame.event.get():
          if event.type == MOUSEBUTTONDOWN:
				return str(x.posx)+","+str(x.posy)
	 else:
		 return " " 				
	   	     
					
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
	   			        
def Intermedio_de_niveles(color,texto,nivel,Villanos,ventana):
	 
    ventana.fill(color)
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

def dibujar_datos_conexion(heroe,villano,color,ventana):
	 texto.pintar_nombres(30,"Player 1",color,0,0,ventana)
	 texto.pintar_nombres(30,"Vida: " + str(heroe.vida) ,color,0,21,ventana)
	 texto.pintar_nombres(30,"Player 2",color,600,0,ventana)
	 texto.pintar_nombres(30,"Vida: " + str(villano.vida) ,color,600,21,ventana)
	 
	 
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
		ventana.fill((0,0,0))
		texto.pintar_nombres(40,"GAME OVER",(255,255,255),300,0,ventana)
		pygame.display.update()
		time.sleep(2)
		sys.exit()          

def salida():
	for event in pygame.event.get():
	      if event.type == QUIT:
     		     pygame.quit()
     		     sys.exit()           

def game(ventana):
 #Valores globales

 negro = (0,0,0) #color
 blanco = (255,255,255) #color
 pygame.init() # iniciacion 
 
 texto = textos()  #clase texto (maneja todo lo que tiene que ver con textos en el juego)           
 chica = Heroe() 
 posy,posx=0,0
 nivel = 0
 menu = 1 
 cuadro =  pygame.image.load("imagenes/Seleccion.png")
         
 sonido=[
          pygame.mixer.Sound("Sonidos/seleccion2.wav"),
          pygame.mixer.Sound("Sonidos/Goku.wav"),
          pygame.mixer.Sound("Sonidos/Naruto.wav"),
          pygame.mixer.Sound("Sonidos/Mega-man.wav"),
          pygame.mixer.Sound("Sonidos/Megalovania.wav"), 
        ]


 #lista Villanos
 Villanos = [ Villano("Imagenes/Villanos/pez.png",100,9,"Imagenes/Balas/Bola_de_agua.png","Pez celestial"),
             Villano("Imagenes/Villanos/Eva_01.png",300,9,"Imagenes/Balas/Rayo.png","Eva 01"),
             Villano("Imagenes/Villanos/Dragon.png",400,9,"Imagenes/Balas/fuego.png","Bowser"),
             Villano("Imagenes/Villanos/Roca.png",200,9,"Imagenes/Balas/Roca.png","Golem"),
             ]
 #lista fondos             
 Fondos = [
         pygame.image.load("Imagenes/Fondos/Mar.jpg"),
         pygame.image.load("Imagenes/Fondos/Ciudad.png"),
         pygame.image.load("Imagenes/Fondos/Castillo_bowser.png"),
         pygame.image.load("Imagenes/Fondos/Fondo.png"),
         pygame.image.load("Imagenes/Fondos/Bosque.png"),
         ]
           




 

 while menu !=4:
		
			
  a=0 #cuadro seleccion coordenada x 
  x=0 #imagenes coordenada x
  y=100#imagenes coordenada y
  b=100#cuadro seleccion coordenada y
  c=0 # cuadro seleccion suma en y 

  while menu == 1:
	 ventana.fill(negro)
	 texto.pintar_nombres(40,"JUEGO",(255,255,255),300,0,ventana)
	 texto.pintar_nombres(40,"Escoja un personaje",(255,255,255),200,50,ventana)
	 texto.pintar_nombres(50,"Persione ESPACIO para continuar",(255,255,255),10,500,ventana)
         ventana.blit(cuadro,((a*55),b))
	 for n in chica.Imagenes:
           ventana.blit(n,(x*55,y))
           x +=1
           if x>9:
			   y +=55
			   x=0
	
	 x = 0
	 y = 100	
	
	 ventana.blit(chica.Imagenes_muestra[a+c],(600,100))
	 pygame.display.update()
 	 for event in pygame.event.get():
		  if event.type == QUIT:
			  pygame.quit()
			  sys.exit()
		  elif event.type == KEYDOWN:
			  if event.key == K_LEFT and a>0:
				  a -= 1
				  chica.Imagen = chica.Imagenes[a+c]
				  sonido[0].play()
				  ventana.blit(chica.Imagenes_muestra[a+c],(600,100))
			  if event.key == K_RIGHT and a<9:
				  a +=1
				  chica.Imagen = chica.Imagenes[a+c]
				  sonido[0].play()
				  ventana.blit(chica.Imagenes_muestra[a+c],(600,100))
			  if event.key == K_DOWN and c<20:
				  c +=10

				  b +=55
				  sonido[0].play()
				  chica.Imagen = chica.Imagenes[a+c]
				  ventana.blit(chica.Imagenes_muestra[a+c],(600,100))
				 
			  if event.key == K_UP and c>0:
				  c -=10
				  b -=55 
				  chica.Imagen = chica.Imagenes[a+c] 
				  sonido[0].play()
				  ventana.blit(chica.Imagenes_muestra[a+c],(600,00))				 	  	 
			  if event.key == K_SPACE:
				  sonido[1].play()
				  menu = 2
				   
  # variables flecha
  Flechax =0
  Flechay =550
 			 
  while menu == 2:
	 ventana.fill(negro)
	 texto.pintar_nombres(40,"JUEGO",(255,255,255),300,0,ventana)
	 texto.pintar_nombres(40,"Escoja un personaje",(255,255,255),200,50,ventana)
	 texto.pintar_nombres(50,"Persione ESPACIO para continuar",(255,255,255),10,500,ventana)
         ventana.blit(cuadro,((a*55),b))
	 for n in chica.Imagenes:
           ventana.blit(n,(x*55,y))
           x +=1
           if x>9:
			   y +=55
			   x=0	
	 x = 0
	 y = 100	
	 texto.pintar_nombres(50,"Jugar",(255,255,255),50,550,ventana)
	 texto.pintar_nombres(50,"Volver",(255,255,255),50,600,ventana)
	 ventana.blit(chica.Imagenes_muestra[a+c],(600,100))
	 ventana.blit(pygame.image.load("Imagenes/mano.png"),(Flechax,Flechay))
	 pygame.display.update()
 	 for event in pygame.event.get():
 		 if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
		 elif event.type == KEYDOWN:
			 if event.key == K_DOWN and Flechay != 600:
				 Flechay += 50
			 if event.key == K_UP and Flechay != 550 :
				 Flechay -=50	  	 
			 if event.key == K_SPACE:
				 if Flechay == 550:
					 menu =4
				 if Flechay ==600:
					 sonido[3].play(2)
					 menu = 1
                     
			 
			         
					 	 
		 
	 	
		
 pygame.mouse.set_visible(False)	
		

 while nivel== 0 :
	  ventana.blit(Fondos[nivel],(0,0))
	  dibujar_datos(chica,Villanos,negro,nivel,ventana)
	  chica.Movimiento(ventana,posx,posy)
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
 Intermedio_de_niveles(negro,texto,nivel,Villanos,ventana)		 
	 
 while nivel == 1:

	  ventana.blit(Fondos[nivel],(0,0))
	  dibujar_datos(chica,Villanos,blanco,nivel,ventana)
	  chica.Movimiento(ventana,posx,posy)
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
 Intermedio_de_niveles(negro,texto,nivel,Villanos,ventana)

 while nivel == 2:
	  ventana.blit(Fondos[nivel],(0,0))
	  dibujar_datos(chica,Villanos,blanco,nivel,ventana)
	  chica.Movimiento(ventana,posx,posy)
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
 Intermedio_de_niveles(negro,texto,nivel,Villanos,ventana)

 while nivel == 3:
	  ventana.blit(Fondos[nivel],(0,0))
	  dibujar_datos(chica,Villanos,(255,255,255),nivel,ventana)
	  chica.Movimiento(ventana,posx,posy)
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
 menu = 1	 

def cliente(ventana,skinp):
	
	opc=True
	heroe_servidor = Heroe()
	heroe_servidor.vida=5    
	s=socket.socket()
	s.connect(("localhost",8888))
	c="3,"+str(skinp)+",100"
	s.send(c)
	c=s.recv(1024)
	fondo,skin,vida = c.split(",")
	Lista=list()
	posx,posy=0,0
	posxE,posyE=0,0
	heroe_servidor.Imagen = heroe_servidor.Imagenes[int(skin)]
	heroe.Imagen = heroe.Imagenes_cliente[int(skinp)]
	sonidos[4].play()
        while opc==True:	   
	     try:
	      ventana.blit(Fondos[int(fondo)],(0,0))
	      dibujar_datos_conexion(heroe_servidor,heroe,(255,255,255),ventana)
	      posxE,posyE= pygame.mouse.get_pos()
	      mensaje= str(posxE)+","+str(posyE)+","+Movimiento(heroe,ventana,(posxE-24),(posyE-24))
	      Movimiento(heroe,ventana,(posxE-24),(posyE-24))
	      heroe_servidor.Movimiento(ventana,(int(posx)-24),(int(posy)-24))	     
	      Envio_disparo(heroe)
	      s.send(mensaje)	     
	      x = s.recv(1024)
	      print x
	      Lista=x.split(",")
	      Disparo_conexion(Lista, heroe_servidor)
	      posx,posy = Lista[0],Lista[1]
	      salida()
	      impresion_disparo(heroe_servidor,"positiva")
	      impresion_disparo(heroe,"negativa")
	      choque_balas(heroe,heroe_servidor)
	      pierde_vida(heroe_servidor,heroe)
	      pierde_vida(heroe,heroe_servidor)
	      pygame.display.update()
	      if heroe.vida==0 or heroe_servidor.vida == 0:
			s.close
			opc= False
             except:
			  opc=False
     
    



 	    	  		             
def servidor (ventana,skinp):
   
   
   heroe.vida=5
   
   opc = True	 
   Lista = list()
   heroe_cliente = Heroe()
   heroe_cliente.vida=5
   s = socket.socket()
   s.bind(("localhost", 8888))
   s.listen(1) 
   sc, addr = s.accept()
   x=sc.recv(1024)
   posy,posx=0,0
   fondo,skin,vida = x.split(',')
   mensaje = "3,"+str(skinp)+",100"
   sc.send(mensaje)
   posxE,posyE=0,0
   heroe_cliente.Imagen = heroe_cliente.Imagenes_cliente[int(skin)]
   heroe.Imagen = heroe.Imagenes[skinp]
   sonidos[4].play()
   while opc==True:	   
	    try:
	     ventana.blit(Fondos[int(fondo)],(0,0))
	     dibujar_datos_conexion(heroe,heroe_cliente,(255,255,255),ventana)
	     posxE,posyE= pygame.mouse.get_pos()
	     mensaje= str(posxE)+","+str(posyE)+","+Movimiento(heroe,ventana,(posxE-24),(posyE-24))
	     heroe_cliente.Movimiento(ventana,(int(posx)-24),(int(posy)-24))
	     sc.send(mensaje)	    
	     x = sc.recv(1024)
	     print x
	     Lista=x.split(",")
	     posx,posy = Lista[0],Lista[1]
	     salida()
	     Disparo_conexion(Lista,heroe_cliente)
	     impresion_disparo(heroe_cliente,"negativa")
	     impresion_disparo(heroe,"positiva")
	     choque_balas(heroe,heroe_cliente)
	     pierde_vida(heroe_cliente,heroe)
	     pierde_vida(heroe,heroe_cliente)	    
	     pygame.display.update()
	     if heroe.vida==0 or heroe_cliente.vida == 0:	
			 sc.close
			 opc= False
            except:
			   opc=False	 
		 
			
			   
			   
			   
		







sonidos[5].play()



seleccion =	True



while True:
 while seleccion==True:
	
    ventana.fill((0,0,0))
    texto.pintar_nombres(50,"JUGAR",(255,255,255),50,0,ventana)
    texto.pintar_nombres(50,"CONEXION",(255,255,255),50,50,ventana)
    texto.pintar_nombres(50,"SALIR",(255,255,255),50,100,ventana)
    ventana.blit(pygame.image.load("Imagenes/mano.png"),(Flechax,Flechay))
    pygame.display.update()
    print str(heroe.vida)

    for event in pygame.event.get():
	
 		 if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
		 elif event.type == KEYDOWN:
			 if event.key == K_DOWN and Flechay != 100:
				 Flechay += 50
			 if event.key == K_UP and Flechay != 0 :
				 Flechay -=50	  	 
			 if event.key == K_SPACE:
				 seleccion=False
 
 if Flechay == 0:

	game(ventana)
	seleccion=True 
	
 if Flechay == 50:
	
  seleccion = True	
     
  while seleccion == True:
	
	
    ventana.fill((0,0,0))
    texto.pintar_nombres(50,"CREAR PARTIDA",(255,255,255),50,0,ventana)
    texto.pintar_nombres(50,"BUSCAR PARTIDA",(255,255,255),50,50,ventana)
    ventana.blit(pygame.image.load("Imagenes/mano.png"),(Flechax,Flechay))
    pygame.display.update()
    
    for event in pygame.event.get():
	
 		 if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
		 elif event.type == KEYDOWN:
			 if event.key == K_DOWN and Flechay != 50:
				 Flechay += 50
			 if event.key == K_UP and Flechay != 0 :
				 Flechay -=50	  	 
			 if event.key == K_SPACE:
				 seleccion = False


 if Flechay == 0:
	sonidos[5].stop() 
	skin=Ecoger_personaje(ventana,texto,heroe,sonidos) 
	servidor(ventana,skin)
	seleccion=True 
	ventana.fill((0,0,0))

	if heroe.vida > 0:
		texto.pintar_nombres(50,"Ganador: player 1 ",(255,255,255),50,0,ventana)
	else:
		texto.pintar_nombres(50,"Ganador: player 2 ",(255,255,255),50,0,ventana)		        
                
 if Flechay == 50:
	 
	sonidos[5].stop()
	skin=Ecoger_personaje(ventana,texto,heroe,sonidos) 
	cliente(ventana,skin)
	seleccion=True
	ventana.fill((0,0,0))
	if heroe.vida > 0:
		texto.pintar_nombres(50,"Ganador: player 2 ",(255,255,255),50,0,ventana)
	else:
		texto.pintar_nombres(50,"Ganador: player 1 ",(255,255,255),50,0,ventana)		        
    
 pygame.display.update()
 sonidos[4].stop()
 heroe.vida = 5
 time.sleep(5)     
    
	 				
				
				 

