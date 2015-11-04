# MyDiaryNet

## 前期背景调查

### 什么是UDP协议
* [wiki](https://en.wikipedia.org/wiki/User_Datagram_Protocol)
* http://www.erg.abdn.ac.uk/users/gorry/course/inet-pages/udp.html
* UDP - User Datagram Protocal 用户数据报协议
	* 用来支持需要在计算机之间传输数据的网络应用
	* 使用IP协议的上层
	* unreliable 不可靠的服务
	* 但是小巧高效
	* 不经过中间系统 Intermediate Systems (IS)，直接原样到final destination
	* 2个字节存放端口，0-65535有效

### 什么是C/S架构系统
* [wiki](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* Client/Server 结构
	* client和server分离，每一个客户端都可以向服务器发出请求，等待回复
	* 具体例子如email，network printing，world wide web

### 官方文档学习
* [官方文档socket](https://docs.python.org/2.7/library/socket.html)
* [socket HOWTO](https://docs.python.org/2/howto/sockets.html)
* socket - 接口的意思
	* 首先要将client socket和server socket分开
	* 当用户端向服务器请求数据时，发生了什么？
		* 用户端create了一个接口，socket object，通过端口连到web上
		* 然后用户端的接口提交请求，阅读回复，最后destroy
		* 用户端接口一般只有一次交换数据
```python
# create a TCP socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80- the normal http port 
# 通过端口连到一个服务器上
s.connect(("www.mcmillan-inc.com", 80))
```
	* 服务器这边发生了啥呢？
		* 首先也是create了一个接口
		* 然后通过端口80收听
```python
# create a TCP socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host,and a well-known port
# 将接口接到了一个主机上，数字较小的端口一般是一些well known service
serversocket.bind((socket.gethostname(), 80))
# become a server socket
# listen 表示最多可以接受5个连接排队
serversocket.listen(5)
```
	* 具体通信是如何完成的呢？
		* 主循环
		* 服务器socket并没有传输数据，它只是制造了clientsocket
		* 之后每个clientsocket会对应之前做出连接申请额用户端socket，它们之间会继续chat
		* 而服务器socket在制造了clientsocket之后就会立即回到listen部分，继续接听其他连接请求
```python
while 1:
#accept connections from outside 通过accept接受连接
(clientsocket, address) = serversocket.accept()
#now do something with the clientsocket. In this case, we'll pretend this is a threaded server
ct = client_thread(clientsocket)
ct.run()
```
	* 接下来两个client socket如何对话？
		* ```socket.send(string[, flags])```发送data
		* ```socket.recv(bufsize[, flags])```接受data
		* ```close``` 要记得关闭接口

	* blocking & non-blocking socket？
		* 可参考[faketook同学](https://faketooth.gitbooks.io/omooc2py/content/0MOOC/3w/SprintLog_3wd1.html)

### 教程参考
* 使用TCP协议的教程
	* [Python socket – network programming tutorial](http://www.binarytides.com/python-socket-programming-tutorial/)
	* [Code a simple socket server in Python](http://www.binarytides.com/python-socket-server-code-example/)
	* [TCP/IP Client and Server](https://pymotw.com/2/socket/tcp.html)
* UDP教程
	* [Programming udp sockets in python](http://www.binarytides.com/programming-udp-sockets-in-python/)
	* [User Datagram Client and Server](https://pymotw.com/2/socket/udp.html)
* 有关为什么这次任务使用UDP而不是TCP
	* [jasonycliu同学的说法](https://jasonycliu.gitbooks.io/omooc2py/content/1sTry/net101.html)
	* 他觉得是因为TCP比较复杂，还有引入线程的概念，所以才选择UDP
	* 个人觉得TCP并没有复杂到很难理解的地步，单纯对于写代码来说，并不会有很难完成的地方
	* 我猜想和后续任务有关，之后再验证
## 任务拆解
* 分为server和client两部分
	* server：
		* create socket 创建接口
		* bind socket to address 将接口与host地址连接起来
		* waiting for receiving data 等待用户请求
		* 用户请求为r/sync：返回更新的日记
		* 用户发送来new diary：接受data写入file
	* client：
		* create socket 创建接口
		* 请求server输出old log
		* 等待用户输入
		* 用户输入?/h/help ：打印帮助菜单
		* 用户输入q/quit：退出程序
		* 用户输入r/sync：请求server返回更新后的日记
		* 其他输入视为new diary发送给server，server接收到data会更新入file
													
* 备选项：
	* 是否能保存笔记的客户端来源?
		* 思考：通过server端的recvfrom返回的address，也就是客户端的address，附加到每个新加diary的前面 ```From <address>```
	* 并在合适的情景中输出?
		* 思考：合适的情景是指啥？
	* 进一步的,能根据客户端不同,要求输出不同客户端提交的笔记嘛?
		* 思考一：不同客户端保存不同的file？
		* 思考二：通过前面保存的笔记的客户端来源，筛选出给不同客户端提交的笔记？

