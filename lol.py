import serial
connected = False

ser = serial.Serial('/dev/cu.usbmodem1421', 115200)

while not connected:
    serin = ser.read()
    connected = True

print ser.write("two words")
