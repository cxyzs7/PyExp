'''
Created on Jan 1, 2014

@author: ylou
'''
import atexit
import time
import math
 
def microtime(get_as_float = False) :
    if get_as_float:
        return time.time()
    else:
        return '%f %d' % math.modf(time.time())
start_time = microtime(False)
 
def shutdown():
    global start_time
    print "Execution took: {0} seconds".format(start_time)
 
atexit.register(shutdown)

print 'Start'

array = []

print array[0]

