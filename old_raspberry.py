import sys
import time
import paho.mqtt.publish as publish
import Adafruit_DHT
import threading
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.IN)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.IN)
def on_connect(client,userdata,flags,rc):
    print("Connected"+str(rc))
    client.subscribe("group3_get")
def on_message(client,userdata,msg):
    #print(msg.topic+""+str(msg.payload))
    strings = str(msg.payload)
    ls = len(strings)
    S=""
    for i in range(2,ls-1,1):
        S += strings[i]
    l2 = []
    l2 = S.split(',')
    global LED,FAN,AIR
    for iss in range(0,len(l2),2):
        if l2[iss].upper() == "LED":
            if l2[iss+1] == "1":
                LED = 1
                GPIO.output(17,GPIO.HIGH)
            else:
                LED = 0
                GPIO.output(17,GPIO.LOW)
        elif l2[iss].upper() == "AIR":
            if l2[iss+1] == "1":
                AIR = 1
                GPIO.output(22,GPIO.HIGH)
            else:
                AIR = 0
                GPIO.output(22,GPIO.LOW)
        else:
            if l2[iss+1] == "1":
                FAN = 1
                GPIO.output(27,GPIO.HIGH)
            else: 
                FAN = 0
                GPIO.output(27,GPIO.LOW)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
LED = 0
FAN = 0
AIR = 0
MQ2 = False
MQ1 = False
try:
    client.connect("140.125.33.105")
    threading.Thread(target = client.loop_forever).start()
    while True:
        hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
        RI = GPIO.input(18)
        MQ1 = MQ2
        MQ2 = GPIO.input(23)
        BUTT = GPIO.input(24)
        st = "[" + str(hum) + ',' + str(temp) + ','
        if LED == 1:
            st +="1,"
        else:
            st +="0,"
        if FAN == 1:
            st +="1,"
        else:
            st +="0,"
        if AIR == 1:
            st +="1,"
        else:
            st +="0,"
        
        if RI == True:
            st +="1,"
        else:
            st +="0,"
        
        if MQ2 == True:
            st +='1,'
        else:
            st +='0,'
        
        if BUTT == True:
            st +="1]"
        else:
            st +="0]"
        print(st)
        publish.single("group3_push", payload=st, qos=0, hostname="140.125.33.105")
        
except KeyboardInterrupt:
    sys.exit(1)
