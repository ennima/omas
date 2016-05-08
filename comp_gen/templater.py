############################################################################
#
# Author: Enrique Nieto
# Start: 08-05-2016
# Description: First Version of Templater that replace strings in file.
#
############################################################################
import os

str = "this {is} string example....wow!!! this {is} really string";
'''print (str.replace("{is}", "was"))
print (str.replace("{is}", "was", 3))'''

template_name ="templater.txt"
template = ""
vars_change = [
				{"var":"is","val":"was"},
				{"var":"name","val":"Enrique"},
				{"var":"verv","val":"Great"},
			  ] 

with open(template_name, 'r') as f:
	template = f.read()

#print (template.replace("{is}", "was"))
newTemplate = template
for change_var in vars_change:
	newTemplate = newTemplate.replace("{"+change_var["var"]+"}",change_var["val"])
	print(change_var["var"])

print(newTemplate)