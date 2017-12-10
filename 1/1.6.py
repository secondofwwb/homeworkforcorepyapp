import re

string = 'www.google.com'

patt = 'w{3}.\w+.[cne][onde][umt]?'

m = re.findall(patt, string)

print(m)