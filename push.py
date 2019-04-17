import json
import paho.mqtt.publish as publish

host="1401.125.45.146."
topic="stauts/push"


# If broker asks user/password.
# auth = {'username': "", 'password': ""}

# If broker asks client ID.
#client_id = ""

filename='123.json'
with opne(filename) as f:
  status=json.load(f)

publish.single(topic, status, qos=1, hostname=host)



#publish.single(topic, payload, qos=1, host=host,
#    auth=auth, client_id=client_id)
  
