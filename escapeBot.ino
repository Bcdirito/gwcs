
#include <Servo.h>

int rightWhiskerPin = 7;
int leftWhiskerPin = 5;
int rightWhiskerState = 0;
int leftWhiskerState = 0;

Servo servoRight;
Servo servoLeft;


void setup() {
// put your setup code here, to run once:
  pinMode(rightWhiskerPin, INPUT);
  pinMode(leftWhiskerPin, INPUT);
  Serial.begin(9600);
  servoLeft.attach(12);
  servoRight.attach(13);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1300);
}

void stopMovement(){
// Reset
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
}

void moveForward(int time) {
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(time);
}

void moveBackward(int time) {
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
  delay(time);
}

void turnLeft(int time) {
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1300);
  delay(time);
}

void turnRight(int time) {
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1700);
  delay(time);
}

void loop() {
  // put your main code here, to run repeatedly:
  rightWhiskerState = digitalRead(rightWhiskerPin);
  leftWhiskerState = digitalRead(leftWhiskerPin);

  if (rightWhiskerState == 0 && leftWhiskerState == 0){
    moveForward(1000);
  } else if (rightWhiskerState == 0 && leftWhiskerState != 0){
    turnRight(800);
    moveBackward(1000);
  } else if (rightWhiskerState != 0 && leftWhiskerState == 0){
    turnLeft(800);
    moveBackward(1000);
  } else {
    moveBackward(1000);
  }
}
