#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description="Read a file in reverse")

## add_argument is method
parser.add_argument('filename', help= 'the file to read')
parser.add_argument('--limit','-l', type=int, help= 'the number of lines to read')
parser.add_argument('--version','-v', action='version', version='%(prog)s 1.0')

#"%(prog)s 2.0" % {'prog':'reverse-file'}

## this object which have attributes
args = parser.parse_args()

#print(args)

#attributes
#print(args.filename)

try:
    f = open(args.filename)
except IOError as err :
    print (" Error: file not found")
## multiple except
else:
    with f:
         limit = args.limit
         lines = f.readlines()
         lines.reverse()

         if limit:
             lines = lines[:limit]

         for line in lines:
             print(line.strip()[::-1])
finally:
    print("\n **************  We are finished  ***************\n")
