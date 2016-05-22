import os, sys, subprocess, json
from shutil import copyfile


sys.path.append('lib')
from Template import *

class pyCompilerWin():

	def __init__(self):
		self.templater = Template()
		self.template_setup = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\build_system\\py_setup.py"
		self.build_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\Node\\ticker\\dist\\"
		self.build_script = "open_server.py"
		self.build_script_lib ="lib"
		
		self.dependences_path = self.build_path + "depend\\"
		self.build_dist = self.build_script.split(".")[0]+"_dist"

	def copy_to_dist(self):
		print("Copy files of "+self.build_script+" to",self.build_path+self.build_dist)
		with open(self.build_path+self.build_script) as script:
			line_count = 0
			in_lib = False
			for line in script:
				print(line_count,line)
				line_count += 1
				if(("sys.path.append('"+self.build_script_lib+"')") in line):
					print("##### Dentro de lib")
					in_lib = True
				elif("#end "+self.build_script_lib+" imports" in line):
					print("##### Fuera de lib ")
					in_lib = False
					break
				elif(in_lib):
					if(line.startswith("from")):
						print("class lib")
						lineSplit = line.split(" ")
						src = self.build_path+self.build_script_lib+"\\"+lineSplit[1]+".py"
						dest = self.build_path+self.build_dist+"\\"+lineSplit[1]+".py"
						dest_path = self.build_path+self.build_dist
						print(src,"to",dest)
						if(os.path.exists(dest_path)):
							copyfile(src,dest)
						else:
							print("Making dest: ", dest_path)
							os.mkdir(dest_path)
							copyfile(src,dest)
					elif(line.startswith("import")):
						print("is ordinary lib")

		src = self.build_path + self.build_script
		dest = self.build_path + self.build_dist + "\\"+ self.build_script
		copyfile(src,dest)

	def make_setup(self,build_path):

		self.templater.vars_change=[{"var":"program_py","val":self.build_script}]
		os.chdir(build_path)
		if(self.templater.load(self.template_setup)):
			print("Cargado")
			self.templater.change()
			self.templater.save(build_path+"setup.py")

			
			print(os.getcwd())
			os.system("python setup.py py2exe")
			
		else:
			print("Error al cargar el template: ",os.getcwd()," -> ",self.template_setup)

	def load_config(self,config_file):
		with open(config_file,"r") as load_data:
			json_conf = json.load(load_data)

			print(json_conf["dependences_path"])

			self.template_setup = json_conf["template_setup"]
			self.build_path = json_conf["build_path"]
			self.build_script = json_conf["build_script"]
			self.build_script_lib = json_conf["build_script_lib"]

			self.dependences_path = self.build_path + json_conf["dependences_path"] + "\\"