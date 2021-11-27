import urllib.request
import re
import urllib.error
for i in range(1,10):
    pageurl="https://www.58pic.com/piccate/10-0-0-p"+str(i)+".html"
    data=urllib.request.urlopen(pageurl).read().decode("utf-8","ignore")
    pat='<li><img src="(.*?)"></li>'
    imglist=re.compile(pat).findall(data)
    for j in range(0,len(imglist)):
        try:
            thisimg=imglist[j]
            thisimgurl="http:"+thisimg
            file="C:/Users/admin/Desktop/爬的东西/千图网/"+str(i)+str(j)+".jpg"
            urllib.request.urlretrieve(thisimgurl,filename=file)
            print("第"+str(i)+"页第"+str(j)+"个图片爬取成功")
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
            if hasattr(e,"reason"):
                print(e.reason)
        except Exception as e:
            print(e)
