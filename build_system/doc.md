pyCompilerWin.py

	For use this script, need install python and py2exe

	for python 3.4 use py2exe 0.9.2.2

	for install py2exe 

		pip install py2exe


	Prepare scripts for compile:

		if script have dependences like a .json file that call inside...

			1.- make a folder named depend
			2.- make file named <scriptName>.json
			3.- make this structure:
					{
						"res_files":[
							{"file":"config.json"},
							{"file":"config_1.json"},
							...
							{"file":"config_N.json"}
						]
					}