import re

patt1 = '\w+@\w+\.\w+'
patt2 = '\s\w+\s'
patt3 = '[0-9]{4}'
patt4 = '\d+:\d+:\d+'

string = 'Sat Apr  4 16:51:35 2071::xwkbaa@qjivmhiufvr.com::3195363095-6-11'

m = re.search(patt4, string)

print(m.group())