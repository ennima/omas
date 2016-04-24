import os, sys

from OmasError import *

omasFilePath = ""
omasFile = omasFilePath+'user.omas'
lines = [line.rstrip('\n') for line in open(omasFile)]

omas_project = "empty"

print(lines)
count = 0
error = OmasError()
for line in lines:
	print(line)
	#first line
	if(count == 0):
		if 'project' in line:
			
			lineSplit = line.split(' ')
			omas_project = lineSplit[1]
			print("PROJECT: ",omas_project)
			if(len(lineSplit)>2):
				#print("#ERROR: El proyecto solo puede tener un nombre")
				error.add("#ProjectError:","El proyecto solo puede tener un nombre",count+1)
		else:
			#print("#ERROR: El script debe indicar a que proyecto pertenece.")
			error.add("#ProjectError:","El script debe indicar a que proyecto pertenece.",count+1)
		count+=1
error.show()