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

	def test_returns_true_if_the_tabulation_is_correct(self):
		line = "	#clase usuario"
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		compiler.setScope("project","\t")
		self.assertTrue(compiler.isInScope(line))

	def test_returns_true_if_the_tabulation_is_correct(self):
		line = "	#clase usuario"
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		compiler.setScope("project","\t")
		self.assertTrue(compiler.isInScope(line))

	def test_returns_false_if_the_tabulation_is_not_correct(self):
		line = "as	#clase usuario"
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		compiler.setScope("project","\t")
		self.assertFalse(compiler.isInScope(line))

	def test_returns_true_if_the_line_is_valid_comment(self):
		line = "	#clase usuario"
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		self.assertTrue(compiler.isComment(line))

	def test_returns_false_if_the_line_is_not_valid_comment(self):
		line = "as	clase usuario"
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		#compiler.setScope("project","\t")
		self.assertFalse(compiler.isComment(line))

	def test_returns_false_if_the_line_is_not_valid_tabulation_comment(self):
		line = "as #clase usuario"
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		compiler.setScope("project","\t")
		valida = compiler.isComment(line)
		print(compiler.error.show())
		self.assertFalse(valida)
		

if __name__ == '__main__':
    unittest.main()