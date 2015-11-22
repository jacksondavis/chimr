#include <rgb_lcd.h>

#include <Wire.h>

const int buttonPin = 2;
int buttonState = 0;

rgb_lcd lcd;

void setup() {
  Serial.begin(115200);

  Serial.write('1');

  lcd.begin(16, 2);
  lcd.setRGB(255, 0, 0);
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
    lcd.setRGB(255, 255, 0);
    lcd.print("Please wait");
    delay(100);
    while (str == "")
    {
      str = Serial.readString();
    }
    lcd.clear();
    lcd.setRGB(0, 255, 0);
    lcd.print(str);
  }
}
