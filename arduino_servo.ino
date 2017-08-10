#include <Stepper.h>

#include <Servo.h>

Servo griper;
Servo wrist;
Servo arm;
Stepper stepper(96, 4, 7, 8, 12);
void setup() {
        Serial.begin(9600);
        griper.attach(11);
        wrist.attach(10);
        arm.attach(9); 
        wrist.write(0);
        arm.write(0); 
        stepper.setSpeed(20);
}

void loop() { 
  if(!Serial.available()){
    //movimento arm
    
    for(int brazo = 0; brazo<=42; brazo++){
      arm.write(brazo);
      delay(50);
      }

    //movimiento wrist
    
    for(int muneca = 40; muneca<=60; muneca++){
      wrist.write(muneca);
      delay(50);
      if(muneca==60){delay(800);}
      }    
    
    //movimiento griper
     for(int gri = 0; gri<=100; gri+=2){
        griper.write(gri);
        delay(50);
          if (gri == 100){delay(800);}
      }
     //-------------------sube
      //movimento arm
    
    for(int brazo; brazo>=-42; brazo--){
      arm.write(brazo);
      delay(50);
      }

    //movimiento wrist
    
    for(int muneca = 40; muneca<=60; muneca++){
      wrist.write(muneca);
      delay(50);
      if(muneca==60){delay(800);}
      }    
    //movimiento de la base
    stepper.step(-30);
    //movimiento griper
     for(int gri = 0; gri<=100; gri+=2){
        griper.write(gri);
        delay(50);
          if (gri == 100){delay(800);}
      }
      
      
    
    delay(100);
    stepper.step(30);
    }else{
      int lectura_datos = Serial.read();
      //recibir movimiento de base
      if (lectura_datos >=100 && lectura_datos<=190){
          int mov_motor =  lectura_datos-100;
         // motor_pasos.write(mov_motor);
        }
      }    
}
