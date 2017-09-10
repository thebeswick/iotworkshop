import yaml
with open('../sensors.yaml', 'r') as f:
	mydict = yaml.load(f.read())
f.close()

# print(mydict['sensor'][0]['state_topic'])
print len(mydict)
# print len(mydict['sensor'])

