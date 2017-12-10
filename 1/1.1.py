import re
string = 'bat.bit.but.hat.hit.hut'
patt = '[bh][aeiou]t'

m = re.findall(patt, string)
print(m)