const int buttonPin = 2;
const int ledPin = 6;
const int screenPin = 7;

int buttonState = 0;


void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.write('1');
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {

    Serial.write('0');
  } else {
    Serial.write('1');
  }
}
