import sys
class OmasError():
	"""Class for errors"""
	count = 0
	errorList = []
	

	def __init__(self):
		pass

	def add(self,typeError,message,line):
		self.count+=1
		logString = typeError+" "+message+" "+"on line"+" "+str(line)
		self.errorList.append({"logString":logString,"line":line})

		#print(logString)
		#sys.exit()
		return logString

	def show(self):
		#print("# Se encontraron ",self.count,"errores.")
		logString = "# Se encontraron "+str(self.count)+" errores."
		return logString

	def reset(self):
		self.errorList = []
		self.count = 0

	def getTotalErrors(self):
		return self.count

	def haveErrors(self):
		if(self.count>0):
			return True
		else:
			return False

	def getListErrors(self):
		return self.errorList
