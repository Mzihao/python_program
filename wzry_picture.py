# -*- coding:UTF-8 -*-
from urllib import request
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}
def loadImage():
    url = 'https://pvp.qq.com/web201605/herolist.shtml'
    req = request.Request(url,headers=headers)
    response = request.urlopen(req)
    html = response.read()
    content = etree.HTML(html)
    link_list = content.xpath('//ul/li/a/img[@width=91]/@src')
    name_list = content.xpath('//ul/li/a/img[@width=91]/@alt')
    for i in range(0,len(link_list)):
        link = link_list[i]
        name = name_list[i]
        writeImage(link,name)

def writeImage(link,name):
    print(link,name)
    link = 'https:' + link
    req = request.Request(link)
    response = request.urlopen(req)
    image = response.read()
    filename = name+'.jpg'
    f = open("C:/Users/admin/Desktop/爬的东西/王者荣耀/" + filename, 'wb')
    f.write(image)
    f.close()

if __name__ == '__main__':
    t1 = time.time()
    loadImage()
    t2 = time.time()
    print(t2-t1)