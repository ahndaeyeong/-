import serial
import time

py_serial=serial.Serial(port='com8',baudrate=9600)
while True:
    commend=input('전송할 글자 입력')
    py_serial.write(commend.encode())
    time.sleep(0.1)