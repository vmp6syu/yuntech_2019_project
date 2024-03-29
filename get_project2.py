import json 
import paho.mqtt.client as mqtt
import time 
import os

client = "140.125.45.146"
mqtt_looping = True

topic = "push/test1"

def on_connect(mq, userdata, rc, _):
    # subscribe when connected.
    mq.subscribe(topic)
    #mq.subscribe(TOPIC_ROOT + '/#')
def com(aa):
    if aa=="open":
        os.system('ls')
    if aa=="mode":
        os.system('ls')
    print("get"+aa) 
    
def on_message(mq, userdata, msg):
   # print "topic: %s" % msg.topic
   # print "payload: %s" % msg.payload
    com(msg.payload)
   # print "qos: %d" % msg.qos

def mqtt_client_thread():
    
    client = mqtt.Client()
    user = "test"
    password = "test1234"
    client.username_pw_set(user, password)
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("140.125.45.146",1883,60)
    except:
        print "MQTT Broker is not online. Connect later."

    mqtt_looping = True
    print "Looping..."

    #mqtt_loop.loop_forever()
    cnt = 0
    while mqtt_looping:
       
        client.loop()

        cnt += 1
        if cnt > 20:
            try:
                client.reconnect() # to avoid 'Broken pipe' error.
            except:
                time.sleep(1)
            cnt = 0
    print "quit mqtt thread"
    client.disconnect()

#def stop_all(*args):
#    global mqtt_looping
#    mqtt_looping = False

if __name__ == '__main__':
   #signal.signal(signal.SIGTERM, stop_all)
   #signal.signal(signal.SIGQUIT, stop_all)
   #signal.signal(signal.SIGINT,  stop_all)  # Ctrl-C

    mqtt_client_thread()

    print "exit program"
    sys.exit(0)
