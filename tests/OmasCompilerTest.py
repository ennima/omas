import sys, os
import unittest
sys.path.append('..\\skeleton\\')
from OmasCompiler import *
PATH_OMAS = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\skeleton\\samples\\"
class OmasCompilerTest(unittest.TestCase):
	
	# def test_it_should_be_able_to_construct(self):
	# 	compiler = OmasCompiler(PATH_OMAS,'user.omas')
	# 	self.assertIsInstance(compiler,OmasCompiler,"Es instancia")

	# def test_should_return_one_when_counting_lines(self):
	# 	#getLine returns the line that the compiler is processing
	# 	#in this case is ready for read line number one
	# 	compiler = OmasCompiler(PATH_OMAS,'user.omas')

	# 	self.assertEqual(compiler.getLine(),1)

	# def test_returns_true_if_the_tabulation_is_correct(self):
	# 	line = "	#clase usuario"
	# 	compiler = OmasCompiler(PATH_OMAS,'user.omas')
	# 	compiler.setScope("project","\t")
	# 	self.assertTrue(compiler.isInScope(line))

	# def test_returns_true_if_the_tabulation_is_correct(self):
	# 	line = "	#clase usuario"
	# 	compiler = OmasCompiler(PATH_OMAS,'user.omas')
	# 	compiler.setScope("project","\t")
	# 	self.assertTrue(compiler.isInScope(line))

	# def test_returns_false_if_the_tabulation_is_not_correct(self):
	# 	line = "as	#clase usuario"
	# 	compiler = OmasCompiler(PATH_OMAS,'user.omas')
	# 	compiler.setScope("project","\t")
	# 	self.assertFalse(compiler.isInScope(line))

	# def test_returns_true_if_the_line_is_valid_comment(self):
	# 	line = "	#clase usuario"
	# 	compiler = OmasCompiler(PATH_OMAS,'user.omas')
	# 	self.assertTrue(compiler.isComment(line))

	# def test_returns_false_if_the_line_is_not_valid_comment(self):
	# 	line = "as	clase usuario"
	# 	compiler = OmasCompiler(PATH_OMAS,'user.omas')
	# 	#compiler.setScope("project","\t")
	# 	self.assertFalse(compiler.isComment(line))

	# def test_returns_false_if_the_line_is_not_valid_tabulation_comment(self):
	# 	line = "as #clase usuario"
	# 	compiler = OmasCompiler(PATH_OMAS,'user.omas')
	# 	compiler.setScope("project","\t")
	# 	valida = compiler.isComment(line)
	# 	print(compiler.error.show())
	# 	self.assertFalse(valida)
		
	def test_run_script(self):
		compiler = OmasCompiler(PATH_OMAS,'user.omas')
		compiler.pathTypes = os.getcwd().replace("tests","") + "skeleton\\" + compiler.pathTypes

		print(compiler.pathTypes)

		if(compiler.debug()):
			print("--- El build fue exitoso :) ---")
		else:
			print("--- Hay errores :( ---")
			print(compiler.error.getListErrors())
			
		# compiler.setScope("user","\t\t")
		# compiler.setLine()
		# line="		strings 50 name"
		# compiler.isField(line)

		# for line in compiler.lines:
		# 	compiler.setLine()
		# 	print(compiler.getLine(),line)
		# 	if(compiler.isProject(line)):
		# 		print("Pertenece a ",compiler.omas_project)
		# 	elif(compiler.isObject(line)):
		# 		print("Es un objeto\n")
		# 	elif(compiler.isInScope(line)):
		# 		print("Dentro de ",compiler.scope["activeScope"])
		# 		if(compiler.isComment(line)):
		# 			print("Es un comentario")
		# 		elif(compiler.isField(line)):
		# 			print("Es un campo\n")
		# 	elif(not compiler.isInScope(line)):
		# 		compiler.error.add("#Error de Scope:","Fuera de scope en linea "+str(compiler.getLine()),compiler.getLine())
		# 		#print("#Error: Fuera de scope en linea "+str(compiler.getLine()))
		# 		break

		# if(compiler.error.haveErrors()):
		# 	print(compiler.error.show())
		# 	print(compiler.error.getListErrors())
		# else:
		# 	print("--- El build fue exitoso :) ---")

		print(os.getcwd().replace("tests",""))

if __name__ == '__main__':
    unittest.main()