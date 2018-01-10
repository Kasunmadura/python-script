#!/bin/python


#Please note that these exercises can be completed using the Linux Academy CentOS 7 Cloud Server images available with your subscription along with the version of Python already installed.
#Write a Python script that sets the following variables:
#first_name - Set to your first name
#last_name - Set to your last name
#age - Set to your age as an integer
#birth_date - Set to your birthdate as a string
#Using the variables, print the following to the screen when you run the script:

#My name is FIRST_NAME LAST_NAME.
#I was born on BIRTH_DATE and I'm AGE years old.

first_name = "Kasun"
last_name  = "Madura"
age        = 30
birth_date = "1987/10/28"

print("My name is %s %s.\nI was born on %s and I'm %s years old. " %  (first_name,last_name,age,birth_date))
