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

	