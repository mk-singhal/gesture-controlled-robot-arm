#include <Servo.h>

#define numOfValsRec 5
#define digitsPerValRec 1

Servo servofinger_1;
Servo servofinger_2;
Servo servofinger_3;
Servo servofinger_4;
Servo servofinger_5;

int valsRec[numOfValsRec];
int stringLength = numOfValsRec * digitsPerValRec + 1;      //$00000
int counter = 0;
bool counterStart = false;
String recievedString;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servofinger_1.attach(3);
  servofinger_2.attach(5);
  servofinger_3.attach(6);
  servofinger_4.attach(11);
  servofinger_5.attach(9);
}

void recieveData() {
  while(Serial.available()) {
    char c = Serial.read();
    
    if(c == '$'){
     counterStart = true; 
    }

    if(counterStart) {
      if(counter < stringLength) {
        recievedString = String(recievedString + c);
        counter++ ;
      }
      if(counter >= stringLength) {
        for(int i = 0; i<numOfValsRec; i++)
        {
          int num = (i*digitsPerValRec)+1;
          valsRec[i] = recievedString.substring(num,num+digitsPerValRec).toInt();
        }
        recievedString = "";
        counter = 0;
        counterStart = false;
      }
    }
    
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  recieveData();
  if (valsRec[0] == 0) {servofinger_1.write(150);Serial.print("1 ");} else {servofinger_1.write(0);Serial.print("0 ");}
  if (valsRec[1] == 0) {servofinger_2.write(180);Serial.print("1 ");} else {servofinger_2.write(0);Serial.print("0 ");}
  if (valsRec[2] == 0) {servofinger_3.write(180);Serial.print("1 ");} else {servofinger_3.write(0);Serial.print("0 ");}
  if (valsRec[3] == 0) {servofinger_4.write(180);Serial.print("1 ");} else {servofinger_4.write(0);Serial.print("0 ");}
  if (valsRec[4] == 0) {servofinger_5.write(160);Serial.print("1 ");} else {servofinger_5.write(0);Serial.print("0 ");}
  Serial.println();
  delay(1000);
}
