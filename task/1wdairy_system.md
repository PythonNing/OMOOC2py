#交互 101
本周整体任务概述:

* 完成一个极简交互式日记系统,需求如下:
    * 一次接收输入一行日记
    * 保存为本地文件
    * 再次运行系统时,能打印出过往的所有日记
* 时限: 0wd4~1wd3
* 发布: 发布到各自仓库的 _src/om2py0w/0wex1/ 目录中
* 指标:
    * 包含软件使用说明书: README.md
    * 能令其它学员根据说明书,运行系统,完成所有功能



---

## 20151018

从最简单可以实现的部分开始做。

<pre><code>print 'Here is the previous dairy.'
f = open('new dairy.txt','a+')
print f.read()

f = open('new dairy.txt','a')
line = raw_input(' new dairy >')
f.write('%s\n' % line)
f.close()
</code></pre>

* 环境配置：win/python 2.7.10/powershell
* 以上几行在powershell里面测试的话,可以达到最基本要求，输入一行日记，保存为本地文件，再次运行打印过往日记。
* 但用powershell本就无法中文输入，所以没法测试中文是否可行

## 20151019
* 安装了[Cygwin](https://cygwin.com/)，打算在Cygwin里测试中文输入
* 发现另一个问题，在Cygwin下是不会一行一行读取代码，然后在遇到```raw_input```的时候提示输入。
* 突然了解到原来前一个问题是因为没有进入python的交互模式，在Cygwin可以使用```-i```进入交互模式（[ref](http://www.pythondoc.com/pythontutorial27/interpreter.html)）。但是运行了script就会直接进入交互模式了。仍然有问题
* 尝试输入中文成功。
* to do: 加日期，持续交互
 
## 20151020
* 先放下交互模式问题，重新设计code为可以持续交互。
* 设想如下：
    * 打印出菜单，询问user是想要写新日记还是读取旧日记或者退出
    * 选择1，写新日记write，同时加上localtime
    * 选择2，读取日记read，打印出之前的日记
    * 选择3，退出程序
    * 想要持续交互就是在选择1和选择2最后回到菜单模式，除非user选择退出
    * 如果user输入的选择不是1/2/3，则报错误信息再重新回到菜单
    * 之前想要用while实现持续交互，但现在发现其实不用，直接调用回主程序即可（想到最早学过一点C语言，记得C是不能在函数里面再调用自己的，python真自由）

<pre><code>import os
from time import localtime, strftime

def dairy():
	print """
	Choose from the menu below:
	1. Write new dairy
	2. Read previous dairy
	3. Quit """
	
	choice = raw_input('Input 1/2/3 >') # ask for choosing from menu
	
	if choice == '1':
		write() # write new dairy
	elif choice == '2':
		read() # read previous dairy
	elif choice == '3':
		os._exit(0) # exit the script
	else:
		print 'Wrong number. Choose again!'
		dairy() # return to the menu

def write():
	f = open('new dairy.txt','a') 
	line = raw_input('Input here >')
	edit_time = strftime("%a, %Y %b %d %H:%M:%S", localtime())
	f.write('%s     %s\n' % (edit_time, line))
	f.close()
	dairy() # return to the menu

def read():
	f = open('new dairy.txt','a+')
	print 'Below is the previous dairy.'
	print f.read()
	dairy() # return to the menu
	
dairy()
</code></pre>

测试结果
* Powershell：正常，虽然还是显示/输入不了中文，但持续交互目的达成
* Cygwin：
    * ```python -i dairy.py```用这个命令行使python进入到了交互模式，可以正常交互使用，而在选择3，用到了```os._exit()```除了可以退出程序也可以同时退出交互模式，不小心又把昨天的遗留问题解决了。但在想这是个可以general来使用的方法还是只是碰巧这次可以这么使用。
    * 中文显示输入没有问题
    * 但奇怪的是时间显示有问题，用的是```time```module里的```localtime()```但结果出来的时间和实际不一样，遗留问题