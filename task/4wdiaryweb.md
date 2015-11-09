# MyDiary Web Application

任务需求
> 通过网页访问笔记系统
> 每次运行时合理打印出以往所有笔记
> 一次接收输入一行笔记
> 在服务端兼容3w的Net版本命令行界面进行交互

## 背景知识
这次的背景知识我是写完代码才补的. 其实这些对于完成这次任务的直接影响不大, 但是想深入展开, 自己开脑洞联想的话, 那就是必须多了解了解的~

### web框架
* [wiki](https://en.wikipedia.org/wiki/Web_application_framework)
* 是一种软件框架,来支持动态网站,web应用,web服务等的开发
* 框架有助于减轻网页开发时的共通性工作负荷,提升代码的可再用性
* eg, 许多框架提供数据库访问接口, 标准模板以及会话管理等

### REST-Representational state transfer
* [wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)
* REST是一种软件架构风格, 不是标准
* 通常基于使用HTTP, URI和XML和HTML现有的广泛流行的协议及标准
	* 资源由[URI](https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E8%B5%84%E6%BA%90%E6%A0%87%E5%BF%97%E7%AC%A6)指定
		* Uniform Resource Identifier 是一个用于表示某一个互联网资源名称的字符串
		* 允许用户对网络中的资源通过特定的协议进行交互
		* 最常见形式就是URL(uniform/universal resource locator), 有时俗称为网址
		* 较少见的是URN(uniform resource name)
		* 对于一个资源URI,URN定义它的身份/名称,URL提供查找它的方法,经常是互补的
	* 对资源操作,对应[HTTP](https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE)协议的GET,POST,PUT,DELETE
		* HTTP(HyperText Transfer Protocol)是互联网应用最广的网络协议
		* HTTP是一个客户端和服务器端请求和应答的标准(TCP协议)
		* HTTP/1.1协议中定义了8种方法对资源进行操作:
			* OPTIONS:传回所有HTTP请求方法
			* HEAD:向服务器发出指定资源请求,但不传回资源的本文部分,只获取关于该资源的信息
			* GET:向指定资源发出"显示"请求,应该只用于读取数据
			* POST:向指定资源提交数据,如提交表单或上传文件
			* PUT:向指定资源位置上传其最新内容
			* DELETE:请求服务器删除Request-URI所标识的资源
			* TRACE:显示服务器收到的请求,主要用于测试或诊断
			* CONNECT:预留给能够将连接改为渠道方式的代理服务器,通常用于SSL加密服务器的链接
			* [HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
	* 通过操作资源的表现形式来操作资源
	* 资源的表现形式则是[XML](https://zh.wikipedia.org/wiki/XML)或[HTML](https://zh.wikipedia.org/wiki/HTML)等
		* XML,HTML都是一种markup language,标记语言,标记指计算机能理解的信息,计算机之间可以通过这些标记处理信息
* RESTful风格要求
	* client/server结构
	* 链接协议具有无状态性stateless,每个请求与之前请求都无关
	* 能够利用Cache机制增进性能(快照)
	* 层次化结构, intermediary server
	* code on demand(可选),服务器可以临时对某个客户端进行扩展
	* 统一风格界面
* 其他阅读: [REST 入门介绍](http://www.cnblogs.com/shanyou/archive/2012/05/12/2496959.html)

### python web框架
* [python web server gateway interface](https://www.python.org/dev/peps/pep-0333/)
* [python的一些web框架推荐, 包括Django,CherryPy,Flask,Bottle等](http://www.open-open.com/news/view/774e1f)
* Bottle优点在于轻巧,只需要一个bottle.py的file就可以快速进行开发
* So be pythonic!

---

针对任务还是可以从bottle官方tutorial开始着手

## 发布一个网站
[commit 3aadf46](https://github.com/bambooom/OMOOC2py/blob/3aadf461941e0a178be076cdf6a013c4d801eadf/_src/om2py4w/4wex0/main.py)
```python
from bottle import route, run

@route('/hello')
def hello():
	return "Hello World!"

run(host='localhost', port=8080, debug=True)
```
就是这样一个网站就可以发布出来,用浏览器打开http://localhost:8080/hello 就可以看到网页上显示"Hello World!"

* 具体来看, @route就是定义一个网页路由是../hello
* 这个网页上是有什么东西呢?由hello()这个method定义的
* hello() return的就是个字符串"Hello World!",所以网页上就会显示出来
* 而最后的run就是让服务器端开始运作

## 动态网页
[commit e8156b9](https://github.com/bambooom/OMOOC2py/blob/e8156b9c37803ecbd991f3b1043953161127c584/_src/om2py4w/4wex0/main.py)
```python
from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
	return template("Hello {{name}}, how are you?", name=name)

run(host='localhost', port=8080, debug=True)
```
* 定义了两个route都是同一个callback method
* 但是打开http://localhost:8080/会显示"Hello Stranger.."
* 而打开http://localhost:8080/hello/<name>都会显示出"Hello <name>, how are you?"
* 网址的name会传给greet
* template模板相当于一个html的文件,bottle return出来的是html代码,传入浏览器,就可以将html用于显示网页

## HTTP请求方法
[commit 66a6c83](https://github.com/bambooom/OMOOC2py/blob/66a6c839fa93f7528af2111c761afc1e49b02422/_src/om2py4w/4wex0/main.py)
```python
from bottle import request,route,run
@route('/login')
def login():
	return '''
	<form action="/login" method="post">
	Username: <input name="username" type="text" />
	Password: <input name="password" type="password" />
	<input value="Login" type="submit" />
	</form>
	'''

@route('/login', method='POST')
def do_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	if check_login(username, password):
		return "<p>Your login information was correct.</p>"
	else:
		return "<p>Login failed.</p>"
```

* 打开网页http://localhost:8080/login就会显示出username和password两个输入框以及一个login的button
* @route默认是以GET方法获取数据,所以直接return了一大段html code
* 此段html code表示在网页创建表单forms,其中有username,password的输入框,并有一个login的button,这几个组件
* 而在同一个网页需要获得用户输入的数据, 用POST方法表示用户提交表单.提交之后,用bottle中的```request.forms.get```获取输入数据.
* 最后return给浏览器的也是html code

## html输入框以及打印日记框
* 了解了基本的HTTP请求及提交表单方法之后,针对任务本身,可以先解决掉html部分
* 就是在网页上显示出一个输入框让用户可以输入新日记
* 一个提交button
* 一个文字框打印出旧日记
* google了一下html里面有些什么可以实现以上三个部分
	* 从前一个例子里就可以知道前两个部分,都是用```<input>```只是设定不一样就可以了
	* 输入框```type="text", name="newdiary"```
	* 提交button```value="Submit", type="submit"```value是指button上显示的文字是什么
	* 文字框打印日记使用的是```<textarea>```
	* 文字框内要打印的日记变量设定为diarylog

```html
<!DOCTYPE html>
<html>
<body>

<form action="/mydiary" method="post">
  Input here: <input type="text" name="newdiary" />
  <input value="Submit" type="submit" />
</form>
<br>
<textarea rows="20" cols="50">
{{diarylog}}</textarea>

</body>
</html>
```

## template模板使用
* 如果直接在每次@route网页时return一大段html,会很重复,并且如果网页越来越复杂,html会很长很长,这时就需要用到template
* 我的理解template就是html code,是决定网页展示出来效果的
* bottle里面有最简单的simpleTemplate,非常简单,所以并不会好看,先放下美化这部分(美化这部分才需要用到jinja2和bootstrap)
* [commit eb5e57a](https://github.com/bambooom/OMOOC2py/blob/eb5e57a131ba2bda020f88e0964e75f08d77026f/_src/om2py4w/4wex0/main.py)

```python
from bottle import route, run template

@route('/mydiary')
def login():
	return template('diaryweb', diarylog="Hello World!")

run(host='localhost',port=8250, debug=True, reloader=True)
```
* bottle中的template,第一个argv是会在当前目录下寻找是否有diaryweb.tpl这样一个模板文件
* 我已将上一部分的html存成diaryweb.tpl模板,其中一个变量是diarylog,所以也通过template设定
* 这样就会在打开网页时看到输入框,提交button以及文字框,文字框中已打印出来Hello World!

## 输入提交并打印
* 搞定网页显示之后,就可以添加在输入框输入提交之后可以显示到文字框的功能
* 其实就是结合POST提交表单以及request获取数据,最后用template传到网页
* [commit 6c9821d](https://github.com/bambooom/OMOOC2py/blob/6c9821d3d6f82662b468cd1c022fe5ac512e205b/_src/om2py4w/4wex0/main.py)
```python
from bottle import request,route,run,template

@route('/mydiary')
def start():
	return template('diaryweb', diarylog='hello world')

@route('/mydiary', method=POST)
def input_new():
	newdiary = request.forms.get('newdiary')
	return template('diaryweb', diarylog = 'hello world \n'+newdiary)

run(host='localhost', port=8250, debug=True, reloader=True)
```
* 打开网页http://localhost:8250/mydiary就可以输入任何日记,点击submit或按回车键即可提交,并在文字框中看到输入的新日记

## 与file结合
* 输入提交并打印功能完备,最后只需要打印以及输入新的日记放到server本地文件里面就可以了
* [commit 0ed577f](https://github.com/bambooom/OMOOC2py/blob/0ed577fdb37858ba4653416982e909d3ff87ad3f/_src/om2py4w/4wex0/main.py)
```python
from bottle import request, route, run, template

@route('/mydiary')
def start(): # 打开网页时打印出旧日记
	log = read_diary() # 读取本地日记文件
	return template("diaryweb", diarylog=log) # 打印在网页文字框中

@route('/mydiary', method='POST')
def input_new():
	newdiary = request.forms.get('newdiary') # 获取用户提交数据
	write_diary(newdiary) # 写入本地文件
	log = read_diary() # 读取更新后日记文件
	return template("diaryweb", diarylog=log) #打印更新后日记文件在文字框中
```
* 喜大普奔!bottle部分完成了!虽然还没有美化~

---
* 任务的另一半是客户端通过CLI也可以与网页端交互
* 主要包括获取网页数据,提交数据至网页两部分
* 待更新
