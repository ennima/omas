import os
import zipfile
from shutil import copyfile

class NwjsCompiler():

	errors = []
	log = []
	
	nw_name = ""
	exe_name = ""
	run_build_path = ""
	tmp_build_path = ""
	nw_engine_name =""

	def __init__(self):
		self.nw_engine_name = "nw.exe"

	#private methods
	def make_zip(self,tmp_build_path,dir_to_zip,zip_name):

		zf = zipfile.ZipFile(tmp_build_path+zip_name , "w")
		os.chdir(dir_to_zip)

		for dirname, subdirs, files in os.walk("."):
			self.log.append("dirname to zip: "+dirname.replace(dir_to_zip,""))
			#print("dirname to zip: "+dirname.replace(dir_to_zip,""))
			if(dirname == "."):
				self.log.append("discard root dir")
			else:
				zf.write(dirname)
			for filename in files:
				#print(os.path.join(dirname, filename))
				zf.write(os.path.join(dirname, filename))
		zf.close()
		self.log.append(tmp_build_path+zip_name+" it's done")


	def __make_nw(self,tmp_build_path,dir_to_zip,zip_name,override=True):
		file_nw = zip_name.replace(".zip",".nw")
		self.log.append("Making nw: "+file_nw)
		
		if(os.path.exists(tmp_build_path+file_nw)):
			if(override):
				self.log.append("nw Override")
				os.remove(tmp_build_path+file_nw)
				os.rename(tmp_build_path+zip_name,tmp_build_path+file_nw)
				self.nw_name = file_nw
				self.log.append(tmp_build_path+file_nw+" it's done in override mode")
				return True
			else:
				self.log.append(tmp_build_path+file_nw+" already exists")
				self.errors.append(tmp_build_path+file_nw+" already exists")
				self.nw_name = None
				return False
		else:
			os.rename(tmp_build_path+zip_name,tmp_build_path+file_nw)
			self.nw_name = file_nw
			self.log.append(tmp_build_path+file_nw+" it's done")
			return True


	#public methods
	def set_run_build_path(run_build_path):
		self.run_build_path = run_build_path

	def generate_nw(self,dir_to_zip,tmp_build_path,override=True):
		self.tmp_build_path = tmp_build_path
		current_dir = os.getcwd()
		name_split = dir_to_zip.split("\\")
		name = name_split[(len(name_split)-2):-1]
		zip_name = name[0] + ".zip"
		
		self.log.append("Generting mw")
		if(os.path.exists(tmp_build_path+zip_name)):
			if(override):
				
				self.log.append("Zip Override")
				os.remove(tmp_build_path+zip_name)
				self.make_zip(tmp_build_path,dir_to_zip,zip_name)
				self.__make_nw(tmp_build_path,dir_to_zip,zip_name,override)
				return True
			else:
				self.errors.append("Zip file "+zip_name+" already exists")
				self.log.append("Zip file "+zip_name+" already exists")
				return False
		else:
			self.make_zip(tmp_build_path,dir_to_zip,zip_name)

			file_nw = zip_name.replace(".zip",".nw")
			if (os.path.exists(tmp_build_path+file_nw)):
				
				if(override):
					os.chdir(current_dir)
					os.remove(tmp_build_path+file_nw)
					self.__make_nw(tmp_build_path,dir_to_zip,zip_name,override)
					self.log.append("The nw "+file_nw+" it's done")
					return True
				else:
					self.errors.append("Nw file "+file_nw+" already exists")
					self.log.append("Nw file "+file_nw+" already exists")
					return False
			else:
				os.chdir(current_dir)
				self.__make_nw(tmp_build_path,dir_to_zip,zip_name,override)
				self.log.append("The nw "+file_nw+" it's done")
				return True
			


	def prebuild(self):
		self.log.append("Begin run process")
		os.chdir(self.run_build_path)
		exe_file = self.nw_name.replace(".nw",".exe")
		self.exe_name = exe_file
		if(os.path.exists(self.run_build_path+self.nw_name)):
			#print("Override "+self.run_build_path+self.nw_name)
			self.log.append("Override "+self.run_build_path+self.nw_name)
			os.remove(self.run_build_path+self.nw_name)
		
		if(os.path.exists(self.tmp_build_path+self.nw_name)):
			#print("copiando: "+self.tmp_build_path+self.nw_name+" a "+self.run_build_path+self.nw_name)
			self.log.append("copiando: "+self.tmp_build_path+self.nw_name+" a "+self.run_build_path+self.nw_name)
			os.rename(self.tmp_build_path+self.nw_name,self.run_build_path+self.nw_name)
		else:
			#print("No se pudo copiar: "+self.tmp_build_path+self.nw_name)
			self.log.append("No se pudo copiar: "+self.tmp_build_path+self.nw_name)
			self.errors.append("No se pudo copiar: "+self.tmp_build_path+self.nw_name)
		if(os.path.exists(self.run_build_path+exe_file)):
			self.log.append("Override "+self.run_build_path+exe_file)
			os.remove(self.run_build_path+exe_file)

		self.log.append("Making "+self.run_build_path+exe_file)
		#print("copy /b "+self.nw_engine_name+"+"+self.nw_name+" "+exe_file)
		os.system("copy /b "+self.nw_engine_name+"+"+self.nw_name+" "+exe_file)

		return True

	def run(self):
		print("Runing App: "+self.exe_name)
		os.system(self.exe_name)
		print("App exit")
