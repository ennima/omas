import sys
import unittest
sys.path.append('../comp_gen/')
from ComposerGenerator import *

class ComposerGeneratorTest(unittest.TestCase):

	def test_it_should_be_able_to_construct(self):
		generator = ComposerGenerator()
		self.assertIsInstance(generator,ComposerGenerator,"Es instancia")

	def test_it_should_be_able_to_generate_json_project_default_settings(self):
		generator = ComposerGenerator()
		
		#Default settings in class
		projectPath = "C:\\Users\\enrique.nieto\\Documents\\develops\\PHP\\"
		projectName = "ennima/test"
		projectDescription = "Test for composer"
		projectType = "project"
		license = "proprietary"
		namespace = "Test1"
		rootSrc = 'src/'
		rootTest = 'tests'
		author='\t{\n\t\t\t"name": "Enrique Nieto",\n\t\t\t"email": "ennima@hotmail.com"\n\t\t}'

		jsonReturn = "{\n\t\"name\":\"" + projectName + "\",\n\t\"description\":\"" + projectDescription + "\",\n\t"
		jsonReturn += "\"type\":\"" + projectType + "\",\n\t\"license\":\"" + license + "\",\n\t" + "\"authors\": [\n\t" + author + "\n\t],\n\t\"require\":{},\n\t"
		jsonReturn += '\"autoload\":{\n\t\t\t\t"psr-4":{\n\t\t\t\t\t"' + namespace + '\\\\":"' + rootSrc + '"\n\t\t\t\t}\n\t}\n}\n'

		self.assertEqual(generator.generateEmptyProject(),jsonReturn)
		

	def test_it_should_be_able_to_generate_json_project_new_settings(self):
		generator = ComposerGenerator()

		generator.setProjectPath("C:\\Path\\")
		generator.setProjectName("corp/test")
		generator.setProjectDescription("New test for composer")
		generator.setProjectType("project")
		generator.setLicense("MIT")
		generator.setNamespace("Corp")
		generator.setRootSrc("code/src/")
		author='\t{\n\t\t\t"name": "Enrique Nieto Martínez",\n\t\t\t"email": "ennima@hotmail.com"\n\t\t}'
		generator.setAuthor(author)

		jsonReturn = "{\n\t\"name\":\"" + "corp/test" + "\",\n\t\"description\":\"" + "New test for composer" + "\",\n\t"
		jsonReturn += "\"type\":\"" + "project" + "\",\n\t\"license\":\"" + "MIT" + "\",\n\t" + "\"authors\": [\n\t" + author + "\n\t],\n\t\"require\":{},\n\t"
		jsonReturn += '\"autoload\":{\n\t\t\t\t"psr-4":{\n\t\t\t\t\t"' + "Corp" + '\\\\":"' + "code/src/" + '"\n\t\t\t\t}\n\t}\n}\n'

		self.assertEqual(generator.generateEmptyProject(),jsonReturn)

	def test_it_should_be_able_to_generate_json_project_default_settings_empty_no_test(self):
		generator = ComposerGenerator()
		generator.setRootTest("")
		self.assertTrue(generator.makeEmptyProject())

	def test_it_should_be_able_to_generate_json_project_default_settings_empty_no_test_but_exists_project(self):
		generator = ComposerGenerator()
		generator.setRootTest("")
		self.assertFalse(generator.makeEmptyProject())

	

	def test_it_should_be_able_to_generate_json_project_empty_no_test(self):
		generator = ComposerGenerator()
		generator.setRootTest("")
		generator.setProjectName("ennima/testA")
		generator.setNamespace("Corp")
		self.assertTrue(generator.makeEmptyProject())

	def test_it_should_be_able_to_generate_json_project_empty_no_test_but_project_exists(self):
		generator = ComposerGenerator()
		generator.setRootTest("")
		generator.setProjectName("ennima/testA")
		generator.setNamespace("Corp")
		self.assertFalse(generator.makeEmptyProject())

	

	def test_it_should_be_able_to_generate_json_project_default_settings_test_driven(self):
		generator = ComposerGenerator()
		self.assertTrue(generator.makeTestDrivenProject())

	def test_it_should_be_able_to_generate_json_project_default_settings_test_driven_but_project_exists(self):
		generator = ComposerGenerator()
		self.assertFalse(generator.makeTestDrivenProject())

	

	def test_it_should_be_able_to_generate_json_project_new_settings_test_driven(self):
		generator = ComposerGenerator()
		generator.setProjectPath("C:\\Users\\enrique.nieto\\Documents\\develops\\PHP\\PHP2\\")
		self.assertTrue(generator.makeTestDrivenProject())

	def test_it_should_be_able_to_generate_json_project_new_settings_test_driven_but_project_exists(self):
		generator = ComposerGenerator()
		generator.setProjectPath("C:\\Users\\enrique.nieto\\Documents\\develops\\PHP\\PHP2\\")
		self.assertFalse(generator.makeTestDrivenProject())


if __name__ == '__main__':
    unittest.main()