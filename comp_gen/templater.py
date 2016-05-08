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

with open(template_name, 'r') as f:
	template = f.read()

print (template.replace("{is}", "was"))