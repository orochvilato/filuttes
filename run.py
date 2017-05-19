#!/usr/bin/env python3
# -*- coding: utf-8 -*

from app import app


f = open('/home/olivier/devs/filuttes/app/gms.txt')
import re
lutte = {}
def addconf(dct,path,value):
    for p in path[:-1]:
        if not p in dct.keys():
            dct[p] = {}
        dct = dct[p]
    if path[-1] in dct.keys():
        if isinstance(dct[path[-1]],basestring):
            dct[path[-1]] = [dct[path[-1]]]
        dct[path[-1]].append(value)
    else:
        dct[path[-1]] = value

for line in f:
    m = re.match(r'^\[(.*)]$',line)
    if m:
        current_path = m.groups()[0].split('.')
    else:
        m2 = re.match(r'^([A-Za-z0-9_\.]+): ?(.*)$',line)
        if m2:
            addconf(lutte,current_path+[m2.groups()[0]],m2.groups()[1])
        else:
            addconf(lutte,current_path+['contenu'],line)

print lutte

if __name__ == "__main__":
    app.run()
