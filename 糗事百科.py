# 多线程
import urllib.request
import threading
import re
import urllib.error
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
opener=urllib.request.build_opener()  #创建支持处理HTTP请求的opener对象
opener.addheaders=[headers]
urllib.request.install_opener(opener)
class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,14,2):
            url="http://www.qiushibaike.com/8hr/page/"+str(i)
            pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")
            pat='<a class="recmd-content" href=".*?" target="_blank" onclick="_hmt.push.*?">(.*?)</a>'
            datalist=re.compile(pat,re.S).findall(pagedata) #使用re.S参数，正则表达式会将这个字符串作为一个整体，在整体中进行匹配。
            for j in range(0,len(datalist)):
                print("第"+str(i)+"页第"+str(j)+"个段子的内容是：")
                print(datalist[j])
class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,14,2):
            url="http://www.qiushibaike.com/8hr/page/"+str(i)
            pagedata=urllib.request.urlopen(url).read().decode("utf-8","ignore")
            pat='<a class="recmd-content" href=".*?" target="_blank" onclick="_hmt.push.*?">(.*?)</a>'
            datalist=re.compile(pat,re.S).findall(pagedata)
            for j in range(0,len(datalist)):
                print("第"+str(i)+"页第"+str(j)+"个段子的内容是：")
                print(datalist[j])
one=One()
one.start()
two=Two()
two.start()
