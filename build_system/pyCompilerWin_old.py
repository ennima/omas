import os, sys, subprocess
from shutil import copyfile


sys.path.append('lib')
from Template import *


templater = Template()
template_setup = "py_setup.py"
build_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\Node\\ticker\\dist\\"
build_script = "open_server.py"
build_script_lib ="lib"
dependences_path = build_path + "depend\\"

build_dist = build_script.split(".")[0]+"_dist"

def copy_dependences():


def copy_to_dist():
	print("Copy files of "+build_script+" to",build_path+build_dist)
	with open(build_path+build_script) as script:
		line_count = 0
		in_lib = False
		for line in script:
			print(line_count,line)
			line_count += 1
			if(("sys.path.append('"+build_script_lib+"')") in line):
				print("##### Dentro de lib")
				in_lib = True
			elif("#end "+build_script_lib+" imports" in line):
				print("##### Fuera de lib ")
				in_lib = False
				break
			elif(in_lib):
				if(line.startswith("from")):
					print("class lib")
					lineSplit = line.split(" ")
					src = build_path+build_script_lib+"\\"+lineSplit[1]+".py"
					dest = build_path+build_dist+"\\"+lineSplit[1]+".py"
					dest_path = build_path+build_dist
					print(src,"to",dest)
					if(os.path.exists(dest_path)):
						copyfile(src,dest)
					else:
						print("Making dest: ", dest_path)
						os.mkdir(dest_path)
						copyfile(src,dest)
				elif(line.startswith("import")):
					print("is ordinary lib")

	src = build_path + build_script
	dest = build_path + build_dist +"\\"+build_script
	copyfile(src,dest)

def make_setup(build_path):

	templater.vars_change=[{"var":"program_py","val":build_script}]
	if(templater.load(template_setup)):
		print("Cargado")
		templater.change()
		templater.save(build_path+"setup.py")

		os.chdir(build_path)
		print(os.getcwd())
		os.system("python setup.py py2exe")
		
	else:
		print("Error al cargar el template")


copy_to_dist()
make_setup(build_path+build_dist+"\\")