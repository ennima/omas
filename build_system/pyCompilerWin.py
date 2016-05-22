import os, sys, subprocess

sys.path.append('lib')

from Template import *

templater = Template()

template_setup = "py_setup.py"
build_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\Node\\ticker\\dist\\"
build_script = "open_server.py"
build_script_lib ="lib"


templater.vars_change=[{"var":"program_py","val":build_script}]
if(templater.load(template_setup)):
	print("Cargado")
	templater.change()
	templater.save(build_path+"setup.py")

	os.chdir(build_path)
	print(os.getcwd())
	os.system("python setup.py py2exe")
	#subprocess.call(['python','setup.py py2exe'],shell=True)
else:
	print("Error al cargar el template")
