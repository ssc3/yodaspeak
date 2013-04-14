#! /usr/bin/python

import cgi
from os import environ
import cgitb
cgitb.enable()

print "Content-type: text/plain"
print
f = cgi.FieldStorage()

input_string = f.getfirst('w')

print "You input the string " + str(input_string) 

for my_word in input_string:
    print str(my_word)

