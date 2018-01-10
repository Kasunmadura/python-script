#!/usr/bin/python

#import sys

#print ("Frist Argument is  %s" % sys.argv[1])


import argparse

parser = argparse.ArgumentParser()
## add_argument is method
parser.add_argument('filename', help= 'the file to read')
args = parser.parse_args()
