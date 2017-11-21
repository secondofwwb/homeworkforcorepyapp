import re

string = 'tom smith tom,smith'

patt = '\w+[,|\s]'

m = re.findall(patt, string)

print(m)