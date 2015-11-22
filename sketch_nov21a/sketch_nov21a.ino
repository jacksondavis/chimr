#include <rgb_lcd.h>

#include <Wire.h>

const int buttonPin = 2;
const int ledPin = 6;

int buttonState = 0;

rgb_lcd lcd;

const int colorR = 255;
const int colorG = 0;
const int colorB = 0;


void setup() {
  lcd.begin(16, 2);
    
  lcd.setRGB(colorR, colorG, colorB);
    
  // Print a message to the LCD.
  lcd.print("Hello");
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.write('1');
}

void loop() {
  buttonState = digitalRead(buttonPin);
  bool rang = false;
  if (buttonState == HIGH & !rang) {

    Serial.write('0');
    rang = true;
  } else {
    Serial.write('1');
  }
  if (rang & Serial.read() == 0)
  {
      lcd.clear();
      lcd.print("Coming to door");
      rang = false;
  }
}
