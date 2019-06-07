#include <Servo.h>                           // Include servo library

Servo servoRight;
Servo servoLeft;

int piezo = A0;

int sensorReading = 0;
int threshold = 10;

void moveKitty() {
  // Your Code Here
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1500);

}

void stopKitty() {
  // Your Code Here
  servoRight.writeMicroseconds(2000);
  servoLeft.writeMicroseconds(2000);
}

void setup() {
  // put your setup code here, to run once:

  //Your Code Here
  servoLeft.attach(13);
  servoRight.attach(12);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorReading = analogRead(piezo);

  //Your Code Here

  while (sensorReading <= threshold) {
    moveKitty();
    Serial.println("Meow meow!");
    delay(1000);
  }

  stopKitty();
  delay(500);
}
