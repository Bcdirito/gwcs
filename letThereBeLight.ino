int pin = 10;
int unit = 320;

void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
//  digitalWrite(pin, HIGH);
//  delay(1000)
//  digitalWrite(pin, LOW);
//  delay(1000)

  // Message - You Rock

  flashMessage();
}

void dot() {
  digitalWrite(pin, HIGH);
  delay(unit);
  digitalWrite(pin, LOW);
}

void dash() {
  digitalWrite(pin, HIGH);
  delay(unit * 3);
  digitalWrite(pin, LOW);
}

void flashY() {
  dash();
  delay(unit);
  dot();
  delay(unit);
  dash();
  delay(unit);
  dash();
}

void flashO(){
  dash();
  delay(unit);
  dash();
  delay(unit);
  dash();
}

void flashU(){
  dot();
  delay(unit);
  dot();
  delay(unit);
  dash();
}

void flashR(){
  dot();
  delay(unit);
  dash();
  delay(unit);
  dot();
}

void flashC(){
  dash();
  delay(unit);
  dot();
  delay(unit);
  dash();
  delay(unit);
  dot();
}

void flashK(){
  dash();
  delay(unit);
  dot();
  delay(unit);
  dash();
}

void flashFirstWord(){
  flashY();
  delay(unit * 3);
  flashO();
  delay(unit * 3);
  flashU();
  delay(unit * 7);
}

void flashSecondWord(){
  flashR();
  delay(unit * 3);
  flashO();
  delay(unit * 3);
  flashC();
  delay(unit * 3);
  flashK();
  delay(unit * 7);
}

void flashMessage(){
  flashFirstWord();
  flashSecondWord();
}
