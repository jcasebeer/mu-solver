#!/usr/bin/env python3

collection = {'mi':'_'}

def rule1(s):
    if s[-1] == 'i':
        return s + 'u'
    return s

def rule2(s):
    return s + s[1:]

def rule3(s):
    return s.replace('iii', 'u')

def rule4(s):
    return s.replace('uu', '')

rules = [rule1, rule2, rule3, rule4]

print("Looking for mu...")
while 'mu' not in collection:
    new = {}
    for key in collection.keys():
        for r in rules:
            if r(key) != key:
                    new[r(key)] = key
    for key in new:
        collection[key] = new[key]
    print("Collection Size: "+str(len(collection.keys())))

print("mu has been found!")            
p = 'mu'
while(p != '_'):
    print(p + " from "+collection[p])
    p = collection[p]
