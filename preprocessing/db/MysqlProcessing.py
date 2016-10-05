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

	prettyfy = False

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


	def field_type(self,field):
		
		#print("-Field: ",field["name"])
		return_type = ""
		for i in range(0,(len(self.types))):
			if(self.types[i]["class"] == field["type"]):
				
				if(field["type"] != "bool"):
					
					if(field["type"] == "uid"):
						return_type = self.types[i]["type"]
						break

					if(field["type"] == "date"):
						return_type = self.types[i]["type"]
						break

					if(field["type"] == "time"):
						return_type = self.types[i]["type"]
						break

					if(field["type"] == "datetime"):
						return_type = self.types[i]["type"]
						break

					if(field["type"] == "string"):
						
						if((toNum(self.types[i]["min"]) <= field["size"])and((field["size"] <= toNum(self.types[i]["max"])))):
							#print("COINCIDE CON TYPE: ",self.types[i]["type"])
							return_type = self.types[i]["type"]+"("+str(field["size"])+")"
							break

					if(field["type"] == "int"):
						
						if((toNum(self.types[i]["min"]) <= field["size"])and((field["size"] <= toNum(self.types[i]["max"])))):
							#print("COINCIDE CON TYPE: ",self.types[i]["type"])
							#print("INT ",len(str(field["size"])))
							cantidad = str(len(str(field["size"])))
							return_type = self.types[i]["type"]+"("+cantidad+")"
							break

					if(field["type"] == "float"):
						deci = field["size"].split(",")
						#print("DECIMAL("+deci[0]+","+deci[1]+")")
						return_type = "DECIMAL("+deci[0]+","+deci[1]+")"

				else:
					if(field["type"] == "bool"):
						return_type = self.types[i]["type"]
						break
			
		return return_type
				




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

		print("#Table  "+table_name, " #ID: ",field_id)

		createQuery = "CREATE TABLE "+table_name+"("
		print(createQuery)

		fieldsQuery = []

		fields_len = len(fields)
		count_field = 0
		for field in fields:
			tipo = self.field_type(field)
			if(count_field < (fields_len-1)):
				line_end = ","
			else:
				line_end =""
			if(self.prettyfy):
				line_end = line_end+"\n"
			else:
				line_end = line_end
			#print("--TYPE IS: ",tipo)

			if(len(field) == 2):
				#print ("Field simple data BOOL")
				print(field["name"]+" "+tipo+line_end)

			elif( len(field) == 3):
				#print ("Normal field")
				
				if(field["type"] == "uid"):
					#print("ES UN ID")
					print(field_id+"_id "+tipo+line_end)
				else:
					print(field["name"]+" "+tipo+line_end)

			elif( len(field) == 4):
				#print ("Required field")
				print(field["name"]+" "+tipo + " NOT NULL"+line_end)

			elif( len(field) == 5):
				#print ("Unique field")
				print(field["name"]+" "+tipo + " NOT NULL UNIQUE"+line_end)
			#print(",")

			count_field += 1
		print(");")
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