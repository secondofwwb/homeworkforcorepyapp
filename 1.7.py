import re

string = '44415124'

patt = '[0-9]+'

m = re.findall(patt, string)

print(m)