#!/usr/bin/python

import cgi
from os import environ
from os import sys

import cgitb
cgitb.enable()

print "Content-type: text/plain"
print
f = cgi.FieldStorage()

input_string = f.getfirst('w')

if not f:
    print "Enter text, you must"
    sys.exit(0)

# print len(input_string.split(' '))

conj_list = ["and", "but", "or", "nor", "for", "yet", "so", "is"]

flag = False

subject_list = []
object_list = []
merged_list = []

for my_word in input_string.split(' '):

    if (flag == True):
        object_list.append(str(my_word))
    else:
        subject_list.append(str(my_word))

    for conj_words in conj_list:
        if (my_word.lower() == conj_words.lower()):
            flag = True


object_list.append(",")
merged_list = object_list + subject_list

array_idx = 0
for yoda_word in merged_list:

    if (array_idx == 0):
        array_idx += 1
        print yoda_word.capitalize(),  # wtf: A trailing comma means space? what shit language is this
    else:
        print yoda_word.lower(),


