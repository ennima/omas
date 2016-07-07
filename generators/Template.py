############################################################################
#
# Author: Enrique Nieto
# Start: 08-05-2016
# Description: First Version of Template that replace strings in file.
#
############################################################################
import os, sys

class Template():
	template_src ="templater.txt"
	template = ""
	vars_change = ""
	templateFinal = ""
	def __init__(self):

		self.vars_change = [
				{"var":"is","val":"was"},
				{"var":"name","val":"Enrique"},
				{"var":"verv","val":"Great"},
			  ] 

	def load(self, *args):
		if (len(args) == 1 and isinstance(args[0],str)):
			self.template_src = args[0]
			print("Load ",self.template_src)

		if(os.path.exists(self.template_src)):
			with open(self.template_src, 'r') as f:
				self.template = f.read()

			if(self.template != ""):
				return True
			else:
				return False
		else:
			return False

	def change(self):
		for change_var in self.vars_change:
			self.template = self.template.replace("{"+change_var["var"]+"}",change_var["val"])
			
		#print(self.template)
		return True

	def save(self, *args):
		if (len(args) == 1 and isinstance(args[0],str)):
			self.templateFinal = args[0]
			print("save ",self.templateFinal)

		print("#---- path: "+os.path.dirname(self.templateFinal))
		if(os.path.exists(os.path.dirname(self.templateFinal))):
			print("Existe: "+os.path.dirname(self.templateFinal))
		else:
			print("Falta: "+os.path.dirname(self.templateFinal))
			os.makedirs(os.path.dirname(self.templateFinal))
		
		if(not os.path.exists(self.templateFinal)):
			print("##---No existe: "+self.templateFinal)
			
			try:

				file = open(self.templateFinal,"w+")

				file.close()
			except:
				print("error occured")
				sys.exit(0)
		else:
			print("##---- Existe: ",self.templateFinal)
			with open(self.templateFinal, 'w') as f:
					f.write(self.template)
					return True


	def setTemplateSrc(self,template_src):
		self.template_src = template_src

	def setVarsChange(self,vars_change):
		self.vars_change = vars_change