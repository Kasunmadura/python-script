#!/usr/bin/python

import glob
import os
import shutil
import json
import re
#import math


try:
    os.mkdir("../files/receipts/processed")
except OSError:
    print("'processed' directory alread exists")


# Get a list of receipts
#recepits = glob.glob('../files/receipts/new/receipts-[0-9]*.json')
## only Iterate even files

even_receipts = [f for f in glob.iglob('../files/receipts/new/receipts-[0-9]*.json')
            if re.match('../files/receipts/new/receipts-[0-9]*[02468].json', f) ]

# Iterate over the receipts
subtotal = 0.0

for path in even_receipts:
    # read content adn tally a subtotal
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])

    #    subtotal += math.floor(float(content['value']))
    #    subtotal += math.ceil(float(content['value']))

    # mv the file to the processed firectory
    ## easy to use method  :)
    destination = path.replace('new', 'processed')

    shutil.move(path, destination)
    # print that we processed the files
    print ("move '%s' to '%s'" % (path , destination))

# Print the subtotal of all processed receipts
print("Receipts subtotal: $%s" % round(subtotal, 2))
