import re

string = '12'
patt = '0?1[0-2]'

m = re.findall(patt, string)
print(m)