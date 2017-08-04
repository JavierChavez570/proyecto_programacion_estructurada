# -*- coding: utf-8 -*-
from Tkinter import *
import serial,csv
arduino = serial.Serial('/dev/cu.usbmodem10',9600)
app = Tk()
datos = []
with open('save_data.csv') as doc:
	#consultar los elementos del csv por lineas
	lineas = doc.read().splitlines()[-1]
	#sacarinformación sin titulos
print lineas
def retoro_paro():
	arduino.write(lineas)
	pass
app.mainloop()

