import serial
from time import sleep
x = ''

def a(s):
    with serial.Serial('/dev/ttyUSB0', 9600) as ser:
                ser.write(str(s).encode())

while 1:
    with open('fns.csv', 'r', newline='') as file:
        command = file.read()
        if not x == command:
             x = command
             a(x)
            #  sleep(0.05)
        # else:
        #     a('s')
        # file.close()
            

            
        
        
            
            


        