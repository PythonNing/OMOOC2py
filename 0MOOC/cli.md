# CLI 入门

win7/Powershell

From LPTHW

| CLI | meaning |
| -- | -- |
| ```pwd``` | print working directory |
| ```hostname``` | my computer's network name |
| ```mkdir``` | make directory |
| ```cd``` | change directory |
| ```ls``` | list directory |
| ```rmdir``` | remove directory |
| ```pushd``` | push directory 推送路径|
| ```popd``` | pop directory 弹出路径|
| ```cp``` | copy a file or directory |
| ```robocopy``` | robust copy 更可靠的复制命令 |
| ```mv``` | move a file or directory 重命名 |
| ```more``` | page through a file 逐页显示整个文件 |
| ```type``` | print the whole file |
| ```forfiles``` | run a command on lots of files |
| ```dir -r``` | find files |
| ```select-string``` | find things inside files 文件中查找内容 |
| ```help``` | read a manual page |
| ```helpctr``` | find what man page is appropriate |
| ```echo``` | print some arguments |
| ```set``` | export/set a new environment variable |
| ```exit``` | exit the shell |
| ```runas``` | Danger!become super user root |
| ```New-Item``` | 创建空文件 |

* ```mkdir ..temp/"I have fun"```使用引号创建包含空格的名字的目录
* 一般使用```/```表示路径，在win下```\```有相同功能
* 使用```cd ../../..```往上层目录移动
* ``cd ~``回到home路径
* ```dir -R```可以将当前目录下以及子目录打印出来
* ```mkdir -p i/like/icecream```在当前路径创建新的路径，相当于同时创建3个嵌套目录
* ```pushd i/like/icecream```直接进入```icecream```目录下，记录下当前位置并跳转到后一个路径
* ```popd```返回推送过的路径，类似于点击返回键，不是返回上层目录
* ```New-Item iamwho.txt -type filw``` 创建空文件iamwho.txt
* ```cp a.txt b.txt```复制a.txt成b.txt
* ```cp a.txt b/```复制a.txt到b这个目录下面
* ```mv a.txt b.txt```重命名a.txt为b.txt
* ```more test.txt```可以逐页浏览文件，windows用空格键往下翻页
* ```cat test.txt```一次性显示所有文件内容
* ```rm a.txt```删除文件
* ```rm -r directory```删除目录以及目录下文件


http://ss64.com/
