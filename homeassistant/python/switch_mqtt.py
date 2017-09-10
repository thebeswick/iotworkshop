import paho.mqtt.client as mqtt  #import the client1
import time

def on_connect(client, userdata, flags, rc):
    m="Connected flags"+str(flags)+"result code "\
    +str(rc)+"client1_id  "+str(client)
    print(m)

def on_message(client1, userdata, message):
    print("message received  "  ,str(message.payload.decode("utf-8")))

broker_address="0.0.0.0"
#broker_address="iot.eclipse.org"
client1 = mqtt.Client("switch_tester")    #create new instance
client1.on_connect= on_connect        #attach function to callback
client1.on_message=on_message        #attach function to callback
time.sleep(1)
client1.connect(broker_address)      #connect to broker
client1.loop_start()    #start the loop
client1.subscribe("house/bulbs/bulb1")
client1.publish("house/bulbs/bulb1","OFF")
time.sleep(5)
client1.disconnect()
client1.loop_stop()
