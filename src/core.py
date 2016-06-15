#!/usr/bin/python
# -*- coding: utf8 -*-

import tools.apktool as apktool
import tools.dextojar as enjarify
import tools.jdcore as jdcore
import recovery

class resanalysis(object):
	"""docstring for resanalysis"""

	jarpath = "out.jar"
	javafilepath = "java"
	smalipath = "work"

	def __init__(self, srcpath, dstpath):
		super(resanalysis, self).__init__()
		self.srcpath = srcpath
		self.dstpath = dstpath
		
	def startrecovery(self):
		print "开始将资源id恢复成R.xx.xx形式（请耐心等待）..."
		recovery.parseinttoid(self.dstpath)

	def useapktool(self):
		print "开始反编译..."
		dpath = self.dstpath
		dpath += "/"
		dpath += self.smalipath 
		apktool.decompile(self.srcpath, dpath)

	def useenjarify(self):
		print "开始讲dex文件转换成jar文件（请耐心等待）..."
		dpath = self.dstpath
		dpath += "/"
		dpath += self.jarpath 
		self.jarpath = dpath
		print self.jarpath
		enjarify.dextojar(self.srcpath, dpath)

	def usejdcore(self):
		print "开始将jar文件转换成java文件（请耐心等待）..."
		dpath = self.dstpath
		dpath += "/"
		dpath += self.javafilepath 
		jdcore.decompile(self.jarpath, dpath)


	def doall(self):
		print "自动化转换中..."
		self.useapktool()
		self.useenjarify()
		self.usejdcore()
		self.startrecovery()
