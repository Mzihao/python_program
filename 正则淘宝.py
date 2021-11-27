# -*- coding:UTF-8 -*-
import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from config import *
from urllib.parse import quote
import time
from lxml import etree

KEYWORD = input('请输入你要搜索的商品：')
sta = input('请输入开始的页数：')
ove = int(input('请输入结束的页数：'))
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
'''建议设置时长30s以上'''

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = KEYWORD
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page == 1:
            html = browser.page_source  # 获取源码
            doc = etree.HTML(html)
            a = doc.xpath("//div[contains(@class,'login-blocks')]/a[@class='password-login-tab-item']/text()")
            # print(a)
            if len(a) > 0:
                name = browser.find_element_by_name("fm-login-id")
                name.clear()
                name.send_keys('麦mzh')
                passwd =browser.find_element_by_name("fm-login-password")
                passwd.clear()
                time.sleep(2)
                passwd.send_keys('mzh19980112')
                button = browser.find_element_by_class_name('fm-button')
                button.click()
            wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'),str(page)))  # 判断页数是否相等，返回true/false
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))  # 信息块
            # print('成功！！！！！！！！！！！！！！')
            get_products()
        if page > 1:#页数大于1就要模拟点击选择页数。
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            time.sleep(5)
            submit.click()
            wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))#判断页数是否相等，返回true/false
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))#信息块
            # print('成功！！！！！！！！！！！！！！')
            get_products()
    except TimeoutException:
        index_page(page)

def get_products():
    """
    提取商品数据
    """
    html = browser.page_source #获取源码
    doc = etree.HTML(html)
    # title = doc.xpath("//div[@class='row row-2 title']/text()")
    image = doc.xpath("//div[contains(@class,'pic')]/a/img/@data-src")
    price = doc.xpath("//div[contains(@class,'g_price g_price-highlight')]/strong/text()")
    deal = doc.xpath("//div[@class='deal-cnt']/text()")
    shop = doc.xpath("//div[contains(@class,'shop')]/a/span[2]/text()")
    if len(image) == len(deal):
        for i in range(0,len(image)):
            product = {
                #'title':title[2*i-1]+title[2*i],
                'image': image[i],
                'price': price[i],
                'deal': deal[i],
                'shop': shop[i],
            }
            print(product)
            save_to_mongo(product)
    else:
        print("这一页异常")

def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')

def main():
    """
    遍历每一页
    """
    for i in range(int(sta),ove+1):
        index_page(i)
    browser.close()

if __name__ == '__main__':
    main()