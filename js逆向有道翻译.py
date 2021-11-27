import requests
import time
from hashlib import md5
import json
import random


def maintain_cookies():
    url = 'http://fanyi.youdao.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    session.get(url, headers=headers)


# 加载一个页面
def spider_youdaofanyi():
    headers = {
        'Host': 'fanyi.youdao.com',
        'Origin': 'http: // fanyi.youdao.com',
        'Referer': 'http: // fanyi.youdao.com /',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
    }
    e = input("请输要翻译的词语：")
    t = time.time()
    ts = str(int(t * 1000))
    salt = ts + str(int(t * 10000))
    str_1 = 'fanyideskweb' + e + salt + 'Tbh5E8=q6U3EXe+&L[4c@'
    md = md5()
    md.update(str_1.encode())
    sign = md.hexdigest()
    # post请求的参数
    data = {
        'i': e,
        'from': ' AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': ts,
        'bv': 'd17d9dd026a611df0315b4863363408c',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    # print(e, ts, salt, sign, data)
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    # 打开响应的对象
    response = session.post(url, headers=headers, data=data)
    # 获取响应的内容
    html = response.text
    # print(html)
    return html


def fanyi():
    html = spider_youdaofanyi()
    jsondict = json.loads(html)
    return jsondict['translateResult'][0][0]['tgt']


if __name__ == '__main__':
    session = requests.session()
    maintain_cookies()
    result = fanyi()
    print('翻译结果是：', result)
