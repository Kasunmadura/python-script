#!/bin/Python

#Please note that these exercises can be completed using the Linux Academy CentOS 7 Cloud Server images available with your subscription along with the version of Python already installed.
#Create a script that has a single variable you can set at the top called user. This user is a dictionary containing the keys:
#'admin' - a boolean representing whether the user is an admin user.
#'active' - a boolean representing whether the user is currently active.
#'name' - a string that is the users name.
#Example:
#user = { 'admin': True, 'active': True, 'name': 'Kevin' }
#Depending on the values of user, print one of the following to the screen when you run the script:
#print (ADMIN) followed by the user s name if the user is an admin.
#print ACTIVE - followed by the user s name if the user is active.
#print ACTIVE - (ADMIN) followed by the user s name if the user is an admin and active.
#print the user s name if neither active nor an admin.
#Change the values of user and re-run the script multiple times to ensure that it works.

user =  {'admin': True,'active':False,'name':"Kasun"}

if user['admin']  and user['active']:
    print("ACTIVE-(ADMIN) %s" % user['name'] )
elif user['admin']:
    print("(ADMIN) %s" % user['name'] )
elif user['active']:
    print("ACTIVE %s" % user['name'])
else:
    print user['name']
