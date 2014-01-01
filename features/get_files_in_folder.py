'''
Created on Jan 1, 2014

@author: ylou
'''

import os
import glob
import itertools

def multiple_file_types(folder, *patterns):
    return itertools.chain.from_iterable(glob.glob1(folder, pattern) for pattern in patterns)

def get_files_in_folder(folder, *patterns):
    for filename in multiple_file_types(folder, *patterns):
        yield os.path.join(folder, filename)

if __name__ == '__main__':
    path = r'C:\Users\ylou\Documents'
    for f in get_files_in_folder(path, '*.pdf', '*.txt'):
        print f


