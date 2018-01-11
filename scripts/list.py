#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser(description="Search for words including partial word")
parser.add_argument('snippet', help='partial (or completed) string to search for in the word file')

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('/usr/share/dict/words').readlines()
# list comperhenstion

print ([word.strip() for word in words if snippet in word.lower()])

#matches = []
#for word in words:
#    if snippet in word.lower():
#
#print(matches)


#numbers = [1,2,3,5]
#[ x * x for x in numbers ]
