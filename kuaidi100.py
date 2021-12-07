import requests
import json
import time

"""简单写下，通过请求头解决了爬虫返回错误物流信息的问题。可以用自己的快递单号试试与爬虫所得是否一致。"""


def query_kuaidi100(id):
    """
    id: 快递单号
    """
    time.sleep(2)
    url1 = """https://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text={}""".format(id)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    text = requests.post(url1, headers=headers, data='{}').text
    js = json.loads(text)
    print(js)
    posttype = js['auto'][0]['comCode']
    postid = js['num']
    url2 = """https://www.kuaidi100.com/query?type={}&postid={}&temp=0.8926864614539474&phone=""".format(posttype,
                                                                                                         postid)
    headers = {
        "Referer": "https://www.kuaidi100.com/?from=openv",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty"
    }
    response = requests.get(url2, headers=headers, data='{}').text
    js = json.loads(response)
    print(js)
    s = ""
    for i in js['data']:
        s += i['time']
        s += "  "
        s += i['context']
        s += '\n'
    return s


if __name__ == '__main__':
    result = query_kuaidi100('9885523659001')
    print(result)
    print('=' * 30)
    result = query_kuaidi100('YT6160922922422')
    print(result)
    print('=' * 30)
    result = query_kuaidi100('75835676850665')
    print(result)
