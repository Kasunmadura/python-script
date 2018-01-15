#!/usr/bin/python

import sys
################################################# test  1 ################################################
#Functions are a great way to organize your code for reuse and clarity. Write a script that does the following:

#Prompts the user for a message to echo
#Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
#Defines a function that takes a message and count, then prints the message that many times.
#To end the script, call the function with the user-defined values to print to the screen.


################################################# test  1 ################################################


message      = raw_input ("Please type any message = ")

try:
    message_freqency= int(raw_input ("please type the fequency for message = ")or 1)
except NameError as err:
    print ("please Enter valiad number for repeat the message")
    sys.exit(0)
except ValueError as err:
    print ("please Enter valiad number for repeat the message")
    sys.exit()

def count(message,message_freqency):
    for x in range(message_freqency):
        print(message)

count (message, message_freqency)
