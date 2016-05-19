import sys
import unittest
sys.path.append('../')
from NwjsCompiler import *


sys_path_to_build = "C:\\Users\\enrique.nieto\\Documents\\develops\\Nwjs\\build\\"
sys_path_to_dist = "C:\\Users\\enrique.nieto\\Documents\\develops\\Nwjs\\dist\\"
sys_project_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\build_system\\nwjs_app\\"
sys_tmp_build_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\build_system\\tmp\\"

class test_NwjsCompiler(unittest.TestCase):
	
	# def test_it_should_be_able_to_construct(self):
	# 	compiler = NwjsCompiler()
	# 	self.assertIsInstance(compiler,NwjsCompiler,"Es instancia")

	# def test_it_should_return_true_if_nw_is_do_it_not_override(self):
	# 	compiler = NwjsCompiler()
	# 	self.assertTrue(compiler.generate_nw(sys_project_path,sys_tmp_build_path,False))

	# def test_it_should_return_false_if_nw_is_do_it_not_override(self):
	# 	compiler = NwjsCompiler()
	# 	self.assertFalse(compiler.generate_nw(sys_project_path,sys_tmp_build_path,False))

	def test_it_should_return_true_if_nw_its_done_it_override(self):
		compiler = NwjsCompiler()
		self.assertTrue(compiler.generate_nw(sys_project_path,sys_tmp_build_path,True))
		print("  #Errors: ",compiler.log)
if __name__ == '__main__':
    unittest.main()