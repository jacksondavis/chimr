#include <rgb_lcd.h>

#include <Wire.h>

const int buttonPin = 2;
const int buzzer = 8;

int buttonState = 0;

rgb_lcd lcd;

const int colorR = 255;
const int colorG = 0;
const int colorB = 0;

String message = "";   // for incoming serial data

void setup() {
  Serial.begin(115200);
  Serial.write('1');

  lcd.begin(16, 1);
  lcd.setRGB(colorR, colorG, colorB);
  lcd.print("Hello");

  pinMode(buttonPin, INPUT);
  pinMode(buzzer, OUTPUT);
  
  Serial.write('1');
}

void loop() {
  String str;
  buttonState = digitalRead(buttonPin);
  bool rang = false;
  if (buttonState == HIGH & !rang) {
    tone(buzzer, 440, 750);
    delay(400);
    tone(buzzer, 349, 500);

    Serial.write('0');
    lcd.clear();
    lcd.setRGB(255, 255, 0);
    lcd.print("Please wait");
    delay(100);

    while (Serial.available() < 0) {}
    
    while (str == "")
    {
      str = Serial.readString();
    }
    
    lcd.clear();
    lcd.setRGB(0, 255, 0);
    
    lcd.print(str);

    delay(1000);


    if(str.length() > 16) {
      for (int positionCounter = 0; positionCounter < str.length() - 16; positionCounter++) {
          lcd.scrollDisplayLeft();
          delay(400);
      }

    delay(800);
    lcd.clear();
    lcd.print(str);
    }
  }
}


