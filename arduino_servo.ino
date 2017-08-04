#include <Stepper.h>
#include <Servo.h>

Servo servo;
void setup() {
        Serial.begin(9600); 
        servo.attach(9);
}

void loop() { 
  if(!Serial.available()){
    //ejecucion primer agarre de caja
        int ejecucion_griper_base = 90;
        int envio_griper = ejecucion_griper_base+100;
        Serial.println(envio_griper,DEC);
        servo.write(ejecucion_griper_base);// posicion de agarre de griper
        delay(1000);        
        //para enviar con un identificador el numero del griper lo enviaremos sumado por 100 
        //para tener por entendido que el el numero 100 es id y el numero restante es la posicion
        int ejecucion_brazo_base = 30;
        int envio_brazo = ejecucion_brazo_base+200;
        Serial.println(envio_brazo);
    }else{
      int lectura_datos = Serial.read();
      }    
}
