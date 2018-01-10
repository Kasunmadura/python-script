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

with open(args.filename) as f:
     lines = f.readlines()
     lines.reverse()

     if args.limit:
         lines = lines[:args.limit]

     for line in lines:
         print(line.strip()[::-1])
