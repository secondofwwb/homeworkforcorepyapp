import re

string = '878i'

patt = '\d+i$'

m = re.findall(patt, string)

print(m)