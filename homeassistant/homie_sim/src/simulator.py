
import json
import os
import sys
import time
from threading import Timer
from twisted.internet import task
from twisted.internet import reactor
import inspect
import paho.mqtt.client as mqtt

with open(sys.argv[1]) as data_file:    
    data = json.load(data_file)
# def setup():
interval = 60
device_id = (data['device_id'])
prefix = (data['mqtt']['base_topic'])
homie_node = "/led1"

uptime = 0
# return device_id
#  return msg_prefix

def on_message_msgs(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/messages/#
    print("MESSAGES: "+msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_message_bytes(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/bytes/#
    print("BYTES: "+msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_message(mosq, obj, msg):
    # This callback will be called for messages that we receive that do not
    # match any patterns defined in topic specific callbacks, i.e. in this case
    # those messages that do not have topics $SYS/broker/messages/# nor
    # $SYS/broker/bytes/#
    print(msg.topic+" "+str(msg.payload))
    new_topic = msg.topic+device_id
    mqttc.publish("homeassistant/set", device_id)
    mqttc.publish(new_topic, msg_prefix)
 
def keep_alive_msg():
	uptime = uptime + 6
 	mqttc.publish("Alive", "60")
 	pass




mqttc = mqtt.Client()
mqttc.username_pw_set("autom8", "20Myrtle")
# Add message callbacks that will only trigger on a specific subscription match.
# mqttc.message_callback_add("homeassistant/1", on_message_msgs)
# mqttc.message_callback_add("homeassistant/2", on_message_bytes)
mqttc.on_message = on_message
mqttc.connect("192.168.1.100", 1883, 60)
mqttc.subscribe("homeassistant")
mqttc.subscribe("homeassistant2")
timeout = 6.0 # Sixty seconds
l = task.LoopingCall(keep_alive_msg)
l.start(timeout) # call every sixty seconds
reactor.run()
mqttc.loop_forever()




