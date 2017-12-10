import re
sometype = type(0)

patt = '\s\'\w+\''

m = re.findall(patt, str(sometype))

print(m)