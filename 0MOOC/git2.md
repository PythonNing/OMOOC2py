# Git

### 配置
* win7
* git for Windows

## 使用 - 最简单的编辑md文档后push
* 先在本地复制整个project下来
```git clone https://github.com/bambooom/OMOOC2py```

* 然后用```cd```进入相关目录，这次我是尝试在本地编辑.md然后再push

* 进入目录后，用vi或者vim打开编辑器进行编辑
```vi EVA.md```就会把文件打开预览了，点击```i```就可以进入```--INSERT--```模式进行编辑

![](g1.png)

* 编辑完了之后，按```esc```键就保存退出编辑模式了，再按```shift + : ```键，在最下面一行就会出现一个冒号，再输入```wq```，回车就可以退出文件回到平常的命令行界面了。

* 这时可用```git status```看看是有哪些change

* 然后```git commit -a```把所有的update先推送到本地缓存上

* 最后```git push```就可以把所有的commit推送到github/gitbook

* 如果在网页上有过直接的更改，可以先```git pull```把网页上的更新拖下来，再把本地的更新push上去

## 体验
* 前几周其实一直绕过git，今天终于有空搞懂了。
* 虽然还只是基础用法明白了，还有很多option可以用，但也感觉很开心了。该补的课终究要补哈哈哈~
* 另外直接能开```vi```就可以阅览/编辑文本实在太爽了
