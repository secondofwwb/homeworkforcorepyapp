import re

patt = '\d+\s\d+'

with open('redata.txt', 'r') as f:
    while True:
        string = f.readline()
        if string is '':
            break
        else:
            m = re.search(patt, string)
            if m is None:
                print('wrong')
            else:
                print('ok')