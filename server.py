#!/bin/python

import socket
import re
import cgi, cgitb


# Standard socket stuff:
host = '' # do we need socket.gethostname() ?
port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1) # don't queue up any requests

# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(1024) # get the request, 1kB max
    print req
    # Look in the first line of the request for a move command
    # A move command should be e.g. 'http://server/move?a=90'
    # match = re.match('GET /move\?a=(\d+)\sHTTP/1', req)
    # if match:
    csock.sendall("""HTTP/1.0 200 OK
        content-type: text/html

 <html>
 <head>
 <title> This is the title </title>
 </head>
 <body>
 <br>
 <form action="/home/ssc3/projects/web-server/cgi/change_lang.py" method="post">
First Name: <input type="text" name="first_name"><br />
Last Name: <input type="text" name="last_name" />

<input type="submit" value="Submit" />
</form>
</body>
</html>
""")
    #else:
        # If there was no recognised command then return a 404 (page not found)
     #   print "Returning 404"
     #   csock.sendall("HTTP/1.0 404 Not Found\r\n")
    csock.close()
