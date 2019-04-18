import json
import os
import time
import paho.mqtt.publish as publish

def mqtt_on_push(host,topic,client_id,user,password,bn_loop):
    client.connect(host)
 
    filename='123.json'
    with opne(filename) as f:
        status=json.load(f)

  
    i=True  #   if we out to stop the connect 
        while (i):
            client.pushlish(topic,status)
  


#publish.single(topic, status, qos=1, hostname=host)
#publish.single(topic, payload, qos=1, host=host,
#    auth=auth, client_id=client_id)
  
if __name__ == '__main__':
  
    host="140.125.45.146"
    topic="stauts/push"
    client_id = ""     # If broker asks client ID.
    user=" "
    password" "
    If broker asks user/password.  # If broker asks user/password.
    bn_loop=1
    
    mqtt_on_push(host,topic,client_id,user,password,bn_loop)
    print "exit program"
    sys.exit(0)
  
  
