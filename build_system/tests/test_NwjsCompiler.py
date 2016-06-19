import sys
import unittest
sys.path.append('../')

from NwjsCompiler import *


# sys_path_to_build = "C:\\Users\\enrique.nieto\\Documents\\develops\\Nwjs\\build\\"
# sys_path_to_dist = "C:\\Users\\enrique.nieto\\Documents\\develops\\Nwjs\\dist\\"
# sys_project_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\build_system\\nwjs_app\\"
# sys_tmp_build_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\build_system\\tmp\\"


sys_path_to_build = "C:\\Users\\enrique.nieto\\Documents\\develops\\Nwjs\\build\\"
sys_path_to_dist = "C:\\Users\\enrique.nieto\\Documents\\develops\\Nwjs\\dist\\"
sys_project_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\Node\\ticker\\frontApp\\"
sys_tmp_build_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\Node\\ticker\\tmp\\"


class test_NwjsCompiler(unittest.TestCase):
	
	# def test_it_should_be_able_to_construct(self):
	# 	compiler = NwjsCompiler()
	# 	self.assertIsInstance(compiler,NwjsCompiler,"Es instancia")

	# def test_it_should_return_true_if_nw_its_done_not_override(self):
	# 	compiler = NwjsCompiler()
	# 	self.assertTrue(compiler.generate_nw(sys_project_path,sys_tmp_build_path,False))
	

	# def test_it_should_return_false_if_nw_is_do_it_not_override(self):
	# 	compiler = NwjsCompiler()
	# 	self.assertFalse(compiler.generate_nw(sys_project_path,sys_tmp_build_path,False))
	# 	print("  #Errors: ",compiler.log)

	####################### This test return true if have nw in tmp dir ####################
	# def test_it_should_return_true_if_nw_its_done_it_override(self):
	# 	compiler = NwjsCompiler()
	# 	self.assertTrue(compiler.generate_nw(sys_project_path,sys_tmp_build_path,True))
		

	# def test_it_should_return_true_if_nw_its_done_it_override_and_generate_logs(self):
	# 	compiler = NwjsCompiler()
	# 	self.assertTrue(len(compiler.log)>0)

	# def test_it_should_return_true_if_nw_its_done_it_override_and_do_not_make_errors(self):
	# 	compiler = NwjsCompiler()
	# 	self.assertTrue(len(compiler.errors)==0)

	def test_run(self):
		compiler = NwjsCompiler()
		compiler.run_build_path = sys_path_to_build
		compiler.generate_nw(sys_project_path,sys_tmp_build_path,True)
		#compiler.make_zip(sys_tmp_build_path,sys_project_path,"myZip.zip")
		self.assertTrue(compiler.prebuild())
		compiler.run()
	

if __name__ == '__main__':
    unittest.main()