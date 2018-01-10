#!/usr/bin/python

## read file
xmen_file = open('../files/xmen.txt')

## with new line
#for line in xmen_file:
#    print (line)

## No new lines
print (xmen_file.read())

xmen_file.close()
