import sys
import unittest
sys.path.append('../')
from OmasCompiler import *
PATH_OMAS = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\"
class OmasCompilerTest(unittest.TestCase):
	
	def test_it_should_be_able_to_construct(self):
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		self.assertIsInstance(compiler,OmasCompiler,"Es instancia")

	def test_should_return_one_when_counting_lines(self):
		#getLine returns the line that the compiler is processing
		#in this case is ready for read line number one
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		self.assertEqual(compiler.getLine(),1)


if __name__ == '__main__':
    unittest.main()