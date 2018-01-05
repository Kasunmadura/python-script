#/usr/bin/python

import time

start_time = time.localtime()

print ("Time start at %s" % time.strftime("%X", start_time) )

# wait for user input

raw_input("Please press Enter to continue...")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print ("Timer stopped at %s" % time.strftime("%X", stop_time))
print ("Total time %s secondes" % difference)
