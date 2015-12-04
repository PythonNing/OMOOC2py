# MyDiary QPY

* 嗯最后一项任务~Android应用
* 因为上周出去玩了,所以推迟交作业
* 本来还想出门在外的时候是不是可以用手机写代码呢?然而发现还是不太现实...
* 反而就算最后是在手机上实现app,其实开发过程测试等仍然是需要本机操作更方便也更有效率
* 这次就我个人而言, 花时间最多的不是码代码, 而是搭建开发测试的环境...

## 参考资料
* [如何自在的折腾QPy  by大妈](http://codelab.qpython.org/pythonic/init-my-qpy-env.html)
* [如何使用QPython开发Android应用  by River](http://codelab.qpython.org/qpythoncodelab/1st-qpython-app-for-android.html)
* [官方文档](http://wiki.qpython.org/)
* 另外还有已经交了作业的两位同学的教程
	* [@xpgeng](https://xpgeng.gitbooks.io/omooc2py/content/_src/om2py7w/7wex0/Mydaily-Android.html)
	* [@jeremiahzhang](https://jeremiahzhang.gitbooks.io/omooc2py/content/2nDev/week07_qpy.html) 主要参考环境搭建

## 任务分解
- [x]环境搭建
	- [x]root自己的小米4
	- [x]手机上安装BusyBox和SSHDroid
- [x]Web App开发,主要修改QPython自带WebApp Sample完成,参照@xpgeng同学代码
	- [x]学习下sqlite3
- [x]本地client

## 1. 有关环境搭建
* 其实说环境搭建,其实只是想解决在本机开发的代码需要传到手机的QPython里去,应该怎么传,传到哪里去的问题
* 这一点一开始只看到大妈的教程里有讲用到Busybox和SSHDroid,以及River的视频里讲到用adb安卓开发工具
	* 先跟着大妈的教程,下了BusyBox和SSHDroid,结果忘了自己根本没root权限,试个毛.....
	* 转回先root手机吧
* root手机的时候被第一个教程坑了...
	* 教程说可以把最新的稳定版下下来只是改一下版本编号就变成开发版了
	* 试了....并没有好嘛....
	* 重新在MIUI论坛上搜了一下才有正确姿势,直接刷开发版本才会真正有root权限
	* 顺便也下了Root Checker和Root Explorer来检查是否有root access以及直接从手机上找下是否可以找到QPython的文件夹
* root好了才能正常使用BusyBox和SSHDroid....
	* BusyBox是类似一个小工具箱,把正常UNIX应该有的功能一起装载在手机上
	* SSHDoid是一个通道,打通开发机和手机,可以直接从开发机终端上直接连到手机的Shell上
		* 所以可以在自己的开发机上使用```ssh root@192.168.0.100```登录上手机,这样才能愉快的在开发机上调戏
* 另外还有如何加载python,大妈的教程也有清楚写.
* 以及我因为还没搞清楚fabric怎么玩,所以很蠢的复制粘贴了那三行
* 现在想想其实只是想把自己电脑里写的项目代码传到手机里的话,其实只需要root手机之后,找到对应目录,直接手机数据线连上电脑,复制粘贴最快
	* 但如果是复杂项目,这么做肯定是太麻烦,还是像git push这样可以马上上传的然后运行测试才能最快迭代

## 2. WebApp开发
* 从QPython自带的WebApp Sample着手,已有的框架全都不用变, 只需要修改route的函数即可
* 参照两位同学提交的代码,学习了一下sqlite3
	* 参考[官方文档](https://docs.python.org/2/library/sqlite3.html)
	* 发现一个问题就是都有一部先```create_database```的过程
	* 但我搜了一下可以很简单的使用```create table if not exists```更加方便
* 然后发现的一个问题是我点击运行项目时,并没有出现网页,反而是终端运行server的界面
	* 比对自己和同学以及WebApp Sample才看出来是开头的声明部分```#qpy:webapp:MyDiaryQpy```格式必须是这样的,才能直接打开title是```MyDiaryQpy```的网页出来
		* 头声明可参考[官方文档此处](http://wiki.qpython.org/doc/program_guide/)

## 3. 本地命令行client
* 直接把6w的代码拿过来直接可以跑

## 其他
* 有关fabric自己还需要再补补课
* 在最开始环境配置过程浪费太多时间,原因是一开始没有理解到root手机才能进入想要进入的目录,其余用scp,BusyBox,SSHDroid或者adb或者数据线直接传都是进一步的姿势~
	* 这一部分姿势需要再捋下条理


##Changelog
201512005 创建编辑

