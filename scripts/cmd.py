#!/usr/bin/python

import subprocess

#code = subprocess.call(['ls', '-l'])
try:
    output = subprocess.check_output(
              ['ls', 'fake.txt'],
              stderr= subprocess.STDOUT
             )
except OSError as err:
    print(" Caught OS error")
    output = err
except subprocess.CalledProcessError as err:
    print ("Caught CalledProcessError")
    output = err

#code = subprocess.check_output(['ls', '-z'])

#if code == 0 :
#    print (" command finished successfuly")
#else:
#    print("failed with code: %i" % code)

print (output)
