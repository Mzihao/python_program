import requests

url = "https://www.dongchedi.com/motor/pc/car/brand/get_select_series"

payload='offset=0&limit=30&is_refresh=1&city_name=%E6%B9%9B%E6%B1%9F&price=20%2C25'
headers = {
  'authority': 'www.dongchedi.com',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
  'content-type': 'application/x-www-form-urlencoded',
  'accept': '*/*',
  'origin': 'https://www.dongchedi.com',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.dongchedi.com/auto/library/20,25-x-x-x-x-x-x-x-x-x-x-x-x-x-x?tt_web_version=new',
  'accept-language': 'zh-CN,zh;q=0.9',
  'cookie': 'UM_distinctid=17894a7eec225e-08f6b922a94748-c3f3568-15f900-17894a7eec3512; MONITOR_WEB_ID=2e6aeece-41d6-413f-ad7c-1a418b4fb6ef; _ga=GA1.2.1443996008.1617401788; tt_web_version=new; is_dev=false; is_boe=false; tt_webid=6975403868071396901; ttwid=1%7C7FbbonhQETTYdckGF342ir3ZXk1BFy94tPVCriqNFpc%7C1624087775%7C7384efc96dc8685ae69535949c01f4986d1e345cfac9353abd0b47a40581ddfe; city_name=%E6%B9%9B%E6%B1%9F; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1624087778; CNZZDATA1278124308=201908327-1617401692-https%253A%252F%252Fwww.baidu.com%252F%7C1624085319; _gid=GA1.2.696711900.1624087788; _gat_gtag_UA_138671306_1=1; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1624087800'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
