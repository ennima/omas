import sys
import unittest
sys.path.append('../')
from OmasCompiler import *
PATH_OMAS = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\"
class OmasCompilerTest(unittest.TestCase):
	
	def test_it_should_be_able_to_construct(self):
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		self.assertIsInstance(compiler,OmasCompiler,"Es instancia")


if __name__ == '__main__':
    unittest.main()