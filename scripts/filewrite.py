#!/usr/bin/python

import os
## write a file
#xmen_file = open('../files/xmen.txt','w')

## read and write
xmen_file = open('../files/xmen.txt', 'r+w')

xmen_file.seek(-1, os.SEEK_END)
## same
#xmen_file.seek(-1, 2)

xmen_file.write("\nBeast\n")
xmen_file.write("Phoenix\n")

## wirte anther method
xmen_file.writelines(['Morph\n','Rogue\n'] )
xmen_file.close()


## no need to close , 'a' is append mode

with open('../files/xmen.txt','a') as xmen_file:
    xmen_file.write("Professor Xavier\n")
