import re

patt1 = '\w+@\w+\.\w+'
patt2 = '\s\w+\s'
patt3 = '[0-9]{4}'
patt4 = '\d+:\d+:\d+'
patt5 = '([a-z]+)@(\w+)\.(\w+)'
patt6 = '([a-z]+)@(\w+\.\w+)'
patt7 = '((?<=\w{3}\s)\w{3})\s+(\d+).+\s(\d{4})'

string = 'Sat Apr  4 16:51:35 2071::xwkbaa@qjivmhiufvr.com::3195363095-6-11'

m = re.search(patt4, string)
m2 = re.search(patt7, string)

rep = 'wuwenbosecond@163.com'

m3 = re.sub(patt1, rep, string)

print(m2.groups())
