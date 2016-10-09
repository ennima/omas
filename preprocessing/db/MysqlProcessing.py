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
	current_table_file = ""
	current_fields = []
	data = []
	tables = []
	tables_total = 0
	types = []
	types_path = "types.json"
	global_path = ""

	# Memory Outputs
	memory_create = []
	memory_insert = []
	memory_update = []
	memory_delete = []

	# Backend 
	bk_var_prefix = "$"
	bk_var_nom = "_val_"

	# Processing Options
	process_create = True
	process_insert = True
	process_update = True
	process_delete = True
	process_select = True

	# Output
	publish_project_name = "MysqlPrj" 
	publish_path = ""
	publsh_to_file = True
	publish_single_file = True
	prettyfy = True

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
							if(self.types[i]["type"] == "VARCHAR"):
								return_type = self.types[i]["type"]+"("+str(field["size"])+")"
							else:
								return_type = self.types[i]["type"]
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
				
	def set_table_name(self,name):
		vals = {}
		table_name = name
		field_id = ""
		
		if(isPlural(name)):
			field_id = name.replace("s","")

		else:
			field_id = name
			table_name = name + "s"

		vals = {"table_name":table_name, "field_id":field_id}
		return vals


	def create_table(self,name,fields):
		print("Creando tabla ",name)
		table_vals = self.set_table_name(name)
		table_name = table_vals["table_name"]
		field_id = table_vals["field_id"]

		self.current_table_file = table_name

		print("#Table  "+table_name, " #ID: ",field_id)

		if(self.prettyfy):
			createQuery = "CREATE TABLE "+table_name+"("+"\n"
		else:
			createQuery = "CREATE TABLE "+table_name+"("
		
		#print(createQuery)

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
				line_begin = "\t"
			else:
				line_end = line_end
				line_begin = ""
			#print("--TYPE IS: ",tipo)

			if(len(field) == 2):
				#print ("Field simple data BOOL")
				#print(field["name"]+" "+tipo+line_end)
				createQuery += line_begin+field["name"]+" "+tipo+line_end

			elif( len(field) == 3):
				#print ("Normal field")
				
				if(field["type"] == "uid"):
					#print("ES UN ID")
					#print(field_id+"_id "+tipo+line_end)
					createQuery += line_begin+field_id+"_id "+tipo+line_end
				else:
					#print(field["name"]+" "+tipo+line_end)
					createQuery += line_begin+field["name"]+" "+tipo+line_end

			elif( len(field) == 4):
				#print ("Required field")
				#print(field["name"]+" "+tipo + " NOT NULL"+line_end)
				createQuery += line_begin+field["name"]+" "+tipo + " NOT NULL"+line_end

			elif( len(field) == 5):
				#print ("Unique field")
				#print(field["name"]+" "+tipo + " NOT NULL UNIQUE"+line_end)
				createQuery += line_begin+field["name"]+" "+tipo + " NOT NULL UNIQUE"+line_end
			#print(",")

			count_field += 1
		createQuery +=");"
		#print(");")
		print(createQuery)
		print(fieldsQuery)
		return createQuery
	
	def create_insert(self,name,fields):
		
		print("Creando Insert a la tabla: ",name)
		table_vals = self.set_table_name(name)
		table_name = table_vals["table_name"]
		field_id = table_vals["field_id"]
		

		self.current_table_file = table_name

		print("#Table  "+table_name, " #ID: ",field_id)

		if(self.prettyfy):
			createQuery = "INSERT INTO "+table_name+"("+"\n"
			valsQuery = "VALUES" + "("+"\n"
		else:
			createQuery = "INSERT INTO "+table_name+"("
			valsQuery = "VALUES" + "("
		
		
		fieldsQuery = []

		fields_len = len(fields)
		count_field = 0
		for field in fields:
			
			if(count_field < (fields_len-1)):
				line_end = ","
			else:
				line_end =""
			if(self.prettyfy):
				line_end = line_end+"\n"
				line_begin = "\t"
			else:
				line_end = line_end
				line_begin = ""
			

			if(len(field) == 2):
				
				createQuery += line_begin+field["name"]+" "+line_end
				valsQuery += line_begin+self.bk_var_prefix + self.bk_var_nom +field["name"]+" "+line_end
			elif( len(field) == 3):
				
				
				if(field["type"] == "uid"):
					
					createQuery += line_begin+field_id+"_id "+line_end
					valsQuery += line_begin+self.bk_var_prefix + self.bk_var_nom +field_id+"_id "+line_end
				else:
					
					createQuery += line_begin+field["name"]+" "+line_end
					valsQuery += line_begin+self.bk_var_prefix + self.bk_var_nom +field["name"]+" "+line_end

			elif( len(field) == 4):
				
				createQuery += line_begin+field["name"]+" "+line_end
				valsQuery += line_begin+self.bk_var_prefix + self.bk_var_nom +field["name"]+" "+line_end

			elif( len(field) == 5):
				
				createQuery += line_begin+field["name"]+" "+line_end
				valsQuery += line_begin+self.bk_var_prefix + self.bk_var_nom +field["name"]+" "+line_end
			

			count_field += 1
		createQuery +=")"
		valsQuery +=");"
		
		if(self.prettyfy):
			returnQuery = createQuery +"\n"+valsQuery
		else:
			returnQuery = createQuery +" "+valsQuery
		return returnQuery

	def create_update(self,name,fields):
		
		print("Creando Update a la tabla: ",name)
		table_vals = self.set_table_name(name)
		table_name = table_vals["table_name"]
		field_id = table_vals["field_id"]
		

		self.current_table_file = table_name

		print("#Table  "+table_name, " #ID: ",field_id)

		if(self.prettyfy):
			createQuery = "UPDATE "+table_name+" SET "+"\n"
			
		else:
			createQuery = "UPDATE "+table_name+" SET "
		
		
		
		fieldsQuery = []

		fields_len = len(fields)
		count_field = 0
		for field in fields:
			
			if(count_field < (fields_len-1)):
				line_end = ","
			else:
				line_end =""
			if(self.prettyfy):
				line_end = line_end+"\n"
				line_begin = "\t"
			else:
				line_end = line_end
				line_begin = ""
			

			if(len(field) == 2):
				
				createQuery += line_begin+field["name"]+" = "+self.bk_var_prefix + self.bk_var_nom +field["name"]+" "+line_end
				
			elif( len(field) == 3):
				
				
				if(field["type"] == "uid"):
					idQuery = field_id+"_id = "+ self.bk_var_prefix + self.bk_var_nom +field_id+"_id"
					
				else:
					
					createQuery += line_begin+field["name"]+" = "+self.bk_var_prefix + self.bk_var_nom +field["name"]+" "+line_end
					

			elif( len(field) == 4):
				
				createQuery += line_begin+field["name"]+" = "+self.bk_var_prefix + self.bk_var_nom +field["name"]+" "+line_end
				

			elif( len(field) == 5):
				
				createQuery += line_begin+field["name"]+" = "+self.bk_var_prefix + self.bk_var_nom +field["name"]+" "+line_end
				
			

			count_field += 1
		createQuery +="WHERE " + idQuery + ";"
		
		
		if(self.prettyfy):
			returnQuery = createQuery +"\n"
		else:
			returnQuery = createQuery 
		return returnQuery

	def create_delete(self, name):
		deleteQuery = "DELETE FROM "+name+" WHERE "+name+"."+name+"_id = "+self.bk_var_prefix + self.bk_var_nom +name+"_id;"
		return deleteQuery

	def create_select(self, name):
		deleteQuery = "SELECT FROM "+name+" WHERE "+" 1;"
		return deleteQuery

	def memory_array_to_string(self,memory_array):
		print("# MEMORY REPRESENTATIONS: ")
		retunr_string = ""

		for item in memory_array:
			#print(item)
			retunr_string += item["value"] + "\n\n\n"

		#print(retunr_string)
		return retunr_string

	def memory_to_file(self):
		print("#### TO FILE")
		if(self.process_create):
			if(self.publish_single_file):
				file_contents = self.memory_array_to_string(self.memory_create)
				file_name = self.publish_project_name + "_Create" + ".sql"
				sql_file = open(self.publish_path + file_name ,"w")
				sql_file.write(file_contents)
				sql_file.close()
			else:
				for item in self.memory_create:
					
					table_vals = self.set_table_name(item["name"])
					print(table_vals["table_name"]+".sql")
					print(item["value"])
					sql_file = open(self.publish_path + table_vals["table_name"]+".sql" ,"w")
					sql_file.write(item["value"])
					sql_file.close()

		if(self.process_insert):
			if(self.publish_single_file):
				file_contents = self.memory_array_to_string(self.memory_insert)
				file_name = self.publish_project_name + "_Insert" + ".sql"
				sql_file = open(self.publish_path + file_name ,"w")
				sql_file.write(file_contents)
				sql_file.close()
			else:
				for item in self.memory_insert:
					
					table_vals = self.set_table_name(item["name"])
					print(table_vals["table_name"]+".sql")
					print(item["value"])
					sql_file = open(self.publish_path + table_vals["table_name"]+"_Insert.sql" ,"w")
					sql_file.write(item["value"])
					sql_file.close()

		if(self.process_update):
			if(self.publish_single_file):
				file_contents = self.memory_array_to_string(self.memory_update)
				file_name = self.publish_project_name + "_Update" + ".sql"
				sql_file = open(self.publish_path + file_name ,"w")
				sql_file.write(file_contents)
				sql_file.close()
			else:
				for item in self.memory_update:
					
					table_vals = self.set_table_name(item["name"])
					print(table_vals["table_name"]+".sql")
					print(item["value"])
					sql_file = open(self.publish_path + table_vals["table_name"]+"_Update.sql" ,"w")
					sql_file.write(item["value"])
					sql_file.close()

		if(self.process_delete):
			if(self.publish_single_file):
				file_contents = self.memory_array_to_string(self.memory_delete)
				file_name = self.publish_project_name + "_Delete" + ".sql"
				sql_file = open(self.publish_path + file_name ,"w")
				sql_file.write(file_contents)
				sql_file.close()
			else:
				for item in self.memory_delete:
					
					table_vals = self.set_table_name(item["name"])
					print(table_vals["table_name"]+".sql")
					print(item["value"])
					sql_file = open(self.publish_path + table_vals["table_name"]+"_Delete.sql" ,"w")
					sql_file.write(item["value"])
					sql_file.close()



	def process(self):
		single_file = ""
		table_file = ""
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
				if(self.process_create):
					create_table_query = self.create_table(self.current_table,self.current_fields)
					self.memory_create.append({"name":self.current_table, "value":create_table_query})

				if(self.process_insert):
					create_insert_query = self.create_insert(self.current_table,self.current_fields)
					self.memory_insert.append({"name":self.current_table, "value":create_insert_query})

				if(self.process_update):
					create_insert_query = self.create_update(self.current_table,self.current_fields)
					self.memory_update.append({"name":self.current_table, "value":create_insert_query})

				if(self.process_delete):
					create_insert_query = self.create_delete(self.current_table)
					self.memory_delete.append({"name":self.current_table, "value":create_insert_query})


				#print(create_insert_query)
				if(self.publsh_to_file):
					if(self.publish_single_file):
						if(self.process_create):
							print("#Single File")
							single_file += create_table_query + "\n\n"
					else:
						
						if(self.process_create):
							# print("CURRENT: ",self.current_table_file)
							# table_file = open(self.publish_path + self.current_table_file + ".sql","w")
							# table_file.write(create_table_query)
							# table_file.close()
							pass

				self.current_fields = []
		print("\n # MEMORY: ", self.memory_update, "\n\n")	
		#self.memory_array_to_string(self.memory_insert)

		if(self.publsh_to_file):		
			print("Publishing to Single File: \n"+single_file)
			self.memory_to_file()
			# if(self.process_create):
			# 	sql_file = open(self.publish_path + "MySQL_Proyect.sql","w")
			# 	sql_file.write(single_file)
			# 	sql_file.close()