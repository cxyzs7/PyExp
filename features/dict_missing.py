'''
Created on Jan 5, 2014

@author: ylou
'''

from collections import defaultdict

class ListDict(dict):
    # if key is missing from dict, it would return whatever __missing__ returns
    def __missing__(self, key):
        self[key] = rv = []
        return rv
    
m = ListDict()

m['test'].append(1)
m['test'].append(2)

print m

m2 = defaultdict(list)
m2['test'].append(1)
m2['test'].append(2)

print m2

