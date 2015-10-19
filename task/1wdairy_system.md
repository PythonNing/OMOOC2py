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
* 突然了解到原来前一个问题是因为没有进入python的交互模式，在Cygwin可以使用```-i```进入交互模式（[ref](http://www.pythondoc.com/pythontutorial27/interpreter.html)）。但是运行了script就会直接进入交互模式了。仍然不是解决办法。
* 尝试输入中文成功。
* to do: 加日期，持续交互
