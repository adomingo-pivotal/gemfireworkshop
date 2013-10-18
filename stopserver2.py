#!/usr/bin/python2.6

import shlex, subprocess, sys,os,signal,time
command_line1="gfsh stop server --dir=/root/labs/server2"
args =shlex.split(command_line1)
argarray = (args)
for i in xrange (0,len(argarray)):
    print " arg # ",i,argarray[i]

ret1 =  subprocess.Popen(args)
ret1.communicate()
ret1.wait
#if ret1.returncode != 0:
#   print "Server shutdown error!"
#   time.sleep(2)
#   os.kill(ret1.pid, signal.SIGTERM)
#else:
#   print "Server shutdown complete"
