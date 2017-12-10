import re

string = '4564.456153'

patt = '\d+\.\d+'

m = re.findall(patt, string)

print(m)