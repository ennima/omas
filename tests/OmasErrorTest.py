import sys
import unittest
sys.path.append('..\\skeleton\\')
from OmasError import *
class OmasErrorTest(unittest.TestCase):
	
	def test_add_error(self):
		error = OmasError()
		self.assertEqual(error.add("error:","syntax error",2),"error: syntax error on line 2")
		error.reset()
		print(error.errorList)


	def test_show_actual_errors_when_erros_found(self):
		error = OmasError();
		error.add("Error:","Syntax Error",1)
		error.add("Error:","Syntax Error",5)
		error.add("Error:","Syntax Error",8)
		error.add("Error:","Syntax Error",12)
		self.assertEqual(error.show(),"# Se encontraron 4 errores.")


	def test_show_actual_errors_when_no_erros_found(self):
		error = OmasError();
		self.assertEqual(error.show(),"# Se encontraron 0 errores.")


	def test_return_total_errors_no_errors_found(self):
		error = OmasError()
		self.assertEqual(error.getTotalErrors(),0)


	def test_return_total_errors_when_errors_found(self):
		error = OmasError()
		error.add("Error:","Syntax Error",200)
		error.add("Error:","Syntax Error",500)
		self.assertEqual(error.getTotalErrors(),2)
		error.reset()
		print(error.errorList)


	def test_should_be_able_when_have_errors(self):
		error = OmasError()
		error.add("Error:","Syntax Error",20)
		self.assertTrue(error.haveErrors())
		error.reset()
		print(error.errorList)


	def test_should_be_able_when_have_not_errors(self):
		error = OmasError()
		self.assertFalse(error.haveErrors())
	

	def test_should_be_able_when_have_error_and_return_list(self):
		error = OmasError()
		error.reset()
		error.add("Error:","Syntax Error 113",113)
		self.assertEqual(error.getListErrors(),[{'line': 113, 'logString': 'Error: Syntax Error 113 on line 113'}])
		

if __name__ == '__main__':
    unittest.main()