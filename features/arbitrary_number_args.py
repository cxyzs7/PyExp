'''
Created on Jan 1, 2014

@author: ylou
'''

def function_optional_args(arg1="", arg2=""):
    print "arg1:{0}".format(arg1)
    print "arg2:{0}".format(arg2)
    
def function_arbitrary_args(*args):
    num_args = len(args)
    print "Number of arguments: {0}".format(num_args)
    for i, arg in enumerate(args):
        print "Argument {0} is {1}".format(i, arg)
        
if __name__ == '__main__':
    function_optional_args()
    function_optional_args("a", "b")
    
    function_arbitrary_args()
    function_arbitrary_args("a", "b", "c")
