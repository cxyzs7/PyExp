'''
Created on Jan 1, 2014

@author: ylou
'''
import logging, inspect

def setup_logging():
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(filename)s:%(lineno)-4d: %(message)s',
                    datefmt='%m-%d %H:%M')

def get_info():
    # frame, filename, line_number, function_name, lines, index
    return inspect.getouterframes(inspect.currentframe())[1]

if __name__ == '__main__':
    setup_logging()
    
    logging.debug('test1')
    logging.warning('WARNING!')
    
    print get_info()
