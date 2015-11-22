#include <rgb_lcd.h>

#include <Wire.h>

const int buttonPin = 2;

int buttonState = 0;

rgb_lcd lcd;

const int colorR = 255;
const int colorG = 0;
const int colorB = 0;

String message = "";   // for incoming serial data

void setup() {
  Serial.begin(115200);
  Serial.write('1');

  lcd.begin(16, 2);
  lcd.setRGB(colorR, colorG, colorB);
  lcd.print("Hello");

  pinMode(buttonPin, INPUT);
  Serial.write('1');
}

void loop() {
  String str;
  buttonState = digitalRead(buttonPin);
  bool rang = false;
  if (buttonState == HIGH & !rang) {
    Serial.write('0');
    lcd.clear();
    lcd.print("waiting for message");
    while (Serial.available() < 0)
    {
    }
    while (str == "")
    {
      str = Serial.readString();
    }
    lcd.clear();
    lcd.print(str);
  }
}