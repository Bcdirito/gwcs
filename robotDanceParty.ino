#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

int PIEZOPIN = 5;                            // Declare pin that the piezo is connected to.
// DECLARE LED PINS HERE

int LED1 = 2;
int LED2 = 3;
int LED3 = 4;

// One octave of notes between A4 and A5, for Piezo Greeting
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;

void setup() {
  pinMode(PIEZOPIN, OUTPUT);                 // Attach piezo to pin 5.
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  servoLeft.writeMicroseconds(1500);        // Calibrate left servo
  servoRight.writeMicroseconds(1500);       // Calibrate right servo
  // Attach LED pins here.
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
}

void giveATwirl() {
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(1000);
}

void werkItGirl() {
  servoLeft.writeMicroseconds(1500);
  delay(1500);
  servoRight.writeMicroseconds(1500);
  delay(1500);
}

void doYourThing() {
  digitalWrite(LED1, HIGH);
  delay(100);
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, HIGH);
  delay(100);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, HIGH);
  delay(100);
  digitalWrite(LED3, LOW);
}

void onTheRunway() {
 for(int x = 0; x < 5; x++){
  tone(PIEZOPIN, note_C5, 1000);
  tone(PIEZOPIN, note_C5, 1000);
  tone(PIEZOPIN, note_G5, 1000);
  tone(PIEZOPIN, note_F5, 1000);

 }
}

void loop() {
  // Code for testing servos.
  // Tinker with the numbers to see how they work!
  // For help, visit https://learn.parallax.com/tutorials/robot/shield-bot/robotics-board-education-shield-arduino/chapter-2-shield-lights-servo-4.
//  servoLeft.writeMicroseconds(1700);
//  servoRight.writeMicroseconds(1300);
//  delay(500);
  for (int x = 0; x < 5; x++){
    giveATwirl();
    werkItGirl();
    doYourThing();
    onTheRunway();
  }
}
