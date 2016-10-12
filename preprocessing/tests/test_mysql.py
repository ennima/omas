import sys
import unittest
sys.path.append('../')
sys.path.append('../db')

from MysqlProcessing import *
from pprint import pprint

class MysqlProcessingTest(unittest.TestCase):
	
	# def test_it_should_be_able_to_construct(self):
	# 	mysql = MysqlProcessing()
	# 	self.assertIsInstance(mysql,MysqlProcessing,"Es instancia")

	# def test_it_should_be_able_to_load(self):
	# 	mysql = MysqlProcessing()
	# 	self.assertTrue(mysql.load("../db/db.json"))
	# 	#pprint(mysql.data)

	def test_making_a_table(self):
		#Global path is for find compiler files.
		mysql = MysqlProcessing("../db/")
		mysql.publish_path = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\build_test\\db\\"
		mysql.prettyfy = False
		mysql.publish_single_file = True
		mysql.publsh_to_file = True
		#mysql.process_create = False

		#This is a specific path not global
		mysql.load("../db/db.json")

		mysql.process()


		
		print(mysql.tables)
   
		
if __name__ == '__main__':
    unittest.main()