# 6w MyDiaryWechat 微信公众号版日记

> * 将公网应用网站改写为公众号后台服务
> * 可以通过公众号使用:
>     * 使用专用指令,可打印出过往所有笔记
>     * 一次接收手机端输入的文字(不包含表情/图片/声音/视频...)
>     * 在服务端合理保存
>     * 同时兼容的命令行工具远程交互/使用/管理
> * 可以通过本地命令行工具监察/管理网站:
>     * 获得当前笔记数量/访问数量等等基础数据
>     * 可以获得所有笔记备份的归档下载
> * 备选:
>     * 如果分笔记类别呢?
>     * 如何建立认证功能,防止有人误入?
>         * 如果识别微信用户呢?
>         * 即,这是一个私人笔记系统,不接受其它人使用
>         * 当然,想作成多人也是相同的技术.
>     * 如何建立数据加密?防止有人通过分析网络协议伪造数据提交

- [x] 微信接入
- [x] 接受指令打印过往日记
- [x] 手机端输入日记
- [x] 命令行端指令模拟应答
- [x] 获得日记数量
- [x] 手机端订阅关注时打印帮助文档
- [x] 手机端/命令行都可以为日记加标签
    * 但手机端可以为一条日记添加多个标签
- [ ] 认证功能?
- [ ] 消息加密?


## 1. 微信接入5w网页应用 [版本](https://github.com/bambooom/OMOOC2py/commit/7659df107d5975759bd7cbb27114ead46adcb586)
* [官方文档](http://mp.weixin.qq.com/wiki/16/1e87586a83e0e121cc3e808014375b74.html)
* [廖雪峰](http://www.liaoxuefeng.com/article/0013900476318564121d01facf844cba508396f95d9bb82000)
* [另一篇就是用bottle和bae/sae搭建](http://www.cnblogs.com/weishun/p/weixin-publish-developing.html)
> 第一步: 填写服务器配置
> 第二步：验证服务器地址的有效性
> 第三步: 第三步：依据接口文档实现业务逻辑

* 重点为第二步,验证服务器地址有效性. 
* 验证的逻辑是这样:
	* 微信会发送一个GET请求到服务器URL上, 上面携带4个参数```signature-加密签名,timestamp-时间戳,nonce-随机数,echostr-随机字符串```
		* 例子: http://yoursaeappid.sinaapp.com//?signature=730e3111ed7303fef52513c8733b431a0f933c7c43&echostr=5853059253416844429&timestamp=1362713741&nonce=1362771581
		* bottle框架下,可以使用```request.GET.get()```获取这个请求里的4个参数
	* 将开发者自己填写的token,以及timestamp和nonce三个参数进行字典排序并拼凑成一个字符串后进行sha1加密
	* 上述结果与signature对比, 若正确则表示请求来源来自微信,返回echostr给微信即可验证成功
* 此处代码完全可以照抄他人的成果.另外,其实此验证的中间加密过程完全可忽略,只要获取echostr并返回echostr即可完成验证.
	* 我的理解是这样,微信做这个接入验证的目的只是检验服务器的有效性,服务器可以正常返回正确值即可.加密等的过程其实是对自己的网站或应用而言的保护.并不能让随便什么其他人就给自己的网站发出请求并接入.
	* 另外一点是,在第一次接入成功后,此验证代码即可注释掉,微信并不会不断发送此验证去检验服务器的有效性.
* 由此可以看出,微信在这里完全只是个展示的地方,一个连接处,所有的后台程序都不在微信,不由微信管理,数据库本身都是在新浪sae

### 微信接入时遇到了坑
* 几乎完全照抄他人教程里的代码,但微信接入sae就是不成功. 在自己无法找到问题的时候, 不要大意地求助吧!
* 所以问了赖同学.有大腿就是好~赖同学帮我找到问题的根源是因为我新浪sae没有实名认证过,所以会在网页自动出现悬浮框提示,这个悬浮框的html源码造成我返回给微信的echostr就是不匹配的. 这时才意识到上周教练free提示说尽早去实名认证不会踩坑.....
* anyway,最终感谢教练告诉我还可以通过已经有实名认证过的人邀请我协作开发的方法来解决.
* 所以说有问题自己不知道怎么解决就求助,找同学,找教练,找大妈都可以~

## 2. 接收读取微信消息xml [版本](https://github.com/bambooom/OMOOC2py/commit/498429866d5f94b1c0da7c22375e4183b1d63563)
* [官方文档](http://mp.weixin.qq.com/wiki/17/fc9a27730e07b9126144d9c96eaf51f9.html)
* 还是参考前面提到教程,并且正好用的是标准库中的xml.etree.ElementTree来解析xml
* 因为微信消息是以xml形式传输, 文本消息的格式如下:
```xml
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName> 
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[this is a test]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>
```
* 真正的信息是被封装在```Content```这个tag里的
* 首先用bottle框架内的```request.body.read()```获取xml数据, 再使用```ElementTree```解析xml,可以分别通过不同tag提取信息,最终一条消息返回一个字典type的数据格式.
```python
def parse_xml_msg(recv_xml):
	recv_xml = request.body.read()
	root = ET.fromstring(recv_xml)
	msg = {}
	for child in root:
		msg[child.tag] = child.text
	return msg
```
* 返回msg的例子比如是这样的: ```msg={'FromUserName': 'omoocpy', 'MsgId': 'hdsicwecewew2233333', 'ToUserName': 'bambooom', 'Content': 'diary WTF', 'MsgType': 'text', 'CreateTime': '20151120'}```

## 3. 被动回复消息
* [官方文档](http://mp.weixin.qq.com/wiki/18/c66a9f0b5aa952346e46dc39de20f672.html)
* 接收时是xml形式,回复自然也是xml, 文本消息格式如下:
```xml
<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[fromUser]]></FromUserName>
<CreateTime>12345678</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[你好]]></Content>
</xml>
```
* 用户真正看到的内容也在```Content```里
* 并且此处的```FromUserName以及ToUserName```和接收消息时应该正好相反
* 通过读取和判定接收的消息内容```msg['Content']```就可以设置如何回复消息
