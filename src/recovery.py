#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import re
import xmlparser


# 一次完成多个字符串的替换
def multiple_replace(text,adict):  
    rx = re.compile('|'.join(map(re.escape,adict)))  
    def one_xlat(match):  
        return adict[match.group(0)]  
    return rx.sub(one_xlat,text) #每遇到一次匹配就会调用回调函数

def parseinttoid(path):
	ids = xmlparser.getidmap(path)
	print ids

	rootdir = path
	l = list(path)
	length = len(l)
	rootdir = path
	if l[length - 1] == '/' :
		rootdir += "java/"
	else:
		rootdir += "/java/" 

	for parent,dirnames,filenames in os.walk(rootdir):
		for filename in filenames:
			inpath = "%s/%s" %(parent, filename)
			outpath = inpath.replace('/java/', '/recovered-java/')
			print "写入文件%s" %outpath
			in_stream = open(inpath, "r")
			if not os.path.exists(os.path.dirname(outpath)):
				os.makedirs(os.path.dirname(outpath))
			# print os.path.dirname(outpath)
			out_stream = open(outpath, "w")

			line = in_stream.readline()
			while line:
				# print line
				line = in_stream.readline()
				line = multiple_replace(line, ids)
				out_stream.write(line)

			in_stream.close()
			out_stream.close()

			

