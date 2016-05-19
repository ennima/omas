import os
from shutil import copyfile
import zipfile


#Sys path to build

sys_path_to_build = "C:\\Users\\enrique.nieto\\Documents\\develops\\Nwjs\\build\\"

sys_path_to_dist = "C:\\Users\\enrique.nieto\\Documents\\develops\\Nwjs\\dist\\"

current_dir = os.getcwd()
dir_to_zip = "nwjs_app"
zip_name = dir_to_zip + ".zip"
count = 0

zf = zipfile.ZipFile(zip_name , "w")
os.chdir(dir_to_zip)

for dirname, subdirs, files in os.walk("."):
	print(dirname.replace(dir_to_zip,""))
	if(dirname == "."):
		print("omitir")
	else:
		zf.write(dirname)
	for filename in files:
		zf.write(os.path.join(dirname, filename))
zf.close()

os.chdir(current_dir)

file_nw = zip_name.replace(".zip",".nw")
os.rename(zip_name,sys_path_to_build+file_nw)

os.chdir(sys_path_to_build)

exe_file = dir_to_zip+".exe"

os.system("copy /b nw.exe+"+file_nw+" "+exe_file)

copyfile(exe_file,sys_path_to_dist+exe_file)
