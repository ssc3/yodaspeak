#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
input_text = form.getvalue('input_text')

#print "Content-type:text/html\r\n\r\n"
#print "<html>"
#print "<head>"
#print "<title>Yoda speak</title>"
#print "</head>"
#print "<body>"
#print "<h2>Hello </h2>" + str(input_text)
#print "</body>"
#print "</html>"

cl_js_file = open('/var/www/scripts/changed_lang.js', 'w')
cl_js_file.write ('Hi there')
cl_js_file.close()
