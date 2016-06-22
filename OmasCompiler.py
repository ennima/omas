##################################################
#Author: Enrique Nieto
#Start: 26-04-2016
##################################################
import os, sys
from OmasError import *

class OmasCompiler:
	omasFilePath = ""
	omasFile = ""
	omasFileName = ""
	lines = []
	omas_project = "empty"
	current_object = "empty"
	current_object_list = []
	count = 0
	error = OmasError()
	scope = {"activeScope":"empty","tabs":"empty"}
	varTypes = ["uid","bool","int","string","float"]
	pathTypes = "types\\"

	def __init__(self,omasFilePath,omasFileName):
		omasFile = omasFilePath+omasFileName
		omasFileOpened = open(omasFile)
		self.lines = [line.rstrip('\n') for line in omasFileOpened]
		print("LINES Array: "+str(self.lines))
		omasFileOpened.close()

	def setLine(self):
		self.count = self.count+1

	def getLine(self):
		return self.count

	def getLineStr(self):
		return self.str(count+1)

	def setScope(self,activeScope,tabs):
		self.scope["activeScope"] = activeScope
		self.scope["tabs"] = tabs

	def isInScope(self,line):
		if("\t" in line):
			firstPartLine = line.partition(' ')[0]
			#print("Scope: ",self.scope,firstPartLine.startswith(self.scope['tabs']))
			if(firstPartLine.startswith(self.scope['tabs'])):
				return True
			else:
				return False
		else:
			return False

	def isComment(self,line):
		#Comment
		#Si un comentario no esta en scope no importa
		if(line.startswith("#")):
			#print("Comment: ",line.strip('#'))
			#print("Comentario in scope",self.isInScope(line))
			return True

		elif("#" in line):
			#print(scope['tabs'],"posible comment")

			#print("Posible Comentario in scope",self.isInScope(line))
			firstPartLine = line.partition(' ')[0]
			if(self.isInScope(line)):
				lineSplit = line.split(self.scope['tabs'])
				#print("linea "+str(self.count+1),lineSplit)
			else:
				#print("#Error de tabulacion")
				self.error.add("#Error de tabulacion:","La sentencia está fuera de: "+self.scope['activeScope'],self.getLine())
				return False
			return True
		else:
			return False	

	def isProject(self,line):
		if("project" in line):
			self.omas_project = line.split(" ")[1]
			self.setScope(self.omas_project,"\t")
			return True
		else:
			return False

	def isObject(self,line):
		if("object" in line):
			if(self.scope["activeScope"]=="empty"):
				self.current_object = line.split(" ")[1]
				self.setScope(self.current_object,"\t")
				return True
			else:
				if(self.isInScope(line)):
					self.current_object = line.split(" ")[1]
					self.setScope(self.current_object,"\t\t")
					return True
				else:
					#print("#Error: objeto fuera de scope")
					self.error.add("#Error de Scope:","El objeto '"+line.split(" ")[1]+"' se encuentra fuera del scope: "+self.scope['activeScope'],self.getLine())
					return False
		else:
			return False

	def isField(self,line):

		line_split = line.split(" ")
		# print(line_split)
		print("Len: ",len(line_split))
		if(len(line_split) > 1):
			# print("Analize field")
			# print("Tabs: ",self.scope['tabs']+"e")
			# print(line_split[0])
			dataType = line_split[0].replace(self.scope['tabs'],"")
			print(dataType)
			if(dataType in self.varTypes):
				print("Campo valido")
			else:
				print("#Error en linea "+str(self.getLine())+": El tipo de dato '"+dataType+"' no está soportado.")
				self.error.add("#Error de sintaxis:","El tipo de dato '"+dataType+"' no está soportado.",self.getLine())
			return True
		else:
			clean_line = line.replace(self.scope['tabs'],"")
			print(clean_line)
			if(clean_line.startswith("_")):
				print("Campo especial")
				if os.path.exists(self.pathTypes+"special.typ"):
					print("Existen los tipos especiales.")
				else:
					print("Faltan los tipos especiales "+self.pathTypes)
					self.error.add("#Error de compilador:","Falta un archivo importante '"+self.pathTypes+"'special.typ",self.getLine())
				return True
			else:
				return False


	