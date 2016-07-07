import sys
import unittest
sys.path.append('../generators/')

from Template import *

#filesPath = 'C:\\Users\\ennim_000\\Documents\\devs\\omas\\generators\\presets\\'
filesPath = 'C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\generators\\presets\\'

class TemplateTest(unittest.TestCase):

	def test_it_should_be_able_to_construct(self):

		templater = Template()
		self.assertIsInstance(templater,Template,"Es Instancia")

	def test_it_should_be_able_when_template_is_loaded(self):
		templater = Template()
		self.assertTrue(templater.load(filesPath+"src\\templater.txt"))

	def test_it_should_be_able_when_template_is_not_loaded(self):
		templater = Template()
		self.assertFalse(templater.load("templater.txt"))


	def test_it_should_be_able_when_template_is_modified(self):
		templater = Template()
		if(templater.load(filesPath+"templater.txt")):
			self.assertTrue(templater.change())

	def test_it_make_new_file_var_changed(self):
		templater = Template()
		templater.load(filesPath+"src\\templater.txt")
		templater.change()
		self.assertTrue(templater.save(filesPath+"render\\templateado.txt"))

if __name__ == '__main__':
    unittest.main()