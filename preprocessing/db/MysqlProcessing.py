import sys, os
import json

class MysqlProcessing:

	current_table = ""
	current_fields = []
	data = []
	tables = []
	tables_total = 0
	types = []
	def __init__(self):
		#print("creado")
		VARCHAR(x)
			Case: user name, email, country, subject, password

		TEXT
			Case: messages, emails, comments, formatted text, html, code, images, links

		MEDIUMTEXT
			Case: large json bodies, short to medium length books, csv strings

		LONGTEXT
			Case: textbooks, programs, years of logs files, harry potter and the goblet of fire, scientific research logging
		types = [
					{
						"class":"string",
						"min":"1",
						"max":"255",
						"type":"VARCHAR"
					},
					{
						"class":"string",
						"min":"256",
						"max":"65535",
						"type":"TEXT"
					},
					{
						"class":"string",
						"min":"65536",
						"max":"16777215",
						"type":"MEDIUMTEXT"
					},
					{
						"class":"string",
						"min":"16777216",
						"max":"4294967295",
						"type":"LONGTEXT"
					},
					{
						"class":"string",
						"min":"16777216",
						"max":"4294967295",
						"type":"LONGTEXT"
					}
				]
	
	def load(self,db_path):
		print("Loading db: "+db_path)
		if(os.path.exists(db_path)):
			# print("Existe la db")
			with open(db_path) as data_file:
				self.data = json.load(data_file)

			return True

		else:
			# print("No existe la db")
			return False

	def create_table(self,name,fields):
		print("Creando tabla ",name)

		for field in fields:
			if(len(field) == 2):
				print ("Normal field simple data")
			elif( len(field) == 3):
				print ("Normal field")
			elif( len(field) == 4):
				print ("Required field")

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