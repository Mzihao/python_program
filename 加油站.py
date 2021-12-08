import requests

url = "https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=baidu&pcevaname=pc4.1&qt=spot&from=webmap&c=340&wd=%E5%8A%A0%E6%B2%B9%E7%AB%99&wd2=&pn=0&nn=0&db=0&sug=0&addr=0&&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=11.94604502186288&rn=50&tn=B_NORMAL_MAP&auth=LfLe5gddYFLDP%3DvEZI2Jf%40IVwwTbaELFuxLBRTNTzTHtBalTBnlcAZzvYgP1PcGCgYvjPuVtvYgPMGvgWv%40uxtw8055yS8v7uvYgP%40vYZcvWPCuVtvYgP%40ZPcPPuVtvYgPhPPyheuVtvhgMuxVVty1uVtCGYuVt1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuVtPYIuVtcvY1SGpuxLt%40jUfJxvYlcvIKMNQTXZbegHcEWe1aDYyuVt%40ZPuxtdKDv7ueuVtegvcguxLBRTNTzRVteh33uVtrZZWuV&seckey=AmgrjPaHC7Y9LzJ3iC8JisMdyrkW7KQE10lt7rcqKak%3D%2CR8iwnmoKQzC77Z4zQpthFaMlxI2H9Dh9XXG1F9NIQSQbCjat0FHSAp%2BIPO6cQGabJ35pRxra5P1dyQFrH4XN2xb6VWiclSzLru%2Bu4KO9RZzGsAu3zf5XoJou6sP7thQVUDMF38IvFEtVM9xHXBDcdc2W5MrylHcnQT9voraBt5LW7UCVsSBJaS8TwW8%2B1Ynf&u_loc=12696204,2557392&ie=utf-8&b=(12636366.07506703,2548562.69411458;12686726.715741793,2595335.637432566)&t=1638979295409&newfrom=zhuzhan_webmap"

payload={}
headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"',
  'Accept': '*/*',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://map.baidu.com/search/%E5%8A%A0%E6%B2%B9%E7%AB%99/@12686518.072539682,2571262.84,11.95z?querytype=s&c=340&wd=%E5%8A%A0%E6%B2%B9%E7%AB%99&da_src=shareurl&on_gel=1&l=11&gr=1&b=(12636366.07506703,2548562.69411458;12732038.004581092,2595335.637432566)&pn=0&device_ratio=2',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': 'BIDUPSID=245DA256C71C742C716323911FFB7944; PSTM=1631190840; BAIDUID=245DA256C71C742CE1375740A17E60D2:FG=1; __yjs_duid=1_b12fb9449d759887b055ec08982a9d821631285556867; BDUSS_BFESS=xVUVZBRG9mUWgyTEh5ZW82YVV6R0tXWWV6OFo0OWVrSGd6ZjNpdksxd1dWOEZoRUFBQUFBJCQAAAAAAAAAAAEAAAAVxpHLbXpowvMxMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbKmWEWyplhNU; BAIDUID_BFESS=245DA256C71C742CE1375740A17E60D2:FG=1; delPer=0; PSINO=7; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=35358_35292_35106_31660_35239_35435_34584_34517_34606_35328_35323_26350_35209_22160; BA_HECTOR=ah20ak21a0a5a124931gr1lm20r; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; M_LG_UID=3415328277; M_LG_SALT=3fd8133b0df5217944efd34b17345d32; validate=44015; ab_sr=1.0.1_ZTE5ZmY0MWY4NjlhYjdmOTA1ZmMyY2JjNDdlMzI0MmM2MDk0MTVlYmVmZGM3MjkxNjhjOGE0ZWUxZmU0OThlZGVmNjFjNWFhOTc2YTk1MGU1YzExZDg4ZGIwYTkzYjIyODhlNTI1YmIxNGY5NjExZDJiNWEyN2VmMzVkN2E2ZThjNGEwMjc4ZTI5OGUyMjVmNmFiYThkMjlhMjZlNTYyZA=='
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
content = data['content']
for i in content:
  addr = i['addr']
  tel = i.get('tel')
  name = i['name']
  print(addr)
  print(tel)
  print(name)
  print('==============')
