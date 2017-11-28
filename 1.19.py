import re

string = 'Tue Nov  1 07:04:16 1977::egatqn@egwlwigpxsda.org::247187056-6-12'

patt = '.+\s[0-9]{4}'

m = re.search(patt, string)

print(m.group())