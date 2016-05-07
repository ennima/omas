import os, sys, datetime, json

#projectName = input("Nombre del Projecto: ")
projectPath = "C:\\Users\\ennim_000\\Documents\\devs\\PHP\\"
projectName = "ennima/test"

projectDescription = "Test for composer"
projectType = "project"
license = "proprietary"
namespace = "Test1"
rootSrc = 'src/'
rootTest = 'tests'

author='\t{\n\t\t\t"name": "Enrique Nieto",\n\t\t\t"email": "ennima@hotmail.com"\n\t\t}'


composer_proy = "{\n\t\"name\":\"" + projectName + "\",\n\t\"description\":\""+projectDescription+"\",\n\t"
composer_proy += "\"type\":\"" + projectType + "\",\n\t\"license\":\"" + license + "\",\n\t" + "\"authors\": [\n\t" + author + "\n\t],\n\t\"require\":{},\n\t"
composer_proy += '\"autoload\":{\n\t\t\t\t"psr-4":{\n\t\t\t\t\t"'+namespace+'\\\\":"'+rootSrc+'"\n\t\t\t\t}\n\t}\n}'
print(composer_proy)

user, pname = projectName.split('/')

if not os.path.exists(projectPath):
    os.makedirs(projectPath)
else:
	print("path exists")
	default_path = projectPath+pname
	if not os.path.exists(projectPath+pname):
	    os.makedirs(default_path)
	    os.makedirs(default_path+"\\"+rootSrc)
	    os.makedirs(default_path+"\\"+rootTest)

	    comp_file = open(projectPath+pname+"\\composer.json","+w")
	    comp_file.write(composer_proy)
	    comp_file.close()
	    print(os.getcwd())
	    os.chdir(default_path)
	    print(os.getcwd())
	    os.system("composer install")
	    os.system("composer require phpunit/phpunit --dev")

	else:
		print("proy exists")


