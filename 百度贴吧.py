from urllib import request,parse # from 包名 import 文件名
import ssl
import random
from lxml import etree

ua_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
]


# 加载一个页面
def loadPage(url):
    # 随机选择一个userAgent
    userAgent = random.choice(ua_list)
    headers = {
        'User-Agent':userAgent
    }

    # 向页面发起请求 获取到请求对象
    req = request.Request(url,headers=headers)
    # 创建未经过验证的上下文 防SSL（证书）错误
    context = ssl._create_unverified_context()
    # 打开响应的对象
    # 函数用于实现对目标url的访问。
    response = request.urlopen(req, context=context)
    # 获取响应的内容
    html = response.read()
    # 对unicode编码进行解码
    content = html.decode('utf-8')
    # 使用etree对html的内容建立文档树
    content = etree.HTML(content)
    # 使用xpath规则分析
    link_list = content.xpath('//a[contains(@class,"j_th_tit")]/@href')
    for link in link_list:
        fulllink = 'https://tieba.baidu.com' + link
        loadImage(fulllink)

# 加载帖中的图片的链接
def loadImage(url):
    # 随机选择一个userAgent
    userAgent = random.choice(ua_list)
    headers = {
        'User-Agent':userAgent
    }
    # 向页面发起请求 获取到请求对象
    req = request.Request(url)
    # 创建未经过验证的上下文 防SSL错误
    context = ssl._create_unverified_context()
    # 打开响应的对象
    response = request.urlopen(req, context=context)
    # 获取响应的内容
    html = response.read()
    # 对unicode编码进行解码
    content = html.decode('utf-8')
    # 使用etree对html的内容建立文档树
    content = etree.HTML(content)
    # 使用xpath规则分析
    link_list = content.xpath('//img[@class= "BDE_Image"]/@src') #//img[contains(@class,"BDE_Image")]/@src
    for link in link_list:
        print(link)
        writeImage(link)

# 把图片下载并保存到本地
def writeImage(url):
    # 随机选择一个userAgent
    userAgent = random.choice(ua_list)
    headers = {
        'User-Agent': userAgent
    }
    # 向页面发起请求 获取到请求对象
    req = request.Request(url)
    # 创建未经过验证的上下文 防SSL错误
    context = ssl._create_unverified_context()
    # 打开响应的对象
    response = request.urlopen(req, context=context)
    # 获取响应的内容
    image = response.read()
    # 把图片二进制格式的内容写入到文件中
    filename = url[-15:]
    f = open("C:/Users/admin/Desktop/爬的东西/爬取百度贴吧图片/"+filename,'wb')
    f.write(image)
    f.close()

#设置起始页和终止页
def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage,endPage+1):
        pn = 50 * (page-1)
        fullurl = url + '&pn=' + str(pn) # 完整的url
        print(fullurl)
        loadPage(fullurl)

if __name__ == '__main__':
    # 用户输入参数
    kw = input('请输入要爬取的贴吧：')
    beginPage = int(input('请输入起始页：'))
    endPage = int(input('请输入终止页：'))

    # 把用户输入的中文通过unicode进行解码
    key = parse.urlencode({'kw': kw}) #kw=kw
    url = 'https://tieba.baidu.com/f?' + key
    tiebaSpider(url, beginPage, endPage)