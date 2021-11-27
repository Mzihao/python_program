from urllib import request,parse # from 包名 import 文件名
import ssl
import random
import time

# 加载一个页面
def loadPage(url,word):
    headers = {
        'Host': 'fanyi.youdao.com',
        'Origin': 'http: // fanyi.youdao.com',
        'Referer': 'http: // fanyi.youdao.com /',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    }

    # 向页面发起请求 获取到请求对象
    req = request.Request(url, headers=headers)
    # 创建未经过验证的上下文 防SSL错误
    context = ssl._create_unverified_context()
    # post请求的参数
    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15910845361184',
        'sign': 'cfa197edea078cd26765c5b77695b0c2',
        'ts': '1591084536118',
        'bv': 'd17d9dd026a611df0315b4863363408c',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    #把data参数转化为url编码
    data = parse.urlencode(data).encode('utf-8')
    # 打开响应的对象
    response = request.urlopen(req, context=context,data = data)
    # 获取响应的内容
    html = response.read()
    # 对unicode编码进行解码
    content = html.decode('utf-8')
    # print(content)
    return content

import json
def fanyi(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule '
    content = loadPage(url,word)
    #print(content)
    jsondict = json.loads(content)
    #print(jsondict)
    return jsondict['translateResult'][0][0]['tgt']

if __name__ == '__main__':
    word = input('请输入你要翻译的单词：')
    result = fanyi(word)
    print('翻译结果是：',result)