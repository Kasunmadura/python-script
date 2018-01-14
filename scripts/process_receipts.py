#!/usr/bin/python

import glob
import os
import shutil
import json


try:
    os.mkdir("../files/receipts/processed")
except OSError:
    print("'processed' directory alread exists")


# Get a list of receipts
recepits = glob.glob('../files/receipts/new/receipts-[0-9]*.json')

# Iterate over the receipts
subtotal = 0.0

for path in recepits:
    # read content adn tally a subtotal
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # mv the file to the processed firectory
    name = path.split('/')[-1]
    destination = '../files/receipts/processed/%s' % name
    shutil.move(path, destination)
    # print that we processed the files
    print ("move '%s' to '%s'" % (path , destination))

# Print the subtotal of all processed receipts
print("Receipts subtotal: $%.2f" % subtotal)
