#!/usr/bin/python
# -*- coding: utf8 -*-

import os

def getid(str):
	ret = "R."
	items = str.split(" ")
	length = len(items)
	if length == 5:
		t1 = items[1].split("=")[1]
		t1 = t1.replace('"', '')
		t2 = items[2].split("=")[1]
		t2 = t2.replace('"', '')
		ret += t1 + "." + t2

		t3 = items[3].split("=")[1].replace('"', '')
		t3 = "%d" %int(t3,16)
		# print ret
		# print t3

		return [t3, ret]
	else:
		return ""

def getidmap(path):
	rootdir = path
	l = list(path)
	length = len(l)
	rootdir = path
	if l[length - 1] == '/' :
		rootdir += "work/res/values/public.xml"
	else:
		rootdir += "/work/res/values/public.xml"
	
	print "解析%s" %rootdir


	if os.path.exists(rootdir):
		fp = open(rootdir, "r")
		line = fp.readline()
		ids = {}
		while line:
			# 去掉首尾的空白字符
			s = line.strip()
			item = getid(s)
			if item != "":
				ids[item[0]] = item[1]
			# ids[item[0]] = item[1]
			line = fp.readline()
		fp.close()
		return ids
	else:
		print "public.xml文件不存在"
		return ""