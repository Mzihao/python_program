import urllib.request
import re
url = "https://blog.csdn.net/"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
opener = urllib.request.build_opener() #创建支持处理HTTP请求的opener对象
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat = '<a href="https://blog.csdn.net/(.*?)"'
result = re.compile(pat).findall(data)
# print(result) # ['briblue/article/details/108050889', 'briblue/article/details/108050889', 'briblue/article/details/108050889']
for i in range(0,len(result)):
    file = "C:/Users/admin/Desktop/爬的东西/csdn/"+str(i)+".html"
    urllib.request.urlretrieve("https://blog.csdn.net/"+result[i],filename=file) #将"https://blog.csdn.net/"+result[i]的内容写入filename中
    # print(result[i])
    print("the "+str(i)+" page")