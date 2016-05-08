import os
class ComposerGenerator():
	projectPath = ""
	projectName = ""
	projectDescription = ""
	projectType = ""
	license = ""
	namespace = ""
	rootSrc = ""
	rootTest = ""
	author=""

	def __init__(self):
		#projectPath = "C:\\Users\\ennim_000\\Documents\\devs\\PHP\\"
		self.projectPath = "C:\\Users\\enrique.nieto\\Documents\\develops\\PHP\\"
		self.projectName = "ennima/test"
		self.projectDescription = "Test for composer"
		self.projectType = "project"
		self.license = "proprietary"
		self.namespace = "Test1"
		self.rootSrc = 'src/'
		self.rootTest = 'tests'
		self.author='\t{\n\t\t\t"name": "Enrique Nieto",\n\t\t\t"email": "ennima@hotmail.com"\n\t\t}'

	

	def emptyGen(self, pname, composerJson):
		default_path = self.projectPath+pname
		if not os.path.exists(default_path):
		    os.makedirs(default_path)
		    os.makedirs(default_path+"\\"+self.rootSrc)
		    if(self.rootTest == ""):
		    	print("No test")
		    else:
		    	os.makedirs(default_path+"\\"+self.rootTest)

		    comp_file = open(default_path+"\\composer.json","+w")
		    comp_file.write(composerJson)
		    comp_file.close()
		    print(os.getcwd())
		    os.chdir(default_path)
		    print(os.getcwd())
		    os.system("composer install")
		    return True
		else:
			print("proy exists")
			return False

	def testDrivenGen(self, pname, composerJson):
		default_path = self.projectPath+pname

		if(self.emptyGen(pname, composerJson)):
			os.system("composer require phpunit/phpunit --dev")
			return True
		else:
			return False
		

	def generateEmptyProject(self):
		composer_proy = "{\n\t\"name\":\"" + self.projectName + "\",\n\t\"description\":\"" + self.projectDescription + "\",\n\t"
		composer_proy += "\"type\":\"" + self.projectType + "\",\n\t\"license\":\"" + self.license + "\",\n\t" + "\"authors\": [\n\t" + self.author + "\n\t],\n\t\"require\":{},\n\t"
		composer_proy += '\"autoload\":{\n\t\t\t\t"psr-4":{\n\t\t\t\t\t"' + self.namespace + '\\\\":"' + self.rootSrc + '"\n\t\t\t\t}\n\t}\n}\n'
		
		return composer_proy

	def makeEmptyProject(self):
		composerJson = self.generateEmptyProject()

		user, pname = self.projectName.split('/')

		if not os.path.exists(self.projectPath):
		    os.makedirs(self.projectPath)
		    if(self.emptyGen(pname,composerJson)):
		    	return True
		else:
			print("path exists")
			if(self.emptyGen(pname,composerJson)):
				return True

		composerJson = self.generateEmptyProject()

		user, pname = self.projectName.split('/')
		if not os.path.exists(self.projectPath):
		    os.makedirs(self.projectPath)
		    if(self.testDrivenGen(pname,composerJson)):
		    	return True
		else:
			print("path exists")
			if(self.testDrivenGen(pname,composerJson)):
				return True
		


	def setProjectPath(self, newProjectPath):
		self.projectPath = newProjectPath


	def setProjectName(self, projectName):
		self.projectName = projectName


	def setProjectDescription(self, projectDescription):
		self.projectDescription = projectDescription


	def setProjectType(self, projectType):
		self.projectType = projectType


	def setLicense(self, license):
		self.license = license


	def setNamespace(self, namespace):
		self.namespace = namespace


	def setRootSrc(self, rootSrc):
		self.rootSrc = rootSrc


	def setRootTest(self, rootTest):
		self.rootTest = rootTest


	def setAuthor(self, author):
		self.author = author


