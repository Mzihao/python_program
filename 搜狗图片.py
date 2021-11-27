# -*- coding:UTF-8 -*-
import requests
import json
from urllib import request
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Host': 'pic.sogou.com',
        'Referer': 'https://pic.sogou.com/pics?query=%E8%BD%A6%E7%89%8C&ie=utf8&p=40230500&st=255&mode=255&policyType=0&rawQuery=%E8%BD%A6%E7%89%8C',
}
def spider():
    for i in range(0,18):
        url = 'https://pic.sogou.com/napi/pc/searchList?mode=255&start=' + str(i*48) + '&xml_len=48&query=%E8%BD%A6%E7%89%8C&rawQuery=%E8%BD%A6%E7%89%8C&st=255'
        res = requests.get(url, headers=headers)
        jsondict = json.loads(res.text)
        # print(len(jsondict['data']['items']))
        print('第'+str(i+1)+'页')
        for j in range(0, len(jsondict['data']['items'])):
            jsondict = json.loads(res.text)
            # print(jsondict['data']['items'][j]['locImageLink'])
            if j+1 >= 10:
                fh = open('G:/车牌/' + str(i+1) + str(j+1) + '.jpg', 'wb')
            else:
                fh = open('G:/车牌/' + str(i + 1) + '0' + str(j + 1) + '.jpg', 'wb')
            if len(jsondict['data']['items'][j]['locImageLink']) > 0:
                # 向页面发起请求 获取到请求对象
                req = request.Request(jsondict['data']['items'][j]['locImageLink'])
                # 打开响应的对象
                response = request.urlopen(req)
                # 获取响应的内容
                image = response.read()
                # print(image)
                fh.write(image)
                fh.close()
                if j + 1 >= 10:
                    print('第' + str(i+1) + str(j+1) + '完成！')
                else:
                    print('第' + str(i + 1) + '0' + str(j + 1) + '完成！')
spider()