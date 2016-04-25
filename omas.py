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


def isInScope(line,scope):
	if("\t" in line):
		#print(scope['tabs'],"fue tabulado")
		lineSplit = line.split(scope["tabs"])
		lineSplitLen = len(lineSplit)
		#print(lineSplitLen," - ",lineSplit)
		if(lineSplitLen==2):
			#print('InScope')
			return True
		else:
			#print('OutScope')
			return False
	else:
		return False

for line in lines:
	print("LINE> ",line)
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
		#Comment
		#Si un comentario no esta en scope no importa
		if(line.startswith("#")):
			print("Comment: ",line.strip('#'))
			print(isInScope(line,scope))
		elif("#" in line):
			print(scope['tabs'],"posible comment")
			print(isInScope(line,scope))				
		count+=1
print(error.show())