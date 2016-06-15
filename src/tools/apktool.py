#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
import os
import subprocess


# s = "java -jar "
# s = s + os.getcwd() + "/src/tools/apktool_2.0.2.jar"
# for i in range(1, len(sys.argv)):
# 	s = s + " "
# 	s = s + sys.argv[i]
# print "Executing command '%s'" %s
# p = subprocess.Popen(s, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# result = p.stdout.read().decode('utf8')
# print result

# 反编译
def decompile(filePath, destpath):
	cmd = "java -jar "
	cmd += os.getcwd() + "/src/tools/apktool_2.0.2.jar"
	cmd += " d " 
	cmd += filePath
	cmd += " -o "
	cmd += destpath
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	result = p.stdout.read().decode('utf8')
	print result
