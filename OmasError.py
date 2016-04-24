import sys
class OmasError():
	"""docstring for OmasError"""
	count = 0
	def __init__(self):
		pass

	def add(self,typeError,message,line):
		self.count+=1
		logString = typeError+" "+message+" "+"on line"+" "+str(line)
		#print(logString)
		#sys.exit()
		return logString

	def show(self):
		#print("# Se encontraron ",self.count,"errores.")
		logString = "# Se encontraron "+str(self.count)+" errores."
		return logString

	def getTotalErrors(self):
		return self.count

	def haveErrors(self):
		if(self.count>0):
			return True
		else:
			return False