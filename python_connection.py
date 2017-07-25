#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial, time, json
from Tkinter import *
app = Tk()
app.title("Control Servo Motor")
app.configure(background="#115d76")
arduino = serial.Serial ('/dev/cu.usbmodem26',9600)


tiempo = Label(app,text="Inicio: %s" % time.ctime())
tiempo.pack(side="top",fill="both",expand=False,padx=4,pady=4)

def servo1_data():
	posicion = arduino.readline()+"\n"
	print posicion
	pass

def servo_lectura():
	archivo = open("guardar_posicion.txt","r+")
	i=0
	while i<=10:
		posicion = arduino.readline()
		archivo.write(posicion)
		print posicion
		i+=1
	archivo.close()
	pass
def ultima_posicion():
	
	while open("guardar_posicion.txt") as c_ar:
		c_ar.readlines()
		x=c_ar.tell()
		pass
	c_ar = open("guardar_posicion.txt","a")
	consul = archivo.read()
	print consul
	archivo.close()
	pass
def prende_led():
	arduino.write(1)
	pass
def mueve_90():
	arduino.write(2)
	pass
def mueve_180():
	arduino.write(3)
	pass
enciende_led = Button(app, text="Prende Led", command=prende_led)
enciende_led.pack()
turn_off_led = Button(app, text="Mueve 90",command=mueve_90)
turn_off_led.pack()
mueve_90_grados = Button(app, text="mueve 180", command=mueve_180)
mueve_90_grados.pack()
muestra = Button(app, text="Consulta", command=servo_lectura)
consulta_posicion=Button(app, text="Utlima Posicion", command=ultima_posicion)
app.geometry("500x200")
app.resizable(width=False, height=False)
consulta_posicion.pack()
muestra.pack()
app.mainloop()
