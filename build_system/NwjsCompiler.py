import os
import zipfile
from shutil import copyfile

class NwjsCompiler():

	errors = []
	log = []
	nw_name = ""

	def __init__(self):
		pass

	#private methods
	def __make_zip(self,tmp_build_path,dir_to_zip,zip_name):
		zf = zipfile.ZipFile(tmp_build_path+zip_name , "w")
		os.chdir(dir_to_zip)

		for dirname, subdirs, files in os.walk("."):
			self.log.append("dirname to zip: "+dirname.replace(dir_to_zip,""))
			if(dirname == "."):
				self.log.append("discard root dir")
			else:
				zf.write(dirname)
				for filename in files:
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
	def generate_nw(self,dir_to_zip,tmp_build_path,override=True):

		current_dir = os.getcwd()
		name_split = dir_to_zip.split("\\")
		name = name_split[(len(name_split)-2):-1]
		zip_name = name[0] + ".zip"
		

		if(os.path.exists(tmp_build_path+zip_name)):
			if(override):
				
				self.log.append("Zip Override")
				os.remove(tmp_build_path+zip_name)
				self.__make_zip(tmp_build_path,dir_to_zip,zip_name)
				self.__make_nw(tmp_build_path,dir_to_zip,zip_name,override)
				return True
			else:
				self.errors.append("Zip file "+zip_name+" already exists")
				self.log.append("Zip file "+zip_name+" already exists")
				return False
		else:
			self.__make_zip(tmp_build_path,dir_to_zip,zip_name)

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
			