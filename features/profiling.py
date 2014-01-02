'''
Created on Jan 1, 2014

@author: ylou
'''
import time
import cProfile
from line_profiler import LineProfiler

class timewith():
    def __init__(self, name=''):
        self.name = name
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start

    def checkpoint(self, name=''):
        print '{0} {1} took {2} seconds'.format(self.name, name, self.elapsed).strip()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.checkpoint('finished')
        pass

def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func

def do_line_profile(follow=[]):
        def inner(func):
            def profiled_func(*args, **kwargs):
                try:
                    profiler = LineProfiler()
                    profiler.add_function(func)
                    for f in follow:
                        profiler.add_function(f)
                    profiler.enable_by_count()
                    return func(*args, **kwargs)
                finally:
                    profiler.print_stats()
            return profiled_func
        return inner

def get_number():
    for x in xrange(5000000):
        yield x

def expensive_function():
    for x in get_number():
        i = x ^ x ^ x
    return 'some result!'

@do_cprofile
def expensive_function_1():
    for x in get_number():
        i = x ^ x ^ x
    return 'some result!'

@do_line_profile(follow=[get_number])
def expensive_function_2():
    for x in get_number():
        i = x ^ x ^ x
    return 'some result!'

if __name__ == '__main__':
    # use timewith class
    timer = timewith('fancy thing')
    expensive_function()
    timer.checkpoint('done with something')
    expensive_function()
    expensive_function()
    timer.checkpoint('done with something else')
    
    # use cProfile
    result = expensive_function_1()

    result = expensive_function_2()
    
