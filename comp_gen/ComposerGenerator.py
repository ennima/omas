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


	def generateEmptyProject(self):
		composer_proy = "{\n\t\"name\":\"" + self.projectName + "\",\n\t\"description\":\"" + self.projectDescription + "\",\n\t"
		composer_proy += "\"type\":\"" + self.projectType + "\",\n\t\"license\":\"" + self.license + "\",\n\t" + "\"authors\": [\n\t" + self.author + "\n\t],\n\t\"require\":{},\n\t"
		composer_proy += '\"autoload\":{\n\t\t\t\t"psr-4":{\n\t\t\t\t\t"' + self.namespace + '\\\\":"' + self.rootSrc + '"\n\t\t\t\t}\n\t}\n}\n'
		print(composer_proy)
