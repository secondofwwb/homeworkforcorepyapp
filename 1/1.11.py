import re

string = 'wuwenbosecond@163.com'

patt = '\w+@\w+\.com'

m = re.findall(patt, string)

print(m)