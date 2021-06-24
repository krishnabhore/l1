#! /usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess
import time

# FieldStrorage is  a function to take input
f = cgi.FieldStorage()
cmd = f.getvalue("x")

# sudo power bcoz we are runnig docker commands
output = subprocess.getoutput("sudo " + cmd)
print(output)
