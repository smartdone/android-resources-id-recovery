# Android 资源id数值恢复成R.xx.xx

## 1.使用的第三方工具

- apktool
- jd-core
- enjarify

## 2.使用环境

需要python2.x和python3.x同时存在，将python3的可执行文件重命名为python3

如果python3叫其他的名字请将/src/tools/dextojar.py中

> cmd = "python3 -O -m src.tools.enjarify.enjarify.main " 中的python3修改为你的python3可执行文件名称(需要添加到环境变量中)

## 3.使用方法

> python resrecovery.py xxx.apk 输出目录

## 4.输出目录结构

> outpath/  

> |--java/    (jd-core将jar转换成java的原始文件)  

> |--recovered-java/	(将id数值恢复成R.xxx.xxx形式之后的java文件)  

> |--work/				(apktool反编译输出的文件夹)  

> |--out.jar			(使用enjarify将dex(apk)转换成的jar文件)
