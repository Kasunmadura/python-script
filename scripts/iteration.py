#!/bin/Python

#Please note that these exercises can be completed using the Linux Academy CentOS 7 Cloud Server images available with your subscription along with the version of Python already installed.
#Building on top of the conditional exercise, write a script that will loop through a list of users, where each item is a user dictionary from the previous exercise, printing out each user s status on a separate line. Additionally, print the line number at the beginning of each line, starting with line 1. Be sure to include a variety of user configurations in the users list.
#User Keys:
#'admin' - a boolean representing whether the user is an admin user.
#'active' - a boolean representing whether the user is currently active.
#'name' - a string that is the user s name.
#Depending on the values of the user, print one of the following to the screen when you run the script:
#print (ADMIN) followed by the user s name if the user is an admin.
#print ACTIVE - followed by the user s name if the user is active.
#print ACTIVE - (ADMIN) followed by the user s name if the user is an admin and active.
#print the user s name if neither active nor an admin.

users = [
{'admin': True,'active':False,'name':"Kasun"},
{'admin': True,'active':True,'name':"Saman"},
{'admin': False,'active':False,'name':"Nimal"}
]

line = 1

for user in users:
    if user['admin']  and user['active']:
        print("%s ACTIVE-(ADMIN) %s" % (line,user['name']) )
    elif user['admin']:
        print("%s (ADMIN) %s" % (line,user['name']) )
    elif user['active']:
        print("%s ACTIVE %s" % (line,user['name']) )
    else:
        print ("%s %s" % (line,user['name']))
    line +=1
