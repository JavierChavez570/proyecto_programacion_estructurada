#include <Servo.h>
int led = 13;    // variable to store the servo position 
Servo servoMotor;
void setup() {
        Serial.begin(9600); 
        servoMotor.attach(9);
        servoMotor.write(0);//Servo connected to D9
}
 
void loop() { 
        // send data only when you receive data:
        
        if(Serial.available()){
          if(Serial.available() == 3){
            for(int i = 0; i<=180; i+=30){
                servoMotor.write(i);
                Serial.println(i);
                 delay(100);
                 }
            }
          if(Serial.available() == 2){
              servoMotor.write(90);
              delay(1000);
              servoMotor.write(0);
            }if(Serial.available() == 1){
              digitalWrite(led,HIGH);
              delay(500);
              digitalWrite(led,LOW);
              }
}
}/*
void setup(){
  Serial.begin(9600);
  pinMode(12,OUTPUT);
  }
void loop(){
      if (Serial.available()>0){
        recepcion_datos = Serial.read();
        }
  }*/
