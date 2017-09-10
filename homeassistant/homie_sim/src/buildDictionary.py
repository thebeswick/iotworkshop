import json 
import yaml
import paho.mqtt.client as mqtt
with open("./config.json") as data_file:
  data = json.load(data_file)

data_file.close()

# yaml.dump(inputList[0], default_flow_style=False)

inputCount = 4
homieInput = "input"
outputCount = 4
homieOutput = "output"
inputList =[dict() for x in range(inputCount)]
outputList =[dict() for x in range(outputCount)]
device_id = (data['device_id'])
prefix = (data['mqtt']['base_topic'])
yamlInputFname = device_id + "_input.yaml"
yamlOutputFname = device_id + "_output.yaml"
# homie_node = "/led1"
# object_id = prefix + device_id + homie_node
yamlFile = open('test.yaml', 'w')
state = False
platform = "    - platform: mqtt"
payload_on = "    payload_on: \"true\""
payload_off = "    payload_off: \"false\""
for i in range(len(inputList)):
  nodeName = "/"+ homieInput + str(i)
  print(nodeName)
  nodeTopic = prefix + device_id + nodeName
  pubTopic = nodeTopic + "/on"
  subTopic = nodeTopic + "/on/set"
  inputList[i] = { "name" : nodeName, "command_topic" : subTopic, "state_topic" : pubTopic, "state" : state }
  print(inputList[i])
  yamlFile.write(platform+"\n")
  yamlFile.write("    name: \""+ nodeName+ "\"\n")
  yamlFile.write("    command_topic: "+ subTopic+ "\n")
  yamlFile.write(payload_on+ "\n")
  yamlFile.write(payload_off+ "\n")

yamlFile.close()


  - platform: mqtt
    name: "Daisy Switch"
    command_topic: "homeassistant/girlsbedrooms/switch1/on/set"
    state_topic: "homeassistant/girlsbedrooms/switch1/on"
    payload_on: "true"
    payload_off: "false"
    qos: 1
  - platform: mqtt

for i in range(len(outputList)):
  nodeName = "/"+ homieOutput + str(i)
  print(nodeName)
  nodeTopic = prefix + device_id + nodeName
  subTopic = nodeTopic + "change"
  pubTopic = nodeTopic + "change"
  outputList[i] = { "NodeName" : nodeName, "subscribe" : subTopic, "publish" : pubTopic, "state" : state }
  print(outputList[i])
mqttc = mqtt.Client()
mqttc.username_pw_set("autom8", "20Myrtle")
mqttc = mqtt.Client()
mqttc.username_pw_set("autom8", "20Myrtle")
mqttc.connect("192.168.1.100", 1883, 60)
mqtt.publish(object_id, state)
