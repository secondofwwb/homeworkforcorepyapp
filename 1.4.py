import re

string = '__init__'

patt = '_+\w+_*'

m = re.findall(patt, string)

print(m)