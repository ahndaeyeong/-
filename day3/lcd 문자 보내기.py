import serial
import time

py_serial=serial.Serial(port='com8',baudrate=9600)
while True:
    commend=input('전송할 글자 입력')
    py_serial.write(commend.encode())
    time.sleep(0.1)
    if py_serial.readable():
        st1=py_serial.readline()
        print(st1[:len(st1)-1].decode())