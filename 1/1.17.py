import re
from collections import Counter

list = []
patt = '[A-Za-z]{3}\s'
with open('redata.txt','r') as f:
    while True:
        string = f.readline()
        if string is '':
            break
        else:
            m = re.match(patt, string)
            list.append(m.group())
print(Counter(list))


