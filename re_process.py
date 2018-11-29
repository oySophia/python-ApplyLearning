#coding="utf-8"
#/usr/bin/python

import re

if __name__ == "__main__":
    f = re.sub("\d+", "112", 'dsdfgda3434fgfg')
    print (f)

    print(re.split(r'[\s\,]+', 'a,b, c  d'))
    print(re.search(r'[a-z]+', 'liuyaN1234ab9').group())
    print(re.search(r'[a-z]+', 'liuyaN1234ab9', re.I).group())