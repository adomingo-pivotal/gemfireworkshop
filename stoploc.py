#!/usr/bin/python2.6

import shlex, subprocess, sys

command_line1 = "gfsh stop locator --dir /root/labs/locator"
args =shlex.split(command_line1)
argarray = (args)
for i in xrange (0,len(argarray)):
    print " arg # ",i,argarray[i]

ret1 =  subprocess.call(args)
if ret1 != 0:
   print "Oops! Locator is down!.  The return code is: ", ret1
else:
   print "Woohoo! it worked! and the return code is: ", ret1
