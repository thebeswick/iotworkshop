import random
import paho.mqtt.client as paho
client = paho.Client()
temperature = random.randint(18,34)
client.connect("0.0.0.0", 1883)
client.publish("homeassistant/sensor1/temperature", temperature, qos=1, retain=1)
# print temperature
client.disconnect()
client.connect("0.0.0.0", 1883)
temperature = random.randint(18,34)
# print temperature
client.publish("homeassistant/sensor2/temperature", temperature, qos=1, retain=1)
client.disconnect()
