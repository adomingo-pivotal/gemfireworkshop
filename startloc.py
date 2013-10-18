#!/usr/bin/python2.6

import shlex, subprocess
command_line ="gfsh start locator --name=locator --dir=locator --bind-address=192.168.2.120 --port=55221 --properties-file=./config/gemfire.properties"
args =shlex.split(command_line)
argarray= (args)
for i in xrange(0,len(argarray)):
     if '--port=' in argarray[i]:
       print "Locator is starting on port" , argarray[i].lstrip('--port=')
       break
ret1 =  subprocess.call(args)
#if ret1 != 0:
#   print "Oops! it didn't work.  The return code is: ", ret1
#else:
#   print "Woohoo! it worked! and the return code is: ", ret1

