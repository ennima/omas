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
	count = 0
	error = OmasError()
	scope = {"activeScope":"","tabs":""}
	varTypes = ["uid","bool","int","string","float"]

	def __init__(self,omasFilePath,omasFileName):
		omasFile = omasFilePath+omasFileName
		omasFileOpened = open(omasFile)
		lines = [line.rstrip('\n') for line in omasFileOpened]
		print(lines)
		omasFileOpened.close()

	def getLine(self):
		return self.count+1

	def getLineStr(self):
		return self.str(count+1)

	def setScope(self,activeScope,tabs):
		self.scope["activeScope"] = activeScope
		self.scope["tabs"] = tabs

	def isInScope(self,line):
		if("\t" in line):
			firstPartLine = line.partition(' ')[0]
			print("Scope: ",self.scope,firstPartLine.startswith(self.scope['tabs']))
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
				print("#Error de tabulacion")
				self.error.add("#Error de tabulacion:","La sentencia está fuera de: "+self.scope['activeScope'],self.getLine)
				return False
			return True
		else:
			return False	



	