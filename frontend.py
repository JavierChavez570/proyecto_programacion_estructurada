# -*- coding: utf-8 -*-
import csv,serial
arduino = serial.Serial('/dev/cu.usbmodem30',9600)
print("""
	  ______________________________________________________														   
														   
	     		 Proyecto Programación Estructurada 	   
		Integrantes: Ing. Juan Manuel Corza Hermosillo     
	                     Ing. Javier Alejandro Chávez Gómez  
	    Proyecto: Brazó robótico con regitro de posiciones  
	   ______________________________________________________
	""")
def enviar_datos(a):
	arduino.write(a)
	if a>=100 and a<=200:
		var= 'base'
	if a>=200 and a<=300:
		var= 'brazo'
	if a>=300 and a<=400:
		var= 'wrist'
	if a>=400 and a<=500:
		var= 'griper'
	print'datos de '+var+' enviados'
	pass
while True:	
	print("Opciones\n1.- Consultar Ult. posic.\n2.- Controlar Brazo")
	seleccion = raw_input()
	valor = int(seleccion)
	if valor == 1:
		#consulta csv ejecutado por backend.py
		with open('save_data.csv') as doc:
			lineas = doc.read().splitlines()[-1]
		print 'Ultima posición: '+lineas
		pass
	if valor == 2:
		row=0
		while row>=1:
			print("Opciones \n 1.- Mover base \n 2.- Mover brazo \n 3.- Mover muñeca \n 4.- Mover Griper")
			value_exec = raw_input()
			eleccion_fases = int(value_exec)
			if eleccion_fases == 1:
				#base movement
				print'A que posición deseas enviar la base\n recuerda, las posiciones van desde -30º a 90º'
				x=0
				while x>=1:
					print'coloca la posicion a mover la base:'
					movimiento = raw_input()
					base_movement = int(movimiento)+100
					convertir_cadena= base_movement
					enviar_datos(convertir_cadena)
					print'deseas moverlo a otra posicion? \n presiona 2 para no, 0 para si'
					respuesta=raw_input()
					x=int(respuesta)
			elif  eleccion_fases == 2:
				#move arm
				print'Coloca la posicion a mover el brazo \n recuerda que las posiciones van desde 0º a 180º'
				y=0
				while y>=1:
					print'coloca la posicion a mover el brazo'
					movimiento_brazo = raw_input()
					arm_movement = int(movimiento_brazo)+200
					convertir_cadena= arm_movement
					enviar_datos(convertir_cadena)
					print'deseas moverlo a otra posición? \n presiona 2 para no 0 para si'
					respuesta=raw_input()
					y=int(respuesta)
			elif  eleccion_fases == 3:
				#move wrist
				print'Coloca la posicion a mover la muñeca del brazo \n recuerda que las posiciones van desde 0º a 180º'
				z=0
				while z>=1:
					print'coloca la posicion a mover el brazo'
					movimiento_muneca = raw_input()
					wrist_movement = int(movimiento_muneca)+300
					convertir_cadena= wrist_movement
					enviar_datos(convertir_cadena)
					print'deseas moverlo a otra posición? \n presiona 2 para no 0 para si'
					respuesta=raw_input()
					z=int(respuesta)
			elif  eleccion_fases == 4:
				#move griper
				print'Coloca la posicion a mover griper del brazo \n recuerda que las posiciones van desde 20º a 75º'
				c=0
				while c>=1:
					print'coloca la posicion a mover griper del brazo'
					movimiento_griper = raw_input()
					griper_movement=int(movimiento_griper)+400
					convertir_cadena= griper_movement
					enviar_datos(convertir_cadena)
					print'deseas moverlo a otra posición? \n presiona 2 para no 0 para si'
					respuesta=raw_input()
					c=int(respuesta)
		pass
else:
	print'Selecciona por lo menos una opcion para ejecutar el programa'



