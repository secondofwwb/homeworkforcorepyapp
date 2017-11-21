# -*- coding: utf-8 -*-
# 数据生成器
from random import randrange,choice
from string import ascii_lowercase as lc
import math
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')
with open('redata.txt', 'w') as f:
    for i in range(randrange(5,11)):
        dtint = randrange(maxsize)   #取一个随机数
        dtstr = ctime(math.pow(2,32))      #随机数转换为时间
        llen = randrange(4,8)     #限定生成数据长度
        email_name = ''.join(choice(lc) for j in range(llen))
        dlen = randrange(llen, 13)
        dom = ''.join(choice(lc) for j in range(dlen))
        f.write('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr,email_name,dom,choice(tlds),dtint,llen,dlen))
