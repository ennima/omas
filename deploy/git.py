import subprocess, os

proy_dir = "C:\\Users\\enrique.nieto\\Documents\\develops\\omas\\"
os.chdir(proy_dir)
print(os.getcwd())
batcmd=["git","add","--all"]
result = subprocess.check_output(batcmd, shell=True)
print(result)