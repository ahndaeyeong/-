import serial
import time
import matplotlib.pyplot as plt
py_serial=serial.Serial(port='COM8',baudrate=9600)
while True:
    temp_list = []
    commend=input('내릴 명령')
    py_serial.write(commend.encode())
    time.sleep(0.1)
    for i in range(100):
        if py_serial.readable():
            response=py_serial.readline()
            temp_list.append(response[:len(response)-1].decode())
            print(response[:len(response)-1].decode())
    plt.plot(temp_list)
    plt.show()
