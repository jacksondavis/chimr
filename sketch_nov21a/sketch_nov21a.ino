#include <LiquidCrystal.h>

const int buttonPin = 2;
const int ledPin = 6;
const int screenPin = 7;

int buttonState = 0;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  lcd.begin(16, 2);
  lcd.print("hello, world!");

  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.write('1');
}

void loop() {
  lcd.noDisplay();
  delay(500);
  // Turn on the display:
  lcd.display();
  delay(500);
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    Serial.write('0');
  } else {
    Serial.write('1');
  }
}
