import requests
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
}
baseurl = 'http://332dy.com/dili/34571.html'
html = requests.get(baseurl, headers=headers).text
content = etree.HTML(html)
urls = content.xpath('//div/ul[@class="d0ea40 rg5waf stui-content__playlist clearfix"]/li/a/@href')
# print(urls)
for i in urls:
    html2 = requests.get(i, headers=headers).text
    pat = '<mip-iframe width="600" height="400" src="(.*?)" layout="flex-item"></mip-iframe>'
    playurl = re.compile(pat).findall(html2)
    if playurl:
        print(playurl)