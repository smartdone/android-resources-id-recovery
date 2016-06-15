#!/usr/bin/python
# -*- coding: utf8 -*-
import sys
import os
import subprocess

# 将dex转换成jar
def dextojar(filepath, outpath):
	cmd = "python3 -O -m src.tools.enjarify.enjarify.main "
	cmd += filepath
	cmd += " -o "
	cmd += outpath
	print cmd
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	result = p.stdout.read().decode('utf8')
	print result
	