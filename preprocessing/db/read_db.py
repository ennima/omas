import json
from pprint import pprint

with open('db.json') as data_file:    
    data = json.load(data_file)

#pprint(data)

for obj in data:
	#pprint(obj)
	for obj_name in obj:
		#Inicio de objeto
		print(obj_name)
		
		for field in obj[obj_name]:
			print(field['name'],field['type'],field['size'])
			print("Field Len: ",len(field))
		#fin de objeto
		print("\n")