import requests
import time
import sqlite3
import json
# import pyecharts.options as opts
# from pyecharts.charts import WordCloud

url = "https://www.dongchedi.com/motor/pc/car/rank_data?month=1000&rank_data_type=11&offset={}&limit=10&city_name=%E5%B9%BF%E5%B7%9E&outter_detail_type=0,1,2,3,4,5"

headers = {
    'authority': 'www.dongchedi.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.dongchedi.com/sales?tt_web_version=new',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'UM_distinctid=17894a7eec225e-08f6b922a94748-c3f3568-15f900-17894a7eec3512; MONITOR_WEB_ID=2e6aeece-41d6-413f-ad7c-1a418b4fb6ef; _ga=GA1.2.1443996008.1617401788; tt_web_version=new; ttwid=1%7C7FbbonhQETTYdckGF342ir3ZXk1BFy94tPVCriqNFpc%7C1624087775%7C7384efc96dc8685ae69535949c01f4986d1e345cfac9353abd0b47a40581ddfe; is_dev=false; is_boe=false; tt_webid=6975784682395272735; Hm_lvt_3e79ab9e4da287b5752d8048743b95e6=1624087778,1624176441; _gid=GA1.2.684041826.1624176445; CNZZDATA1278124308=201908327-1617401692-https%253A%252F%252Fwww.baidu.com%252F%7C1624171755; city_name=%E5%B9%BF%E5%B7%9E; Hm_lpvt_3e79ab9e4da287b5752d8048743b95e6=1624176807'
}


def spider(c):
    n = 1
    data = []
    for i in range(0, 22):
        num = str(i * 10)
        time.sleep(1)
        response = requests.request("GET", url.format(num), headers=headers).text
        result = json.loads(response)['data']['list']
        for j in range(0, len(result)):
            name = result[j]['series_name']
            count = result[j]['count']
            rank = result[j]['rank']
            Min_price = result[j]['min_price']
            Max_price = result[j]['max_price']
            IMG_ADDRESS = result[j]['image']
            d = (name, count)
            data.append(d)
            sql = "insert into Car(ID,NAME,count,rank,Min_price,Max_price,IMG_ADDRESS) values(%d,'%s',%d,%d,%f,%f,'%s')" \
                  % (n, name, int(count), int(rank), float(Min_price), float(Max_price), IMG_ADDRESS)
            c.execute(sql)
            n += 1
        print("第" + str(i+1) + "页完成！")
    conn.commit()
    conn.close()
    # (
    #     WordCloud()
    #         .add(series_name="销量分析", data_pair=data, word_size_range=[6, 66])
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title="销量分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
    #         ),
    #         tooltip_opts=opts.TooltipOpts(is_show=True),
    #     )
    #         .render("词云图.html")
    # )


if __name__ == '__main__':
    conn = sqlite3.connect('car.sqlite')
    c = conn.cursor()
    spider(c)
