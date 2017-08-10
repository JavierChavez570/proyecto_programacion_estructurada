import serial, csv, time
arduino = serial.Serial('/dev/cu.usbmodem21',9600)


while True:	
	time.sleep(1)
	posicionamiento = arduino.readline()
	if posicionamiento >=100 and posicionamiento <=199:	
		archivo = open('save_data.csv','a')	
		doc = csv.writer(archivo)
		identificador_griper = 1;
		posicionamiento_griper = int(posicionamiento)-100;
		escribir_datos = [identificador_griper, posicionamiento_griper] 
		doc.writerow(escribir_datos)
		archivo.close()
		pass
	if posicionamiento >=200 and posicionamiento <=299:
		archivo = open('save_data.csv','a')	
		doc = csv.writer(archivo)
		identificador_brazo = 2;
		posicionamiento_brazo = int(posicionamiento)-200;
		escribir_datos_brazo = [identificador_brazo, posicionamiento_brazo] 
		doc.writerow(escribir_datos_brazo)
		archivo.close()
		pass
	if posicionamiento >=300 and posicionamiento <=400:
		archivo = open('save_data.csv','a')
		doc = csv.writer(archivo)
		identificador_motorpasos = 3
		posicionamiento_motorpasos = int(posicionamiento)-300
		escribir_datos_motor = [identificador_motorpasos,posicionamiento_motorpasos]
		doc.writerow(escribir_datos_motor)
		archivo.close()		
		pass
	
arduino.close()

	
	
