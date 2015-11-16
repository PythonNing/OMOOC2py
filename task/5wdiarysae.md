### 5w MyDiary SAE

# 背景知识
* PaaS - Platform as a Service平台即服务
    * [wiki](https://en.wikipedia.org/wiki/Platform_as_a_service)
    * 一种云计算服务
    * 用户可以在平台上面开发,运行,管理web application,用户不需要管理和控制基础设施
    * 比如Google App Engine
* SAE - Sina App Engine[新浪云应用](http://www.sinacloud.com/doc/sae/python/index.html)
    * 国内最大PaaS
* KVDB - [分布式key-value database](http://www.sinacloud.com/doc/sae/python/kvdb.html)
    * 可扩展NoSQL键值数据库服务
* [NoSQL](https://en.wikipedia.org/wiki/NoSQL) - Non SQL
    * 不使用传统的关系型数据库
    * 不使用SQL作为查询语言
    * 数据存储不需要固定的表格模式
    * 使用硬盘，或者把随机存储器作存储载体

---

# 任务记录
## 1.sae本地环境部署
* [安装sae](http://www.sinacloud.com/doc/sae/python/tools.html)
	* ```$ pip install sae-python-dev```
	* 或者github下载源码安装
* 在本地开发目录新建index.wsgi和config.yaml [参考](http://www.sinacloud.com/doc/sae/python/tutorial.html)
	* 应用配置文件config.yaml内容如下:
```
name: helloworld
version: 1
```	
	* 使用bottle的index.wsgi内容如下:

```python
from bottle import Bottle, run

import sae

app = Bottle()

@app.route('/')
def hello():
    return "Hello, world! - Bottle"

application = sae.create_wsgi_app(app)
```

* 在本地开发目录下运行测试

```$ dev_server.py```

* 访问http://localhost:8080就可以访问应用了

## 2.改写4w代码
### 使用kvdb替代本地txt文件

* [kvdb文档](http://www.sinacloud.com/doc/sae/python/kvdb.html)
* kvdb类似python的dict data type

```python
import sae
import sae.kvdb
kv=sae.kvdb.Client()
```

* 参考小赖的设计:
	* key值为key1,key2,key3....即有几条日记就是key#
		* key值必须为string
		* 一开始尝试直接设置数字为key,然后有新diary就```key+=1```,报错```key must be str```
	* value就是每条日记是一个dict
	```python
	diary = {'time':edit_time, 'diary':newdiary}
	```
	* diary也可以设计为list,```[<time>,<diary>]```,但若增加其他的tag,author之类的功能之后,获取数据的时候会需要知道index,没有dict读取方便简洁
* 测试kvdb的几项基本功能
	* 设置key的值是value ```kv.set(key,diary)```
	* 获取key的值```kv.get(key)```返回的是diary的内容
	* ```kv.get_by_prefix('key')```是查找前缀是'key'的key/value pair,返回的是一个generator,例如可以在循环中返回(key,value)的tuple

### 改写```read_diary```和```write_diary```
* 一开始设想是```write_diary(newdiary,count)``` 把count设置为计数用,即可以加在key后作为key值,写进diary更新了database,在函式最后```count +=1 ```后```return count```就可以知道下次写新日记的时候是第几条.以及```read_diary(count)```也可以用个小循环一条条读取diary ([版本记录](https://github.com/bambooom/OMOOC2py/commit/bd8a31c675e86f52db2fe473be22e4b497ab5bd1))
* 然后想到可以用```kv.get_by_prefix('key')```循环,就不需要count作为```read_diary()```的参数了,仅作为key值的计数即可.
* 另外```read_diary()```本来设置读取的log是一个list,因为list可以很容易的用```len()```知道有多少条日记,但因为使用bottle的template返回的html需要string的参数,所以同时增加了一个string的log.([版本记录]((https://github.com/bambooom/OMOOC2py/commit/f6aeedafb81bc36edc019cf617d7632bb13b217c))
* 学习了template里使用循环打印出日记,比较结构化,也就不需要string的log了.

## 3.增加tag输入
* 先在template内添加tag的输入框 ```标签: <input type="text" name="tag" size="30"/>```
* 每条diary内添加'tag' ```diary={'time':edit_time,'diary':newdiary,'tag':tag}```

## 4.部署到SAE
* 在新浪云上创建应用,应用名称二级域名等之后,在```代码管理```处可以选择svn和git管理.选定之后不能修改.这里我选的git.在本地开发目录里
```
$ git init
$ git remote add sae https://git.sinacloud.com/bambooomhelloworld
$ git add .
$ git commit -am "test"
$ git push sae master:1
```
* 另外可以使用[saecloud](http://www.sinacloud.com/doc/sae/python/tools.html#saecloud)
	* saecloud从config.yaml获得信息,判断将要把代码部署到哪个应用的哪个版本.
	* 在命令行输入```$ saecloud deploy```
	* 但我运行时出现```windowserror```,error信息也都是问号,这个问题有待解决.所以我还是暂时用前一种比较麻烦的办法
* 碰到几个SAE的问题
	* 官方文档其实很多地方没有更新,有关用svn的地方,全部都不用管,使用git即可
	* 没有实名验证的用户只能创建2个应用
	* 不要随便删应用,不能马上删除,要恢复还要氪金
	* 代码最多只能有10个版本
	* 部署到同一个版本下的话,部署时间不会更新,一开始我还以为代码不会覆盖,但其实覆盖了,只是时间上没有更新看不出来orz
	* 网页出错显示不出来之类的话,可以去看错误日志,在控制台->运维->日志中心,选择版本和错误日志以及时间,即可看到运行时的error message,根据这个来修正bug就容易多了.但error message有时候写的不清楚......
		* 突发想法: 是否有工具可以在本地命令行直接查看错误日志?

## 5.改写4wCLI端代码
### 使用```requests```和```BeautifulSoup```
* 上周发现有同学用了这两个包之后,代码非常直接也很简洁.```requests```大妈演示时也讲过了,HTTP for human.比python标准库内的```urllib```和```urllib2```好用
	* ```r=requests.get(url)```访问网站,返回一个类似file object,```r.text```就可以得到html/css源码
	* ```BeautifulSoup```是一个解析html/xml之类的解析器,可以通过它很方便提取html内的相关信息
* ~~改写```get_log()```获取所有历史数据 [版本记录](https://github.com/bambooom/OMOOC2py/commit/c0b3f83f74ea0b4decdab70d9eb762700c82af8f)~~
```python
def get_log():
	response = requests.get("http://bambooomhelloworld.sinaapp.com/")
	soup = BeautifulSoup(response.text, "html.parser")
	tag = soup.textarea # 获取html内在textarea里的信息
	print tag.string # 需要转化成string
	# 若直接print temp,会连带html的<textarea>的tag一起打印出来
```
* ~~改写```write_log()```提交表单,用```requests.post```就很简单了 [版本记录](https://github.com/bambooom/OMOOC2py/commit/cc160b68ad5edf766f5adb193b0e2f3c397cb6a7)~~
* 因为自己的做法太蠢了,重新学习了template使用循环将日记打印出来,所以CLI的function全部需要修改.

## 6.添加ListTags和st:<TAG>功能
* 添加```get_tags()```函式获取所有的标签tags [版本记录](https://github.com/bambooom/OMOOC2py/commit/279dca9c32d1498a80253643a67ebff4313f408f)
	* ~~从```get_log()```获取历史记录后用正则表达中的```re.findall```找出所有的**TAG:<>**,返回一个list~~
	* ~~用```re.sub```去掉所有的前缀**TAG:**~~
	* 使用```soup```的```find_all()```可以将指定html tag下的内容解析出来
	```python
	temp =[]
	for i in soup.find_all('i', class_='tags'):
		temp.append(i.get_text())
	```
	* 获得一个每条日记的tags的list,里面会有重复的tags
	* ```tags = list(set(temp))``` set()可以理解为数学的集合概念,所以去掉了duplicate,最后返回的```tags```就是所有不同的标签的列表.
* 添加st:<TAG>输入判定,还是从小赖同学处学到用```str.startswith('st:')```来判定

## 7.添加打印某一tag下所有日记功能 ```get_log_bytag(tags)```
* ~~前面与从网页获取所有日志一样,获得日记string~~
* ~~因为我写入日记的时候设计的是一行时间,一行TAG,一行日记,所以现在对这个string我就用```splitlines()```分行,返回了一个list~~
* ~~用循环去判定每个tag是否为需要的提取的tag,是的话就将此tag的前后日期及日记提取出来~~
* ~~如果还没有任何历史记录也没有tag时,网页获取的string为```None Type```,不能进行string的操作,系统会报错.后面加入判定如果为空就pass [版本记录](https://github.com/bambooom/OMOOC2py/commit/940b3922f523ae099f8a9024f1f87dd11bef8728)~~
* 还是一样使用```soup.find_all()```获取特定tag下的内容
* 因为每一个diary的时间标签内容都是成组出现,所以只要判定标签为所需要标签,即可提取
此tag下所有日记

## 8.添加FLUSH功能删除所有日记
* 用到```requests.delete```,其实就是http协议中的DELETE去删除资源
* 需要也在```index.wsgi```中加上定义route的```method='DELETE'```
* 具体删除日记也就是在database中删除数据,在kvdb中删除所有key值即可
* 看了文档之后发现可以使用```kv.getkeys_by_prefix()```返回的就是key值的list,再用kv.delete()```删除即可删除记录.

## 9.未做事项
- [ ] 日记排序问题
- [ ] 网站访问记录
- [ ] 认证登录?
- [ ] 页面美化?
