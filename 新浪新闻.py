import urllib.request
import re
data=urllib.request.urlopen("http://news.sina.com.cn/").read()
data2=data.decode("utf-8","ignore")
pat='href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data2)
print(allurl)
for i in range(0,len(allurl)):
    try:
        print("第"+str(i)+"次爬取")
        thisurl=allurl[i]
        print(thisurl)
        # file="C:/Users/admin/Desktop/python数据分析与挖掘/第4章 Urllib库实战/sinanews/"+str(i)+".html"
        # urllib.request.urlretrieve(thisurl,file)
        print("-------成功-------")
    except urllib.error.URLError  as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)








