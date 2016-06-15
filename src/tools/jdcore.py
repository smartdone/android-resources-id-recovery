#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
import os
import subprocess
import platform

# sysplatform = platform.system()
# cmd = "java -jar "
# cmd += os.getcwd() + "/src/tools/jd-core-java-1.2.jar" 

# for i in range(1, len(sys.argv)):
# 	cmd = cmd + " "
# 	cmd = cmd + sys.argv[i]

# print "Executing command '%s'" %cmd
# p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# result = p.stdout.read().decode('utf8')
# print result

def decompile(srcpath, destpath):
	cmd = "java -jar "
	cmd += os.getcwd() + "/src/tools/jd-core-java-1.2.jar "
	cmd += srcpath
	cmd += " "
	cmd += destpath
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	result = p.stdout.read().decode('utf8')
	print "转换完成"
