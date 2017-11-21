import re

string = 'sicuan chengdu wuhou cunxilu 111hao'

patt = '[\w+\s]+[0-9]+hao$'

m = re.match(patt, string)

print(m.group())