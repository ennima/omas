import sys
import unittest
sys.path.append('../')
sys.path.append('../db')

from pyCompilerWin import *

class test_pyCompilerWin(unittest.TestCase):
	
	def test_it_should_be_able_to_construct(self):
		compiler = pyCompilerWin()
		self.assertIsInstance(compiler,pyCompilerWin,"Es instancia")
		print(compiler.template_setup)
		#compiler.copy_to_dist()
		#compiler.make_setup(compiler.build_path+compiler.build_dist+"\\")
		compiler.load_config("C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\build_system\\pyCompilerWin_sample_project.json")
		print("TEst: ",compiler.build_script_lib)

		
if __name__ == '__main__':
    unittest.main()