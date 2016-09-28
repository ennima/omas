import sys, os
import json
import ctypes

def isPlural(cadena):
	if(cadena.endswith("s")):
		return True
	else:
		return False

def toNum(numero):
	valor = numero
	if("." in numero):
		valor = float(numero)
	else:
		valor = int(numero)
	return valor

class MysqlProcessing:

	current_table = ""
	current_fields = []
	data = []
	tables = []
	tables_total = 0
	types = []
	types_path = "types.json"
	global_path = ""
	def __init__(self,global_path):
		#print("creado")
		# VARCHAR(x)
		# 	Case: user name, email, country, subject, password

		# TEXT
		# 	Case: messages, emails, comments, formatted text, html, code, images, links

		# MEDIUMTEXT
		# 	Case: large json bodies, short to medium length books, csv strings

		# LONGTEXT
		# 	Case: textbooks, programs, years of logs files, harry potter and the goblet of fire, scientific research logging
		
		print(self.global_path+self.types_path)
		self.global_path = global_path
		if(os.path.exists(self.global_path+self.types_path)):
			print("Hay types")
		else:
			print("Falta archivo de tipos: "+self.global_path+self.types_path)
	
	def load(self,db_path):
		print("Loading db: "+db_path)
		if(os.path.exists(db_path)):
			# print("Existe la db")
			with open(db_path) as data_file:
				self.data = json.load(data_file)
				self.load_types(self.global_path+self.types_path)

			return True

		else:
			# print("No existe la db")
			return False


	def load_types(self,db_path):
		print("Loading types: "+db_path)
		if(os.path.exists(db_path)):
			# print("Existe la db")
			with open(db_path) as data_file:
				self.types = json.load(data_file)

			return True

		else:
			# print("No existe la db")
			return False


	def field_type_string(self,field):
		
		print("-Field: ",field["name"])
		for i in range(0,(len(self.types))):
			if(self.types[i]["class"] == field["type"]):
				
				if(field["type"] != "bool"):
					
					if(field["type"] == "string"):
						
						if((toNum(self.types[i]["min"]) <= field["size"])and((field["size"] <= toNum(self.types[i]["max"])))):
							print("COINCIDE CON TYPE: ",self.types[i]["type"])
							break

					if(field["type"] == "int"):
						
						if((toNum(self.types[i]["min"]) <= field["size"])and((field["size"] <= toNum(self.types[i]["max"])))):
							print("COINCIDE CON TYPE: ",self.types[i]["type"])
							break
				else:
					print("##BOOLEANO: ", field["name"])
				


	def create_table(self,name,fields):
		print("Creando tabla ",name)
		table_name = name
		field_id = ""
		if(isPlural(name)):
			#print("#ID Plural")
			#print(name.replace("s",""))
			field_id = name.replace("s","")
		else:
			#print("#ID NotPlural")
			#print(name + "s")
			field_id = name
			table_name = name + "s"

		print("#Table  "+table_name)

		createQuery = "CREATE TABLE "+table_name+"("
		fieldsQuery = []

		for field in fields:
			self.field_type_string(field)

			# if(len(field) == 2):
			# 	print ("Field simple data BOOL")
			# elif( len(field) == 3):
			# 	print ("Normal field")

			# 	if(field["name"]=="_id"):
			# 		print("#ID    "+field_id)
			# 		fieldsQuery.append(field_id+"_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT")

			# elif( len(field) == 4):
			# 	print ("Required field")

			# elif( len(field) == 5):
			# 	print ("Unique field")

		print(fieldsQuery)

	def process(self):
		for obj in self.data:
			#pprint(obj)
			for obj_name in obj:
				#Inicio de objeto
				print(obj_name)
				self.tables_total += 1
				self.tables.append(obj_name)
				self.current_table = obj_name

				for field in obj[obj_name]:
					#print(field['name'],field['type'],field['size'])
					self.current_fields.append(field)
					# print("Field Len: ",len(field))
					# for prop in field:
					# 	print(prop)
				#fin de objeto
				print("\n")
				# print(self.current_table)
				# print(self.current_fields,"\n")
				self.create_table(self.current_table,self.current_fields)
				self.current_fields = []