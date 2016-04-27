import os, sys

from OmasError import *

omasFilePath = ""
omasFile = omasFilePath+'user.omas'
lines = [line.rstrip('\n') for line in open(omasFile)]

omas_project = "empty"

print(lines)
count = 0
error = OmasError()
scope = {"activeScope":"","tabs":""}
varTypes = ["uid","bool","int","string","float"]

def getLine(count):
	return count+1
def getLineStr(count):
	return str(count+1)
	
def isInScope(line,scope):
	if("\t" in line):
		
		firstPartLine = line.partition(' ')[0]
		#print(firstPartLine)
		#print(scope in firstPartLine)
		print("Scope: ",scope,firstPartLine.startswith(scope['tabs']))
		if(firstPartLine.startswith(scope['tabs'])):
			#print("En el scope")
			return True
		else:
			#print("#Fuera del scope")

			return False
		#print(scope['tabs'],"fue tabulado")
		'''lineSplit = line.split(scope["tabs"])
		lineSplitLen = len(lineSplit)
		#print(lineSplitLen," - ",lineSplit)
		if(lineSplitLen==2):
			#print('InScope')
			return True
		else:
			#print('OutScope')
			return False'''
	else:
		return False
def isComment(line):
	#Comment
	#Si un comentario no esta en scope no importa
	if(line.startswith("#")):
		#print("Comment: ",line.strip('#'))
		print("Comentario in scope",isInScope(line,scope))
		return True
	elif("#" in line):
		#print(scope['tabs'],"posible comment")

		print("Posible Comentario in scope",isInScope(line,scope))
		firstPartLine = line.partition(' ')[0]
		if(isInScope(line,scope)):
			lineSplit = line.split(scope['tabs'])
			print("linea "+str(count+1),lineSplit)
		else:
			print("#Error de tabulacion")
		return True
	else:
		return False	
def isObject(line):
	pass

for line in lines:
	print("LINE>"+str(count+1),line)
	#first line
	if(count == 0):
		if 'project' in line:
			scope["tabs"]+="\t"
			scope["activeScope"] = "project"
			print(scope)
			lineSplit = line.split(' ')
			omas_project = lineSplit[1]
			#print("PROJECT: ",omas_project)
			activeScope = "project"
			if(len(lineSplit)>2):
				#print("#ERROR: El proyecto solo puede tener un nombre")
				print(error.add("#ProjectError:","El proyecto solo puede tener un nombre",count+1))
		else:
			#print("#ERROR: El script debe indicar a que proyecto pertenece.")
			print(error.add("#ProjectError:","El script debe indicar a que proyecto pertenece.",count+1))
		count+=1
	else:
		
		if(isComment(line)):
			print("Comment")
		elif(isObject(line)):
			pass
		
		count += 1

print(error.show())