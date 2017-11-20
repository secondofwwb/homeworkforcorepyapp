import re

string = 'tom smith'
patt = '\w+\s\w+'

m = re.match(patt, string)
print(m.group())