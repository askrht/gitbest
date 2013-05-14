#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on May 14, 2013

@author: RHT
'''
import re, fileinput, os, optparse #@UnresolvedImport
import ConfigParser, sys
import engine

# globals
options, args, usage = None, None, None
config = None

def setOptions():
    global options, args, usage, keys
    usage = '''usage: python %prog [options]
    
    output folder contains the results
    
    '''
    option_parser = optparse.OptionParser(usage = usage)
    option_parser.add_option("-o", "--out_dir", default = "output", action="store", type="string", dest="out_dir", 
                      help="store results in the specified output directory [default: %default]")
    option_parser.add_option("-k", "--keys_file", default = "keys.ini", action="store", type="string", dest="keys_file", 
                      help="read API keys from the specified file [default: %default]")
    (options, args) = option_parser.parse_args()
    keys = ConfigParser.ConfigParser()
    keys.read(options.keys_file)
    keys.sections()

class Config(object):
    def __init__(self, config_dir='config'): 
        pass

def start():
    setOptions()
    if not os.path.exists(options.out_dir):
        os.makedirs(options.out_dir)
    os.chdir(options.out_dir)
    engine.fetchsamples(keys)

if __name__ == "__main__":
    sys.exit(start())

