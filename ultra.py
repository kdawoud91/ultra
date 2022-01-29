from turtle import color
from vpython import*
import serial

arduinoSerialData=serial.Serial('com3',9600)
measureRod= sphere(pos=vector(1,2,1), radius=0.5)
lengthLabel=label(text='The target distance is=',height=30)

while(True):
    rate(20)
    if arduinoSerialData.inWaiting()>0 :
        myData=arduinoSerialData.readline()
        distance=float(myData)
        print(distance)

        if distance <20:
            measureRod.color = vector(0,0,1)
        elif distance >20 and distance < 25:
             measureRod.color = vector(0,1,0)
        elif distance >25:
            measureRod.color = vector(1,0,0)

        label='target distance is= '
        lengthLabel.text=label+str(distance)



