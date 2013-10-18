#!/usr/bin/python2.6

import shlex,subprocess,sys,os,signal,time
command_line ="gfsh start server --name=server2 --dir=server2 --cache-xml-file=./config/cache.xml --properties-file=./config/gemfire.properties --classpath=../ecommerce.jar --server-port=40405"
args =shlex.split(command_line)
argarray= (args)
for i in xrange(0,len(argarray)):
     if '-port=' in argarray[i]:
       print "Server is starting on port" , argarray[i].lstrip('--port=')
       break
ret1 =  subprocess.Popen(args)
print "Started"
ret1.communicate()
ret1.wait()
#print ret1.returncode
#if ret1.returncode != 0:
#   print "Error starting server!",ret1.returncode
#   time.sleep(2)
#   os.kill(ret1.pid, signal.SIGTERM)
#else:
#   print "Server started successfully"
