import sys
import unittest
sys.path.append('../')
sys.path.append('../lib')

from pyCompilerWin import *

class test_pyCompilerWin(unittest.TestCase):
	
	def test_it_should_be_able_to_construct(self):
		compiler = pyCompilerWin()
		self.assertIsInstance(compiler,pyCompilerWin,"Es instancia")
		print(compiler.template_setup)
		compiler.copy_to_dist()
		compiler.make_setup(compiler.build_path+compiler.build_dist+"\\")

if __name__ == '__main__':
    unittest.main()