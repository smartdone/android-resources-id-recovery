#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import os
import src.core as core

# 显示帮助
def help():
	print "用法:"
	print "\tpython %s [<apk file>] [<destination path>]" %sys.argv[0]

def main():
	srcpath = ""
	dstpath = ""
	if len(sys.argv) == 3:
		srcpath = sys.argv[1]
		dstpath = sys.argv[2]
		# 判断文件是否存在
		if os.path.exists(srcpath):
			obj = core.resanalysis(srcpath, dstpath)
			obj.doall()
		else:
			print "警告：文件 %s 不存在!" %srcpath
	else:
		help()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print "程序已终止"