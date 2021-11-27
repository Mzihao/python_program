from urllib import request
import re

url = "https://read.douban.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
req = request.Request(url,headers=headers)
data = request.urlopen(req).read().decode("utf-8")
# print(data)
pat  ='"id":.*?,"name":"(.*?)"'
lists=re.compile(pat).findall(data)

fh = open("C:/Users/admin/Desktop/爬的东西/豆瓣标题/1.txt",'w')
for i in range(0,len(lists)):
    fh.write(lists[i]+"\n")
# print(list)