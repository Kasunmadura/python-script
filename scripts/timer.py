#!/usr/bin/python

#import time
from time import localtime, strftime , mktime

#start_time = time.localtime()
start_time = localtime()

print ("Time start at %s" % strftime("%X", start_time) )
#print ("Time start at %s" % time.strftime("%X", start_time) )

# wait for user input

raw_input("Please press Enter to continue...")

stop_time = localtime()
#stop_time = time.localtime()

#difference = time.mktime(stop_time) - time.mktime(start_time)
difference = mktime(stop_time) - mktime(start_time)

print ("Timer stopped at %s" % strftime("%X", stop_time))
print ("Total time %s secondes" % difference)
