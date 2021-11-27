import urllib.request
keywd = input("请输入你要搜索的内容：")
keywdurl=urllib.request.quote(keywd)#url转码
url="http://www.baidu.com/s?wd="+keywdurl+"&ie=utf-8&tn=96542061_hao_pg"
req=urllib.request.Request(url) # 向页面发起请求 获取到请求对象
# print(req) #<urllib.request.Request object at 0x000002BCAD78C5C0>
data=urllib.request.urlopen(req).read() # 获取源代码
fh=open("C:/Users/admin/Desktop/爬的东西/"+keywd+".html","wb")
fh.write(data) # 写入数据
fh.close()