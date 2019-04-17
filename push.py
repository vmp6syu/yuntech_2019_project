import json
import os
import time
import paho.mqtt.publish as publish



host="140.125.45.146."
topic="stauts/push"
#client_id = ""     # If broker asks client ID.
#user=" "
#password" "
#If broker asks user/password.  # If broker asks user/password.

client.connect("host")

filename='123.json'
with opne(filename) as f:
  status=json.load(f)

  
i=True  #   if we out to stop the connect 
while (i):
  client.pushlish(topic,status)
  


#publish.single(topic, status, qos=1, hostname=host)
#publish.single(topic, payload, qos=1, host=host,
#    auth=auth, client_id=client_id)
  
