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
		

		jsonReturn = '{\n\t\"name":"ennima/test",\n\t\"description":"Test for composer",\n\t"type":"project",\n\t"license":"proprietary",\n\t"authors": [\n\t\t{\n\t\t\t"name": "Enrique Nieto",\n\t\t\t"email": "ennima@hotmail.com"\n\t\t}\n\t],\n\t"require":{},\n\t"autoload":{\n\t\t\t\t"psr-4":{\n\t\t\t\t\t"Test1\\\\":"src/"\n\t\t\t\t}\n\t}\n}\n'

		print("###### \n",jsonReturn)
		self.assertEqual(generator.generateEmptyProject(),jsonReturn)
		


if __name__ == '__main__':
    unittest.main()